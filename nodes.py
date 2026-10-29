from state import AgentState
from schemas import CodeGenerationResult
from prompts import CODE_REPAIR_PROMPT


def generator_node(state: AgentState, llm) -> dict:
    """
    Generate initial code or repair the previous implementation.
    """

    messages = CODE_REPAIR_PROMPT.invoke(
        {
            "requirements": state["requirements"],
            "code": state["code"],
            "error_logs": state["error_logs"],
            "iteration_count": state["iteration_count"] + 1,
        }
    )

    structured_llm = llm.with_structured_output(
        CodeGenerationResult
    )

    response = structured_llm.invoke(messages)

    return {
        "code": response.code,
    }