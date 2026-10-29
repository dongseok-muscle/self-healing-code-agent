import subprocess
import sys


def execute_python_code(code: str) -> dict:
    """
    Execute Python code and return its output and exit status.
    """

    try:
        result = subprocess.run(
            [sys.executable, "-c", code],
            capture_output=True,
            text=True,
            timeout=5
        )

        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "exit_code": result.returncode,
            "is_success": result.returncode == 0
        }

    except subprocess.TimeoutExpired:
        return {
            "stdout": "",
            "stderr": "Execution timed out after 5 seconds.",
            "exit_code": -1,
            "is_success": False
        }

    except OSError as error:
        return {
            "stdout": "",
            "stderr": f"Execution failed: {error}",
            "exit_code": -1,
            "is_success": False
        }