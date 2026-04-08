#!/usr/bin/env python3
"""
Local AI Agent - Main Orchestrator
Phase 3: Main orchestrator with routing, logging and cloud upgrade
"""

import os
import sys
import json
import requests
import subprocess
from datetime import datetime
from logger import Logger

class LocalAIAgent:
    def __init__(self):
        self.logger = Logger()
        self.session_start = datetime.now()
        self.session_id = self.session_start.strftime("%Y%m%d_%H%M%S")
        self.model_local = "deepseek-r1:1.5b"
        self.model_fallback = "phi"
        self.model_cloud = "gemini-flash"
        self.force_model = None
        self.check_connectivity()

    def check_connectivity(self):
        """Check if we have internet connectivity"""
        try:
            response = requests.get("https://www.google.com", timeout=5)
            self.is_online = response.status_code == 200
        except:
            self.is_online = False

    def get_status(self):
        """Get current agent status"""
        status_icon = "🟢" if self.is_online else "🔴"
        model_info = self.model_cloud if self.force_model == "cloud" else (
            self.model_local if self.force_model == "local" else self.model_local)
        upgrade_info = f"{self.model_cloud} (cloud)" if self.is_online else "unavailable"

        return {
            "status": "Online" if self.is_online else "Offline",
            "status_icon": status_icon,
            "model": model_info,
            "upgrade": upgrade_info
        }

    def query_local_model(self, prompt):
        """Query the local Ollama model"""
        try:
            # Try primary model first
            result = subprocess.run([
                "ollama", "run", self.model_local, prompt
            ], capture_output=True, text=True, timeout=120)

            if result.returncode == 0:
                return result.stdout.strip()

            # Fallback to phi if primary fails
            result = subprocess.run([
                "ollama", "run", self.model_fallback, prompt
            ], capture_output=True, text=True, timeout=120)

            if result.returncode == 0:
                return result.stdout.strip()

            return f"Error: Local models failed - {result.stderr}"
        except Exception as e:
            return f"Error querying local model: {str(e)}"

    def query_gemini(self, prompt):
        """Query Gemini Flash via API"""
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            return "Error: GEMINI_API_KEY not set in environment variables"

        if not self.is_online:
            return "Error: No internet connection for cloud model"

        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"
            headers = {"Content-Type": "application/json"}
            data = {
                "contents": [{
                    "parts": [{"text": prompt}]
                }]
            }

            response = requests.post(url, headers=headers, json=data, timeout=30)
            if response.status_code == 200:
                result = response.json()
                return result["candidates"][0]["content"]["parts"][0]["text"]
            else:
                return f"Error: Gemini API returned {response.status_code}"
        except Exception as e:
            return f"Error querying Gemini: {str(e)}"

    def query_model(self, prompt):
        """Route query to appropriate model"""
        # Log the interaction
        self.logger.log_interaction("user", prompt)

        # Determine which model to use
        if self.force_model == "cloud":
            model_name = self.model_cloud
            response = self.query_gemini(prompt)
        elif self.force_model == "local":
            model_name = self.model_local
            response = self.query_local_model(prompt)
        else:
            # Auto-route based on connectivity and content
            if self.is_online and len(prompt) > 200:  # Use cloud for longer prompts when online
                model_name = self.model_cloud
                response = self.query_gemini(prompt)
            else:
                model_name = self.model_local
                response = self.query_local_model(prompt)

        # Log the response
        self.logger.log_interaction("assistant", response, model=model_name)

        return response

    def save_session(self):
        """Save and compile the current session"""
        log_file = self.logger.save_log()
        print(f"✓ Session saved to {log_file}")

        # Compile the log if compiler exists
        if os.path.exists("compiler.py"):
            try:
                result = subprocess.run([
                    sys.executable, "compiler.py", log_file
                ], capture_output=True, text=True)
                if result.returncode == 0:
                    print("✓ Knowledge compiled successfully")
                else:
                    print(f"⚠ Warning: Compilation had issues:\n{result.stderr}")
            except Exception as e:
                print(f"⚠ Warning: Could not compile knowledge: {str(e)}")

    def print_header(self):
        """Print the agent header"""
        status = self.get_status()
        print("=" * 50)
        print("  LOCAL AI AGENT")
        print("=" * 50)
        print(f"  Status  : {status['status_icon']} {status['status']}")
        print(f"  Model   : {status['model']} ({'local' if 'deepseek' in status['model'] or 'phi' in status['model'] else 'cloud'})")
        print(f"  Upgrade : {status['upgrade']} {'available' if self.is_online else ''}")
        print("-" * 50)
        print("  Commands:")
        print("   /local   → force local model")
        print("   /cloud   → force cloud model (Gemini)")
        print("   /status  → show current status")
        print("   /save    → save and compile session")
        print("   /quit    → exit")
        print("=" * 50)

    def run(self):
        """Main agent loop"""
        self.print_header()

        while True:
            try:
                user_input = input("\nYou: ").strip()

                if not user_input:
                    continue

                # Handle commands
                if user_input.startswith("/"):
                    command = user_input[1:].lower()
                    if command == "quit":
                        self.save_session()
                        print("👋 Goodbye!")
                        break
                    elif command == "local":
                        self.force_model = "local"
                        print("🔧 Forced to local model")
                        continue
                    elif command == "cloud":
                        self.force_model = "cloud"
                        print("☁️ Forced to cloud model")
                        continue
                    elif command == "status":
                        self.check_connectivity()
                        status = self.get_status()
                        print(f"\nStatus: {status['status_icon']} {status['status']}")
                        print(f"Model: {status['model']}")
                        print(f"Upgrade: {status['upgrade']}")
                        continue
                    elif command == "save":
                        self.save_session()
                        continue
                    else:
                        print("❓ Unknown command. Try: /local, /cloud, /status, /save, /quit")
                        continue

                # Query the model
                response = self.query_model(user_input)
                print(f"\nAgent: {response}")

            except KeyboardInterrupt:
                print("\n\n👋 Interrupted. Saving session...")
                self.save_session()
                break
            except Exception as e:
                print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    agent = LocalAIAgent()
    agent.run()