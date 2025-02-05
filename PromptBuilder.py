from Translator import *
import base64

class PromptBuilder:
    """
    Class to engineer prompts
    """
    
    def __init__(self, translator):
        self.translator = translator
        self.valid_flags = ["base64_encode", "translate"]
    
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
    
    # current valid flags: base64_encode, translate
    
    def attack(self, prompt: str, attack_flags: list) -> str:
        # given a prompt, return an engineered prompt based off flags
        # step 1: error checking
        if len(prompt) <= 0:
            raise ValueError("Must be non null prompt")
        if not all(item in self.valid_flags for item in attack_flags):
            print(attack_flags)
            print(self.valid_flags)
            raise ValueError("Invalid attack flag! Valid attack flags are: ", self.valid_flags)
        engineered_prompt = prompt
        b64 = False
        # step 2: go thru flags, apply prompts step by step
        for flag in attack_flags:
            match flag:
                case "translate":
                    target_lang = input("input a target language: ")
                    engineered_prompt = self.translate(engineered_prompt, target_lang)
                case "base64_encode":
                    b64 = True # this changes prompt to bytes so should be done last?
                case _:
                    print("this hypothetically shouldn't ever occur")
          # step 3: return engineered prompt
        if b64 == True:
            engineered_prompt = self.base64_encode(engineered_prompt)

        return engineered_prompt
                    
            
                

      

