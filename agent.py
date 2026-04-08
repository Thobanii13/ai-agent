#!/usr/bin/env python3
"""
Local AI Agent - Main Orchestrator (Fixed)
"""

import os
import sys
import requests
import subprocess
from datetime import datetime
from logger import SessionLogger


class LocalAIAgent:
    def __init__(self):
        self.model_local = "deepseek-r1:1.5b"
        self.model_fallback = "phi"
        self.model_cloud = "gemini-1.5-flash"

        self.logger = SessionLogger(model=self.model_local)

        self.session_start = datetime.now()
        self.session_id = self.session_start.strftime("%Y%m%d_%H%M%S")

        self.force_model = None
        self.check_connectivity()

    def check_connectivity(self):
        try:
            response = requests.get("https://www.google.com", timeout=5)
            self.is_online = response.status_code == 200
        except:
            self.is_online = False

    def query_local_model(self, prompt):
        try:
            result = subprocess.run(
                ["ollama", "run", self.model_local, prompt],
                capture_output=True,
                text=True,
                timeout=120
            )

            if result.returncode == 0:
                return result.stdout.strip()

            print("  [!] deepseek failed, trying phi...")
            result = subprocess.run(
                ["ollama", "run", self.model_fallback, prompt],
                capture_output=True,
                text=True,
                timeout=120
            )

            if result.returncode == 0:
                return result.stdout.strip()

            return "Error: both local models failed"

        except Exception as e:
            return f"Error: {str(e)}"

    def query_gemini(self, prompt):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            return "Error: GEMINI_API_KEY not set"

        if not self.is_online:
            return "Error: No internet connection"

        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model_cloud}:generateContent?key={api_key}"

            data = {
                "contents": [
                    {"parts": [{"text": prompt}]}
                ]
            }

            response = requests.post(url, json=data, timeout=30)

            if response.status_code == 200:
                result = response.json()
                return result["candidates"][0]["content"]["parts"][0]["text"]

            return f"Error: Gemini returned {response.status_code}"

        except Exception as e:
            return f"Error: {str(e)}"

    def query_model(self, prompt):
        # Log user input
        self.logger.add("user", prompt)

        # Routing
        if self.force_model == "cloud":
            model_name = self.model_cloud
            response = self.query_gemini(prompt)

        elif self.force_model == "local":
            model_name = self.model_local
            response = self.query_local_model(prompt)

        else:
            if self.is_online and len(prompt) > 200:
                model_name = self.model_cloud
                response = self.query_gemini(prompt)
            else:
                model_name = self.model_local
                response = self.query_local_model(prompt)

        # Update model + log response
        self.logger.model = model_name
        self.logger.add("assistant", response)

        return response

    def save_session(self):
        if self.logger.message_count() == 0:
            print("  [!] No messages to save.")
            return

        log_file = self.logger.save()
        print(f"✓ Session saved to {log_file}")

        if os.path.exists("compiler.py"):
            try:
                result = subprocess.run(
                    [sys.executable, "compiler.py", "--all"],
                    capture_output=True,
                    text=True
                )

                if result.returncode == 0:
                    print("✓ Knowledge compiled")
                else:
                    print("⚠ Compilation issue")

            except Exception as e:
                print(f"⚠ Could not compile: {str(e)}")

    def print_header(self):
        status = "🟢 Online" if self.is_online else "🔴 Offline"

        print("=" * 50)
        print("  LOCAL AI AGENT")
        print("=" * 50)
        print(f"  Status  : {status}")
        print(f"  Model   : {self.model_local} (local)")
        print(f"  Upgrade : {self.model_cloud if self.is_online else 'unavailable'}")
        print("-" * 50)
        print("  Commands:")
        print("   /local   → force local model")
        print("   /cloud   → force cloud model")
        print("   /status  → show status")
        print("   /save    → save session")
        print("   /quit    → exit")
        print("=" * 50)

    def run(self):
        self.print_header()

        while True:
            try:
                user_input = input("\nYou: ").strip()

                if not user_input:
                    continue

                if user_input.startswith("/"):
                    cmd = user_input[1:].lower()

                    if cmd == "quit":
                        self.save_session()
                        print("👋 Goodbye")
                        break

                    elif cmd == "local":
                        self.force_model = "local"
                        print("🔧 Using local model")
                        continue

                    elif cmd == "cloud":
                        self.force_model = "cloud"
                        print("☁ Using cloud model")
                        continue

                    elif cmd == "status":
                        self.check_connectivity()
                        print("🟢 Online" if self.is_online else "🔴 Offline")
                        continue

                    elif cmd == "save":
                        self.save_session()
                        continue

                    else:
                        print("Unknown command")
                        continue

                response = self.query_model(user_input)
                print(f"\nAgent: {response}")

            except KeyboardInterrupt:
                print("\nSaving before exit...")
                self.save_session()
                break

            except Exception as e:
                print(f"Error: {str(e)}")


if __name__ == "__main__":
    agent = LocalAIAgent()
    agent.run()