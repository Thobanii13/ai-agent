"""
agent.py - Main AI Agent Orchestrator
Connects: connectivity check → model router → logger → compiler
"""

import os
import sys
import requests
from datetime import datetime
from logger import SessionLogger

# ── Config ──────────────────────────────────────────────────────────────────
LOCAL_MODEL   = "deepseek-r1:1.5b"       # primary local model
FALLBACK_MODEL = "phi"                    # fallback if deepseek fails
OLLAMA_URL    = "http://localhost:11434"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_URL    = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
CHECK_URL     = "https://www.google.com"  # used to test connectivity

# ── Connectivity ─────────────────────────────────────────────────────────────
def is_online() -> bool:
    """Check if the machine has internet access."""
    try:
        requests.get(CHECK_URL, timeout=3)
        return True
    except requests.RequestException:
        return False

# ── Local model (Ollama) ─────────────────────────────────────────────────────
def ask_local(prompt: str, model: str = LOCAL_MODEL) -> str:
    """Send a prompt to a local Ollama model."""
    try:
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={"model": model, "prompt": prompt, "stream": False},
            timeout=120
        )
        response.raise_for_status()
        raw = response.json().get("response", "").strip()

        # Strip <think>...</think> blocks from deepseek-r1
        import re
        raw = re.sub(r"<think>.*?</think>", "", raw, flags=re.DOTALL).strip()
        return raw

    except requests.exceptions.ConnectionError:
        return "[ERROR] Ollama is not running. Start it with: ollama serve"
    except Exception as e:
        # Try fallback model
        if model != FALLBACK_MODEL:
            print(f"  [!] {model} failed, trying {FALLBACK_MODEL}...")
            return ask_local(prompt, model=FALLBACK_MODEL)
        return f"[ERROR] Local model failed: {e}"

# ── Cloud model (Gemini) ──────────────────────────────────────────────────────
def ask_cloud(prompt: str) -> str:
    """Send a prompt to Gemini Flash."""
    if not GEMINI_API_KEY:
        return "[ERROR] GEMINI_API_KEY not set. Run: setx GEMINI_API_KEY your_key_here"
    try:
        response = requests.post(
            f"{GEMINI_URL}?key={GEMINI_API_KEY}",
            json={"contents": [{"parts": [{"text": prompt}]}]},
            timeout=30
        )
        response.raise_for_status()
        return response.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
    except Exception as e:
        return f"[ERROR] Cloud model failed: {e}"

# ── Router ────────────────────────────────────────────────────────────────────
def ask(prompt: str, force_local: bool = False, force_cloud: bool = False) -> tuple[str, str]:
    """
    Route the prompt to the right model.
    Returns (response, model_used)
    """
    online = is_online()

    if force_local or not online:
        source = "local"
        response = ask_local(prompt)
    elif force_cloud:
        source = "cloud"
        response = ask_cloud(prompt)
    else:
        # Default: use local first, upgrade with cloud if online
        source = "local"
        response = ask_local(prompt)

    return response, source

# ── Chat loop ─────────────────────────────────────────────────────────────────
def chat():
    """Interactive chat loop with memory logging."""
    logger = SessionLogger()
    online = is_online()

    print("\n" + "═" * 50)
    print("  LOCAL AI AGENT")
    print("═" * 50)
    print(f"  Status  : {'🟢 Online' if online else '🔴 Offline'}")
    print(f"  Model   : {LOCAL_MODEL} (local)")
    if online and GEMINI_API_KEY:
        print(f"  Upgrade : Gemini Flash (cloud) available")
    print("─" * 50)
    print("  Commands:")
    print("   /local   → force local model")
    print("   /cloud   → force cloud model (Gemini)")
    print("   /status  → show current status")
    print("   /save    → save and compile session")
    print("   /quit    → exit")
    print("═" * 50 + "\n")

    mode = "auto"  # auto | local | cloud

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\nSaving session...")
            break

        if not user_input:
            continue

        # Commands
        if user_input == "/quit":
            print("Saving session...")
            break
        elif user_input == "/local":
            mode = "local"
            print("  [→] Switched to local model\n")
            continue
        elif user_input == "/cloud":
            mode = "cloud"
            print("  [→] Switched to cloud model\n")
            continue
        elif user_input == "/status":
            online = is_online()
            print(f"  Online : {'Yes' if online else 'No'}")
            print(f"  Mode   : {mode}")
            print(f"  Logs   : {len(logger.messages)} messages this session\n")
            continue
        elif user_input == "/save":
            _save_and_compile(logger)
            continue

        # Route prompt
        force_local = mode == "local"
        force_cloud = mode == "cloud"
        response, source = ask(user_input, force_local=force_local, force_cloud=force_cloud)

        # Log both sides
        logger.add_message("user", user_input)
        logger.add_message("assistant", response, metadata={"model": source})

        # Display
        label = "AI (local)" if source == "local" else "AI (cloud)"
        print(f"\n{label}: {response}\n")

    # Auto-save on exit
    _save_and_compile(logger)

def _save_and_compile(logger: SessionLogger):
    """Save the session log and run the compiler."""
    if not logger.messages:
        print("  [!] No messages to save.\n")
        return

    summary = f"Session on {datetime.now().strftime('%Y-%m-%d %H:%M')} with {len(logger.messages)} messages."
    log_path = logger.save(summary=summary)
    print(f"\n  ✓ Session saved → {log_path}")

    # Run compiler
    print("  Compiling knowledge...")
    try:
        import subprocess
        result = subprocess.run(
            [sys.executable, "compiler.py"],
            capture_output=True, text=True
        )
        if "Done" in result.stdout:
            print("  ✓ Knowledge compiled → memory/knowledge/\n")
        else:
            print("  [!] Compiler output:", result.stdout[:200])
    except Exception as e:
        print(f"  [!] Compiler error: {e}\n")

# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    chat()