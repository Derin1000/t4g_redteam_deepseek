class Metrics:
    """
    Run metrics on outputs from model
    """
    def __init__(self):
        pass
    
    def toxicity_score(output: Str)-> float:
        """Generate toxicity score for model output

        Args:
            output (Str): Model output as string

        Returns:
            float: Toxicity score
        """