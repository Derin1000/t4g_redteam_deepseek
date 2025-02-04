from Model import *
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

model = Model(MODEL_NAME)
translator = Translator(DEEPL_KEY, DEEPL_URL)
builder = PromptBuilder(translator)
metrics_generator = Metrics()
dataset = Log()

prompt = "Hello World!"

engineered_prompt = builder.translate(prompt, "ZH")

print(engineered_prompt)

enginered_prompt = builder.base64_encode(prompt)

output = model.query(prompt)
toxicity = metrics_generator.toxicity_score(output)

#add get toxicity flag from user
dataset.add_attempt(enginered_prompt,output,toxicity,0)
dataset.write_to_file("log.csv")
print(output)