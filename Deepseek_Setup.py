model_name = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class model_initialization:
    def __init__ (self, model_name):
        self.model_name = model_name
    
    def create_model(self, device) -> tuple:
        cached_dir = None
        dtype = torch.bfloat16
        tokenizer = AutoTokenizer.from_pretrained(model_name, cached_dir=cached_dir)
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=dtype,
            device_map=device,
            cache_dir=cached_dir
        )
        return model, tokenizer
    
    def initialize_token_ids(self, model_name):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model, tokenizer = self.create_model(device=device)
        if "Qwen" in model_name:
            token_ids = {
                "BOS" : 151646,
                "USER" : 151644,
                "ASSISTANT" : 151645,
                "NEWLINE" : 198,
                "THINK_START" : 151648,
                "THINK_END" : 151649,
                "EOS" : 151643
            }
        else:
            raise ValueError(f"Unknown tokens for model {model_name}")
        return model, tokenizer, token_ids
    
    def encode_message(self, tokenizer, token_ids, user_message: str, thinking_message: str = " "):
        user_tokens = tokenizer.encode(user_message, add_special_tokens=False)
        thinking_tokens = tokenizer.encode(thinking_message, add_special_tokens=False)
        return[[token_ids['BOS']] + user_tokens + [token_ids['NEWLINE']] + [token_ids["THINK_START"]] + thinking_tokens]
    
    def get_result(self, encoded_message, model, tokenizer):
        input_ids = torch.tensor(encoded_message).to(model.device)
        attention_mask = torch.ones_like(input_ids).to(model.device)
        with torch.no_grad():
            outputs = model.generate(
                input_ids,
                attention_mask=attention_mask,
                max_length=1000,
                do_sample=False,
                temperature=None,
                top_p=None,
                pad_token_id=tokenizer.pad_token_id,
                eos_token_id=tokenizer.eos_token_id
            )
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=False)
        return generated_text


    

    

    


    

        
    
