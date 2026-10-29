from llm_factory import get_llm


llm = get_llm()

response = llm.invoke(
    "Write a Python function that adds two numbers."
)

print(response.content)