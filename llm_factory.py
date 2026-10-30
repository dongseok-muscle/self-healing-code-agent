from langchain_ollama import ChatOllama


MODEL_NAME = "qwen2.5:3b"


def get_llm():
    """
    Initialize and return the local Ollama language model.
    """

    llm = ChatOllama(
        model=MODEL_NAME,
        temperature=0
    )

    return llm