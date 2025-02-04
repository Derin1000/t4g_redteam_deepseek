import requests
from dotenv import load_dotenv
import os


class Translator:

    def __init__(self, auth_key, url):
        self.auth_key = auth_key
        self.url = url
    
    def translate(self, source_lang, target_lang, text):
        try:
            data = {
                "auth_key" : self.auth_key,
                "text" : text,
                "source_lang": source_lang,
                "target_lang": target_lang
            }

            response = requests.post( self.url, data=data)
            result = response.json()
            if "translations" in result and len(result["translations"]) > 0:
                print("successful translate")
                return result["translations"][0].get("text", "Translation not found")
            else:
                return "Error: No translation"
            
        except Exception as e:
            return f"Request error: {e}"


