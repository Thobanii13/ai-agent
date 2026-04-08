"""
logger.py — Session logger for the AI agent memory system.

Saves every conversation session to a dated markdown file in memory/raw/logs/.
Each log captures: timestamp, messages, model used, and a summary placeholder.

Usage:
    from logger import SessionLogger
    log = SessionLogger(model="deepseek-r1:1.5b")
    log.add("user", "explain recursion")
    log.add("assistant", "Recursion is when a function calls itself...")
    log.save()
"""

import os
import json
from datetime import datetime


LOGS_DIR = os.path.join(os.path.dirname(__file__), "memory", "raw", "logs")


class SessionLogger:
    def __init__(self, model: str = "deepseek-r1:1.5b"):
        self.model = model
        self.messages = []
        self.started_at = datetime.now()
        self.session_id = self.started_at.strftime("%Y%m%d_%H%M%S")
        os.makedirs(LOGS_DIR, exist_ok=True)

    def add(self, role: str, content: str):
        """Add a message to this session. role = 'user' or 'assistant'."""
        self.messages.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        })

    def save(self, summary: str = "") -> str:
        """
        Save the session to a markdown log file.
        Returns the path of the saved file.
        """
        date_str = self.started_at.strftime("%Y-%m-%d")
        filename = f"{self.session_id}.md"
        filepath = os.path.join(LOGS_DIR, filename)

        lines = []
        lines.append(f"# Session Log — {date_str} {self.started_at.strftime('%H:%M')}")
        lines.append(f"\n**Model:** {self.model}")
        lines.append(f"**Session ID:** {self.session_id}")
        lines.append(f"**Messages:** {len(self.messages)}")
        lines.append(f"\n---\n")

        if summary:
            lines.append(f"## Summary\n")
            lines.append(summary)
            lines.append(f"\n---\n")

        lines.append(f"## Conversation\n")
        for msg in self.messages:
            role_label = "You" if msg["role"] == "user" else "AI"
            lines.append(f"**[{msg['timestamp']}] {role_label}:**")
            lines.append(msg["content"])
            lines.append("")

        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        return filepath

    def to_transcript(self) -> str:
        """Return full conversation as plain text (for summarizer later)."""
        lines = []
        for msg in self.messages:
            role_label = "User" if msg["role"] == "user" else "Assistant"
            lines.append(f"{role_label}: {msg['content']}")
        return "\n\n".join(lines)

    def message_count(self) -> int:
        return len(self.messages)


def list_logs() -> list:
    """Return a sorted list of all log files (newest first)."""
    if not os.path.exists(LOGS_DIR):
        return []
    files = [f for f in os.listdir(LOGS_DIR) if f.endswith(".md")]
    return sorted(files, reverse=True)


def read_log(filename: str) -> str:
    """Read and return the contents of a log file."""
    filepath = os.path.join(LOGS_DIR, filename)
    if not os.path.exists(filepath):
        return f"Log not found: {filename}"
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    # Quick test — run this file directly to verify it works
    print("Testing logger...\n")

    log = SessionLogger(model="deepseek-r1:1.5b")
    log.add("user", "What is Python?")
    log.add("assistant", "Python is a high-level programming language known for its simple, readable syntax.")
    log.add("user", "Why is it popular?")
    log.add("assistant", "It's popular because it's easy to learn, has a huge library ecosystem, and works for web, data science, AI, and automation.")

    saved_path = log.save(summary="User asked about Python basics. Covered definition and reasons for popularity.")
    print(f"Log saved to: {saved_path}")

    print(f"\nAll logs:")
    for f in list_logs():
        print(f"  - {f}")