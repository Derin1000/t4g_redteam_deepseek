from openai import OpenAI

class Model:
    """_summary_
    """
    def __init__(self, model: str):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key= None,
        )
        self.model = model
        return 
    
    def query(self, prompt: str) -> str:
        """Queries model with a prompt

        Args:
            prompt (str): Text prompt to provide model

        Returns:
            str: Model output
        """
        completion = self.client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
                "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
            },
            model= self.model,
            messages=[
                {
                "role": "user",
                "content": prompt
                }
            ]
        )
        try:
            return completion.choices[0].message.content
        except:
            print(f"Error generating output: {completion.error['metadata']['raw']}")
            return None