"""
@author: Alex Genovese
@title: Huggingface Api Serverless
@nickname: alexgenovese
@description: Huggingface Api Serverless request
"""

from .nodes.HF_LLM_Serverless import HF_QuestionAnswer

NODE_CLASS_MAPPINGS = { 
    "HF_QuestionAnswer": HF_QuestionAnswer
}
