class PromptBuilder:
    """
    Class to engineer prompts
    """
    
    def __init__(self):
        pass
    
    def base64_encode(self, prompt: str)->str:
        """Encodes prompt in base64

        Args:
            prompt (str): Prompt as string

        Returns:
            str: Base64 encoded prompt
        """
        
    def add_details(self, prompt: str)-> str:
        """Adds details to prompt

        Args:
            prompt (str): Prompt as string

        Returns:
            str: Orginial prompt with details appended
        """
    
    def translate(self, prompt: str, language: str)->str:
        """Translates english prompt to another language

        Args:
            prompt (str): Prompt to translate
            language (str): Language to translate to

        Returns:
            str: Original prompt translated 
        """
        #add exception if language not found