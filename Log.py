import pandas as pd

class Log:
    """
    class to log prompts/outputs to create a dataset
    """
    def __init__(self):
        self.df = pd.Dataframe()
    
    def add_attempt(self, prompt: str,output: str,score: str,toxic: int):
        """Adds jailbreaking attempt to dataset

        Args:
            prompt (str): Prompt tried
            output (str): Output from model
            score (str): Toxicity score measured
            toxic (int): 0 if not toxic or 1 if toxic
        """
        self.df['prompt'] = prompt
        self.df['output'] = output
        self.df['score'] = score
        self.df['toxic'] = toxic
