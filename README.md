# Huggingface Api Serverless Inference 

It's a node to Enhance any Prompt running the inference of LLM model on the serverless endpoint on Hugginggface. 

Inputs:
- hf_token: String -- It's the token string 
- endpoint: String -- It's the repo id hosted on HF (Ex: meta-llama/Meta-Llama-3-8B-Instruct) 
- question: String -- Type here the question
- context: String -- LLM Instruction for the model

Output: 
- STRING: String -- A string

## Installation

### Clone and install dependencies
```
git clone https://github.com/alexgenovese/ComfyUI_HF_Servelress_Inference custom_nodes/ComfyUI_HF_Servelress_Inference
cd custom_nodes/ComfyUI_HF_Servelress_Inference
pip install -r requirements.txt
```

Go into your account and create a new TOKEN: [Hugging Face tokens](https://huggingface.co/settings/tokens)


## Limitations

> [!WARNING]
> Inference API (serverless) requires a model 10GB or below and fails for random reasons on different models.

