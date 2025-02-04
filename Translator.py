import requests
from dotenv import load_dotenv
import os

target_languages = ["AR","BG","CS", "DA", "DE", "EL", 
                    "EN", "ES", "ET", "FI", "FR", "HU", 
                    "ID", "IT","JA","KO","LT","LV","NB",
                    "NL","PL","PT","PT","RO","RU","SK","SL", 
                    "SV","TR","UK","ZH"]

source_languages = ["AR","BG","CS","DA","DE","EL","EN",
                    "ES", "ET", "FI", "FR", "HU", "ID",
                    "IT", "JA", "KO", "LT", "LV", "NB",
                    "NL","PL","PT","RO","RU","SK","SL",
                    "SV","TR","UK","ZH"]


class Translator:

    def __init__(self, auth_key, url):
        self.auth_key = auth_key
        self.url = url
    
    def translate(self, source_lang, target_lang, text):

        if target_lang not in target_languages or source_lang not in source_languages:
            raise ValueError("Unsupported Language")

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
                return result["translations"][0].get("text", "Translation not found")
            else:
                raise ValueError("Error: No translation") 
            
        except Exception as e:
            raise ValueError( f"Request error: {e}")


