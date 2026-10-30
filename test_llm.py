from llm_factory import get_llm


def main():

    llm = get_llm()

    response = llm.invoke(
        "Write a Python function that adds two numbers."
    )

    print("\nAI Response:\n")
    print(response.content)


if __name__ == "__main__":
    main()