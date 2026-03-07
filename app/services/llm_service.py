import requests
import yaml
from app.config import OLLAMA_BASE_URL, DEFAULT_MODEL

class LLMService:

    def __init__(self):
        with open("app/prompts/prompts.yaml", "r") as f:
            self.prompts = yaml.safe_load(f)

    def render_prompt(self, prompt_name, variables):
        prompt_data = self.prompts[prompt_name]
        system = prompt_data["system"]
        user = prompt_data["user"]

        for key, value in variables.items():
            user = user.replace(f"{{{{{key}}}}}", value)

        return f"{system}\n\n{user}"

    def generate(self, category, variables):

        with open(f"app/prompts/{category}.yaml", "r") as f:
            prompt_data = yaml.safe_load(f)

        system = prompt_data["system"]
        user = prompt_data["user"]

        for key, value in variables.items():
            user = user.replace(f"{{{{{key}}}}}", value)

        final_prompt = f"{system}\n\n{user}"

        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json={
                "model": DEFAULT_MODEL,
                "prompt": final_prompt,
                "stream": False
            }
        )

        return response.json()["response"]