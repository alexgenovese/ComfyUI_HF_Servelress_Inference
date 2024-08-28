"""Session handler"""
import os
from huggingface_hub import InferenceClient


def request(hf_token, repo_id, **kwargs):

    if hf_token == "": 
        raise Exception(f"No Huggingface Token provided - found this in ENV {os.environ['HF_AUTH_TOKEN']}")

    client = InferenceClient(
        repo_id,
        hf_token,
    )

    input_params = kwargs.get('json').get('inputs')
    
    if isinstance(input_params, dict) : 
        request=[{"content": input_params.get('context'), "role": "system"},{"content": input_params.get('question'), "role": "user"}]
    else: 
        request=[{"inputs": input_params }]


    response = client.chat_completion(
        messages=request,
        max_tokens=5000,
        stream=False,
    )

    # print(f"------- POST: {response.choices[0].message.content}")

    return response.choices[0].message.content