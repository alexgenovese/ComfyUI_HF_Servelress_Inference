"""
@author: Alex Genovese
@title: Huggingface Api Serverless
@nickname: alexgenovese
@description: Huggingface Api Serverless request
"""

from .nodes.HF_LLM_Serverless import HF_QuestionAnswer
from .nodes.Joy_Caption import JoyPipeline, Joy_caption, Joy_caption_load

NODE_CLASS_MAPPINGS = { 
    "HF_QuestionAnswer": HF_QuestionAnswer,
    "Joy_caption":Joy_caption,
    "Joy_caption_load":Joy_caption_load
}
