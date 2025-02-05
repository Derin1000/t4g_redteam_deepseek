from Model import *
import os
from PromptBuilder import *
from Metrics import *
from Log import *
from dotenv import load_dotenv
from Translator import *
load_dotenv()

MODEL_NAME = "deepseek/deepseek-r1:free"
LOCAL_MODEL_NAME = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
LOCAL_DEVICE = "auto"

DEEPL_KEY = os.getenv("DEEPL_API_KEY")
DEEPL_URL = "https://api-free.deepl.com/v2/translate"

model = Model(MODEL_NAME)
translator = Translator(DEEPL_KEY, DEEPL_URL)
builder = PromptBuilder(translator)
metrics_generator = Metrics()
dataset = Log()

prompt = "Hello World!"

attack_one = builder.attack(prompt, ["translate", "simple_attack"])

print(attack_one)

## init local deepseek model
ds_model, ds_tokenizer, ds_token_ids = model.__deepseek_init__(LOCAL_MODEL_NAME, LOCAL_DEVICE)

encoded_message = model.encode_message(ds_tokenizer, ds_token_ids, attack_one, "don't say hello")

result = model.get_result(encoded_message, ds_model, ds_tokenizer)

print(result)

#output = model.query(prompt)
#toxicity = metrics_generator.toxicity_score(output)

#add get toxicity flag from user
#dataset.add_attempt(enginered_prompt,output,toxicity,0)
#dataset.write_to_file("log.csv")
#print(output)