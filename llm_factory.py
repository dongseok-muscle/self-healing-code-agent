import os

from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace


load_dotenv()

MODEL_ID = "meta-llama/Llama-3.2-3B-Instruct"


def get_llm():
    token = os.getenv("HF_TOKEN")

    if not token:
        raise ValueError(
            "HF_TOKEN is missing. Add it to your .env file."
        )

    endpoint = HuggingFaceEndpoint(
        repo_id=MODEL_ID,
        task="text-generation",
        max_new_tokens=1024,
        do_sample=False,
        huggingfacehub_api_token=token,
    )

    return ChatHuggingFace(llm=endpoint)