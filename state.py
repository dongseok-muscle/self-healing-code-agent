from typing import TypedDict


class AgentState(TypedDict):
    # User input
    requirements: str
    code: str

    # Validation configuration
    expected_output: str
    test_code: str
    validation_mode: str

    # Execution results
    stdout: str
    stderr: str
    error_logs: str
    exit_code: int

    # Workflow tracking
    generation_count: int
    execution_count: int
    max_iterations: int

    # Final status
    is_success: bool