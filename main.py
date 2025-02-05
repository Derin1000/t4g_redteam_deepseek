#from Model import *
import os
from PromptBuilder import *
from Metrics import *
from Log import *
from dotenv import load_dotenv
from Translator import *
load_dotenv()

MODEL_NAME = "deepseek/deepseek-r1:free"

DEEPL_KEY = os.getenv("DEEPL_API_KEY")
DEEPL_URL = "https://api-free.deepl.com/v2/translate"

#model = Model(MODEL_NAME)
translator = Translator(DEEPL_KEY, DEEPL_URL)
builder = PromptBuilder(translator)
metrics_generator = Metrics()
dataset = Log()

prompt = "Hello World!"

attack_one = builder.attack(prompt, ["base64_encode", "translate"])

print(attack_one)



output = model.query(prompt)
toxicity = metrics_generator.toxicity_score(output)

#add get toxicity flag from user
dataset.add_attempt(enginered_prompt,output,toxicity,0)
print(output)