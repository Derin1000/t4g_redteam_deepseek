from Model import *
from PromptBuilder import *
from Metrics import *
from Log import *

MODEL_NAME = "deepseek/deepseek-r1:free"

model = Model(MODEL_NAME)
builder = PromptBuilder()
metrics_generator = Metrics()
dataset = Log()

prompt = "Hello World!"

enginered_prompt = builder.base64_encode(prompt)

output = model.query(prompt)
toxicity = metrics_generator.toxicity_score(output)

#add get toxicity flag from user
dataset.add_attempt(enginered_prompt,output,toxicity,0)
print(output)