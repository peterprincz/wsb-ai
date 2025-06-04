from typing import Optional
import requests
import json
import re
import logging as log
from config.appconfig import config


from model.dto_models import SentinentDTO

class CommentAnalyzer:
    def __init__(self):
        self.ollama_url = config.ollama_url
        self.model = config.model
        self.prompt_template = self._load_prompt_template(config.prompt_path)

    def analyze_comment(self, comment: str) -> Optional[SentinentDTO]:
        prompt = self._generate_prompt_for_comment(comment)
        if not prompt:
            log.info("No prompt available. Aborting analysis.")
            return None
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        try:
            response = requests.post(self.ollama_url, json=payload)
            response.raise_for_status()
            data = response.json()
            log.debug("Raw response:\n", data.get("response", "No response content"))
            answer = data.get("response", "")
            extracted_json_str = self._extract_json_from_answer(answer)
            if extracted_json_str:
                try:
                    result_json = json.loads(extracted_json_str)
                    log.debug("Parsed JSON:", result_json)
                    return SentinentDTO.from_dict(result_json)
                except Exception:
                    log.error("Could not parse JSON. Raw output:" + answer)
                    return None
            else:
                return None
        except requests.RequestException as e:
            log.error(f"Request error: {e}")
            return None

    def _generate_prompt_for_comment(self, comment):
        if self.prompt_template:
            return self.prompt_template.replace("${{COMMENT}}", comment)
        return None

    def _extract_json_from_answer(self, answer):
        matches = re.findall(r'\{\s*"stock_symbol"\s*:\s*".+?",\s*"rating"\s*:\s*-?\d+\s*\}', answer)
        if not matches:
            log.error("No JSON object found in response.: " + answer)
            return None
        return matches[-1]
    
    def _load_prompt_template(self, prompt_path: str):
        try:
            with open(prompt_path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            log.error(f"Error while loading prompt template: {e}")
            return None

