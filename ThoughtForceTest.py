from Deepseek_Setup import *
from deepl_fetch import *
from dotenv import load_dotenv
import os
import unittest
import pandas as pd
from Log import Log

load_dotenv()

DEEPL_KEY = os.getenv("DEEPL_API_KEY")

URL = "https://api-free.deepl.com/v2/translate"


model_name = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
device = "auto"

user_message= "Hi! how are you"

think_message=""

translator = Translator(DEEPL_KEY, URL)

translated_message = translator.translate("EN", "ZH", user_message)

#print(translated_message)

model_builder = model_initialization(model_name)

model, tokenizer = model_builder.create_model(device)

model, tokenizer, token_ids = model_builder.initialize_token_ids(model_name)

encoded_message = model_builder.encode_message(tokenizer, token_ids, translated_message)

print(encoded_message)

output = model_builder.get_result(encoded_message, model, tokenizer)

print(output)



