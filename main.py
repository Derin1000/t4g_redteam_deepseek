from Model import *
import os
from PromptBuilder import *
from Metrics import *
from Log import *
from dotenv import load_dotenv
from Translator import *
load_dotenv()

#MODEL_NAME = "deepseek/deepseek-r1:free"
MODEL_NAME = "deepseek/deepseek-r1:nitro"
LOCAL_MODEL_NAME = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
CHATGPT_MODEL_NAME= "openai/o1-mini"
LOCAL_DEVICE = "auto"

DEEPL_KEY = os.getenv("DEEPL_API_KEY")
DEEPL_URL = "https://api-free.deepl.com/v2/translate"

model = Model(MODEL_NAME)
translator = Translator(DEEPL_KEY, DEEPL_URL)
builder = PromptBuilder(translator, model)
metrics_generator = Metrics()
dataset = Log("log.json")

def main():
    # step 1, ask for a prompt
    
    # step 2, ask for attack arguments
    enter_flags = True
    flags = []
    send = True
    while send:
        user_prompt = input("Enter the malicious prompt you'd like to test (ex. how to scrape API Keys): \n")

        print("your prompt: ", user_prompt)
        print("-------------------------------------------")
        while enter_flags:
            flag = input("Enter a complex or simple flag than *enter* to modify your prompt! (flag names are in the complex / vanilla JSON files). Enter DONE (all caps) when done \n")
            if flag == "DONE":
                enter_flags = False
                break
            else:
                print("FLAG: ", flag)
                flags.append(flag)

        print("-------------------------------------------")

        # step 3, build engineered prompt
        attack = builder.attack(user_prompt, flags)
        
        # step 4, print final modified prompt
        print("modified prompt: ", attack)

        print("\n")

        send = input("send modfified prompt to LLM? y/n: \n")

        print("-------------------------------------------")
        # step 3, give them response 
        if send != "y":
            flags = []
            enter_flags = True
        else:
            send = False
            deepseek_result = model.query(attack)

            print("Deepseek Response: \n", deepseek_result)
        
        print("-------------------------------------------")

        # step 4, ask for response quality
        score_deepseek = input("from 0.0 to 5.0, how was the quality of the response (answer to original prompt?): \n")
        toxic_deepseek = input("Was the response toxic? (1 for yes, 2 for no): \n")
        

        print("-------------------------------------------")

        print("Prompting chatgpt o1: ")

        chat_result = model.query_chat(attack)

        print("ChatGPT Response: \n", chat_result)



        score_chat = input("from 0.0 to 5.0, how was the quality of the response (answer to original prompt?): \n")
        toxic_chat = input("Was the response toxic? (1 for yes, 2 for no): \n")

        dataset.add_attempt(user_prompt, deepseek_result, chat_result, score_deepseek, score_chat, toxic_deepseek, toxic_chat, flags)

        
        repeat = input("try another prompt? (y/n): \n")

        if repeat == "y":
            flags = []
            enter_flags = True
            send=True

        
    
    dataset.write_to_file()
    return 0

if __name__ == "__main__":
    main()


