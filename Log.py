import pandas as pd
import os

class Log:
    """
    Class to log prompts/outputs to create a dataset
    """
    def __init__(self, filename="log.json"):
        """
        Initializes the log. If the file exists, load existing data.
        """
        self.filename = filename
        if os.path.exists(filename):
            self.df = pd.read_json(filename)
        else:
            self.df = pd.DataFrame(columns=["prompt", "output_deepseek", "output_chat", "score_deepseek", "score_chat", "toxic_deepseek", "topic_chat", "strategies"])

    def add_attempt(self, prompt: str, output_deepseek: str, output_chat: str, score_deepseek: float, score_chat: float, toxic_deepseek: int, toxic_chat: int, prompts_used):
        """
        Adds a new record to the log.

        Args:
            prompt (str): The input prompt given to the model.
            output (str): The model's response.
            score (float): The toxicity score (0-1 scale).
            toxic (int): 0 if not toxic, 1 if toxic.
        """
        new_entry = pd.DataFrame([{
            "prompt": prompt,
            "output_deepseek": output_deepseek,
            "output_chat": output_chat,
            "score_deepseek": score_deepseek,
            "score_chat": score_chat,
            "toxic_deepseek": toxic_deepseek,
            "toxic_chat": toxic_chat, #bool(toxic)  # Convert to True/False
            "strategies": prompts_used 
        }])
        self.df = pd.concat([self.df, new_entry], ignore_index=True)

    def write_to_file(self):
        """
        Writes the log data to a CSV file.
        """
        self.df.to_json(self.filename, index=False)
    def getToxicity(self) -> int:
        """
        Asks the user whether the output is toxic or not.

        Returns:
            int: 1 if toxic, 0 if not toxic.
        """
        while True:
            user_input = input("Input 1 for 'This is toxic', 2 for 'This is not toxic': ").strip()
            if user_input in ["1", "2"]:
                return int(user_input) - 1  # Converts "1" -> 1 (toxic) and "2" -> 0 (not toxic)
            else:
                print("Invalid input. Please enter 1 for toxic or 2 for not toxic.")