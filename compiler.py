"""
compiler.py — Knowledge compiler for the AI agent memory system.

Reads raw session logs from memory/raw/logs/
Sends them to Ollama to extract concepts and connections.
Saves structured knowledge articles to memory/knowledge/
Updates memory/index.md with new entries.

Usage:
    python compiler.py              # compile all unprocessed logs
    python compiler.py --all        # recompile everything
"""

import os
import sys
import json
import requests
from datetime import datetime


LOGS_DIR    = os.path.join(os.path.dirname(__file__), "memory", "raw", "logs")
CONCEPTS_DIR = os.path.join(os.path.dirname(__file__), "memory", "knowledge", "concepts")
CONNECTIONS_DIR = os.path.join(os.path.dirname(__file__), "memory", "knowledge", "connections")
INDEX_FILE  = os.path.join(os.path.dirname(__file__), "memory", "index.md")
COMPILED_TRACKER = os.path.join(os.path.dirname(__file__), "memory", ".compiled.json")

OLLAMA_URL  = "http://localhost:11434/api/generate"
MODEL       = "deepseek-r1:1.5b"


def ask_ollama(prompt: str) -> str:
    """Send a prompt to Ollama and return the response."""
    try:
        response = requests.post(OLLAMA_URL, json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }, timeout=120)
        result = response.json().get("response", "").strip()
        # Strip thinking tags if deepseek-r1 leaks them
        if "<think>" in result:
            result = result.split("</think>")[-1].strip()
        return result
    except Exception as e:
        return f"[Ollama error: {e}]"


def load_compiled_tracker() -> list:
    """Load list of already-compiled log filenames."""
    if not os.path.exists(COMPILED_TRACKER):
        return []
    with open(COMPILED_TRACKER, "r") as f:
        return json.load(f)


def save_compiled_tracker(compiled: list):
    """Save updated list of compiled log filenames."""
    with open(COMPILED_TRACKER, "w") as f:
        json.dump(compiled, f, indent=2)


def get_unprocessed_logs(recompile_all: bool = False) -> list:
    """Return list of log files not yet compiled."""
    if not os.path.exists(LOGS_DIR):
        return []
    all_logs = sorted([f for f in os.listdir(LOGS_DIR) if f.endswith(".md")])
    if recompile_all:
        return all_logs
    compiled = load_compiled_tracker()
    return [f for f in all_logs if f not in compiled]


def read_log(filename: str) -> str:
    """Read a raw log file."""
    with open(os.path.join(LOGS_DIR, filename), "r", encoding="utf-8") as f:
        return f.read()


def extract_concepts(log_content: str, log_filename: str) -> dict:
    """Ask Ollama to extract concepts from a log."""
    prompt = f"""You are a knowledge extraction assistant.

Read this conversation log and extract the key concepts discussed.

For each concept:
- Give it a short clear title
- Write 2-3 sentences explaining it
- Note why it matters

Return ONLY a JSON array like this:
[
  {{"title": "concept name", "explanation": "what it is", "why_it_matters": "why important"}},
  {{"title": "another concept", "explanation": "what it is", "why_it_matters": "why important"}}
]

Return ONLY the JSON array. No other text.

LOG:
{log_content[:3000]}
"""
    response = ask_ollama(prompt)
    try:
        # Try to find JSON array in response
        start = response.find("[")
        end = response.rfind("]") + 1
        if start != -1 and end > start:
            return json.loads(response[start:end])
    except Exception:
        pass
    # Fallback if JSON parsing fails
    return [{"title": f"Session {log_filename}", "explanation": response[:200], "why_it_matters": "Extracted from session log"}]


