from Translator import *
import base64

class PromptBuilder:
    """
    Class to engineer prompts
    """
    
    def __init__(self, translator):
        self.translator = translator
    
    def base64_encode(self, prompt: str)->str:
        """Encodes prompt in base64

        Args:
            prompt (str): Prompt as string

        Returns:
            str: Base64 encoded prompt
        """
        return base64.b64encode(prompt.encode("utf-8"))

    def add_details(self, prompt: str)-> str:
        """Adds details to prompt

        Args:
            prompt (str): Prompt as string

        Returns:
            str: Orginial prompt with details appended
        """
        return None
    
    def translate(self, prompt: str, language: str)->str:
        source_lang = "EN"
        return self.translator.translate(source_lang, language, prompt)