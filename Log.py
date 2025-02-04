import pandas as pd
import os

class Log:
    """
    Class to log prompts/outputs to create a dataset
    """
    def __init__(self, filename="log.csv"):
        """
        Initializes the log. If the file exists, load existing data.
        """
        self.filename = filename
        if os.path.exists(filename):
            self.df = pd.read_csv(filename)
        else:
            self.df = pd.DataFrame(columns=["prompt", "output", "score", "toxic"])

    def add_attempt(self, prompt: str, output: str, score: float, toxic: int):
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
            "output": output,
            "score": score,
            "toxic": bool(toxic)  # Convert to True/False
        }])
        self.df = pd.concat([self.df, new_entry], ignore_index=True)

    def write_to_file(self):
        """
        Writes the log data to a CSV file.
        """
        self.df.to_csv(self.filename, index=False)
