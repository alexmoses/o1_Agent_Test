from openai import OpenAI

class BaseAgent:
    def __init__(self):
        self.client = OpenAI()
        self.model = "gpt-4o"
        self.system_role = "You are an AI assistant."  # Default role

    def get_completion(self, prompt):
        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_role},
                    {"role": "user", "content": prompt}
                ]
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"An error occurred: {e}" 