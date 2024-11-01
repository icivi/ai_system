# @title model_llm.py
import random, os
from dataclasses import dataclass
from typing import Dict, List, Optional
from datetime import datetime
from collections import Counter
from cerebras.cloud.sdk import Cerebras


# os.environ["CEREBRAS_API_KEY"] = "csk-xdkjrkc645hjpxm6883c559hw35t8x35nrkcjpjpcyexymnw" # так не желательно
# client = Cerebras(
#     # This is the default and can be omitted
#     api_key=os.environ.get("CEREBRAS_API_KEY"),
#     # api_key=userdata.get("CEREBRAS_API_KEY"),
# )


import os
os.environ["CEREBRAS_API_KEY"] = "csk-xdkjrkc645hjpxm6883c559hw35t8x35nrkcjpjpcyexymnw"


class ModelLLM:
    """ """

    def __init__(self):

        self.client = Cerebras(
            timeout = 20,
            # api_key=os.environ.get("CEREBRAS_API_KEY"),
            # api_key='csk-xdkjrkc645hjpxm6883c559hw35t8x35nrkcjpjpcyexymnw',
            api_key=os.environ.get("CEREBRAS_API_KEY"),
        )

    def generate_response(self, input_prompt: dict, system_prompt: dict) -> str:
        """
        Метод для генерации ответа от модели
        Args:
            input_prompt (dict): Словарь с входным промптом
            system_prompt (dict): Словарь с системным промптом
        Returns:
            str: Ответ модели
        """
        messages = [
            {"role": "system", "content": system_prompt["content"]},
            {"role": "user", "content": input_prompt["content"]},
        ]

        chat_completion = self.client.chat.completions.create(
            messages=messages,
            model="llama3.1-70b",
            max_tokens=1024,
            temperature=1,
            top_p=1
        )

        return chat_completion.choices[0].message.content

class Sellected_Model:
    """Класс для выбора модел"""

    def __init__(self):
        self.model = ModelLLM()

    def get_response(self, input_prompt: dict, system_prompt: dict) -> str:
        """
        Метод для получения ответа от модели
        Args:
            input_prompt (dict): Словарь с входным промптом
            system_prompt (dict): Словарь с системным промптом
        Returns:
            str: Ответ модели
        """
        return self.model.generate_response(input_prompt, system_prompt)