def extract_connections(log_content: str) -> list:
    """Ask Ollama to extract connections/decisions from a log."""
    prompt = f"""You are a knowledge extraction assistant.

Read this conversation log and extract:
1. Key decisions made
2. Lessons learned
3. Links between different topics

Return ONLY a JSON array like this:
[
  {{"type": "decision", "description": "what was decided and why"}},
  {{"type": "lesson", "description": "what was learned"}},
  {{"type": "link", "description": "how two topics connect"}}
]

Return ONLY the JSON array. No other text.

LOG:
{log_content[:3000]}
"""
    response = ask_ollama(prompt)
    try:
        start = response.find("[")
        end = response.rfind("]") + 1
        if start != -1 and end > start:
            return json.loads(response[start:end])
    except Exception:
        pass
    return [{"type": "lesson", "description": response[:200]}]


def save_concept(concept: dict, source_log: str):
    """Save a concept as a markdown file in knowledge/concepts/."""
    os.makedirs(CONCEPTS_DIR, exist_ok=True)
    title = concept.get("title", "untitled").lower().replace(" ", "-").replace("/", "-")
    filename = f"{title}.md"
    filepath = os.path.join(CONCEPTS_DIR, filename)

    content = f"""# {concept.get('title', 'Untitled')}

{concept.get('explanation', '')}

## Why it matters

{concept.get('why_it_matters', '')}

---
*Extracted from: {source_log}*
*Date: {datetime.now().strftime('%Y-%m-%d')}*
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filename


def save_connections(connections: list, source_log: str):
    """Save connections as a markdown file in knowledge/connections/."""
    os.makedirs(CONNECTIONS_DIR, exist_ok=True)
    date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"connections_{date_str}.md"
    filepath = os.path.join(CONNECTIONS_DIR, filename)

    lines = [f"# Connections — {datetime.now().strftime('%Y-%m-%d')}\n"]
    lines.append(f"*Source: {source_log}*\n")

    for item in connections:
        kind = item.get("type", "note").upper()
        desc = item.get("description", "")
        lines.append(f"\n## [{kind}]\n{desc}")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return filename


def update_index(new_concepts: list, new_connections: list):
    """Update memory/index.md with newly added knowledge."""
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Update concepts section
    concept_lines = "\n".join([f"- [{c}](knowledge/concepts/{c})" for c in new_concepts])
    connections_lines = "\n".join([f"- [{c}](knowledge/connections/{c})" for c in new_connections])

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Append update log at bottom
    update_entry = f"""
---
## Update — {timestamp}

### New concepts
{concept_lines if concept_lines else "None"}

### New connections
{connections_lines if connections_lines else "None"}
"""
    with open(INDEX_FILE, "a", encoding="utf-8") as f:
        f.write(update_entry)


def compile_log(filename: str) -> dict:
    """Full pipeline: read log → extract → save → return summary."""
    print(f"\n  Processing: {filename}")

    log_content = read_log(filename)

    print(f"  Extracting concepts...")
    concepts = extract_concepts(log_content, filename)
    saved_concepts = []
    for concept in concepts:
        saved = save_concept(concept, filename)
        saved_concepts.append(saved)
        print(f"    + concept: {concept.get('title')}")

    print(f"  Extracting connections...")
    connections = extract_connections(log_content)
    saved_conn = save_connections(connections, filename)
    print(f"    + connections saved: {saved_conn}")

    update_index(saved_concepts, [saved_conn])

    return {"concepts": saved_concepts, "connections": saved_conn}


def main():
    recompile_all = "--all" in sys.argv

    print("=== Knowledge Compiler ===")
    print(f"Model: {MODEL}")
    print(f"Mode: {'recompile all' if recompile_all else 'new logs only'}\n")

    logs = get_unprocessed_logs(recompile_all)

    if not logs:
        print("No new logs to compile. Run your agent first to generate logs.")
        return

    print(f"Found {len(logs)} log(s) to process...")

    compiled = load_compiled_tracker()
    results = []

    for log_file in logs:
        result = compile_log(log_file)
        results.append({"file": log_file, **result})
        if log_file not in compiled:
            compiled.append(log_file)

    save_compiled_tracker(compiled)

    print(f"\n=== Done ===")
    print(f"Processed: {len(results)} log(s)")
    print(f"Check memory/knowledge/ for new articles")
    print(f"Check memory/index.md for updated navigation")


if __name__ == "__main__":
    main()