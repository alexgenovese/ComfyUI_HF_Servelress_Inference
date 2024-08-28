import torch
from .session import request

class HF_QuestionAnswer:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "hf_token": ("STRING", {}),
                "endpoint": ("STRING", {}),
                "question": ("STRING", {"multiline": True}),
                "context": ("STRING", {"multiline": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "inference"
    CATEGORY = "HF_Serverless/QuestionAnswer"
    TITLE = "HF Question Answer"

    def inference(self, hf_token, endpoint, question, context):
        json = {
            'inputs': {
                'question': question,
                'context': context,
            },
        }
        answer = request(hf_token, endpoint, json=json)
        return (answer, '')


NODE_CLASS_MAPPINGS = {
    "HF_QuestionAnswer": HF_QuestionAnswer
}