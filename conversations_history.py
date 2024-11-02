# @title conversations_history.py
import json
from typing import List, Dict
from pathlib import Path
from datetime import datetime

class SaveToFile:
    def __init__(self, filename: str = "/content/ai_system/conversation_history.json"):
        self.filename = filename

    def save(self, conversation: List[Dict]) -> None:
        """Save conversation history to a JSON file"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(conversation, f, ensure_ascii=False, indent=2)

    def load(self) -> List[Dict]:
        """Load conversation history from JSON file"""
        if not Path(self.filename).exists():
            return []
        with open(self.filename, 'r', encoding='utf-8') as f:
            return json.load(f)

class HistoryCollector:
    def __init__(self):
        self.conversation_history: List[Dict] = []
        self.saver = SaveToFile()
        # Load existing conversation if any
        self.conversation_history = self.saver.load()

    def set_system_prompt(self, system_prompt: str) -> None:
        """Set the system prompt and add it to the conversation history"""
        current_time = datetime.now().strftime("%Y.%m.%d %H:%M")
        entry = {
            "role": "system",
            "content": system_prompt,
            "datetime": current_time
        }
        self.conversation_history.append(entry)
        # Save after setting the system prompt
        self.saver.save(self.conversation_history)

    def add_message(self, role: str, content: str) -> None:
        """Add a new message to conversation history"""
        current_time = datetime.now().strftime("%Y.%m.%d %H:%M")
        entry = {
            "role": role,
            "content": content,
            "datetime": current_time
        }
        self.conversation_history.append(entry)
        # Save after each update
        self.saver.save(self.conversation_history)

    def get_history(self) -> List[Dict]:
        """Get the full conversation history"""
        return self.conversation_history

    def clear_history(self) -> None:
        """Clear the conversation history"""
        self.conversation_history = []
        self.saver.save(self.conversation_history)
