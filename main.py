import requests
import json
import re

class CommentAnalyzer:
    def __init__(self, config):
        self.ollama_url = config["ollama_url"]
        self.model = config["model"]
        self.prompt_path = config["prompt_path"]
        self.debug_log = config["debug_log"]
        self.prompt_template = self._load_prompt_template()

    def analyze_comment(self, comment):
        prompt = self._generate_prompt_for_comment(comment)
        if not prompt:
            print("No prompt available. Aborting analysis.")
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
            if self.debug_log:
                print("Raw response:\n", data.get("response", "No response content"))
            answer = data.get("response", "")
            extracted_json_str = self._extract_json_from_answer(answer)
            if extracted_json_str:
                try:
                    result_json = json.loads(extracted_json_str)
                    if self.debug_log:
                        print("Parsed JSON:", result_json)
                    return result_json
                except json.JSONDecodeError:
                    print("Could not parse JSON. Raw output:")
                    print(answer)
                    return None
            else:
                return None
        except requests.RequestException as e:
            print(f"Request error: {e}")
            return None

    def _generate_prompt_for_comment(self, comment):
        if self.prompt_template:
            return self.prompt_template.replace("${{COMMENT}}", comment)
        return None

    def _extract_json_from_answer(self, answer):
        matches = re.findall(r'\{\s*"stock_symbol"\s*:\s*".+?",\s*"rating"\s*:\s*-?\d+\s*\}', answer)
        if not matches:
            print("No JSON object found in response.")
            print(answer)
            return None
        return matches[-1]
    
    def _load_prompt_template(self):
        try:
            with open(self.prompt_path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            print(f"Error while loading prompt template: {e}")
            return None


if __name__ == "__main__":
    config_path = "config.json"
    configuration = None
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            configuration = json.load(f)
    except Exception as e:
        print(f"Error loading config file '{config_path}': {e}")
        raise e
    analyzer = CommentAnalyzer(configuration)
    result = analyzer.analyze_comment("I'm really bullish on AMD right now — their earnings blew expectations!")
    print(result)