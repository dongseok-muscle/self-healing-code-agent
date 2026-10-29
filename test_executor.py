from executor import execute_python_code


def test_successful_execution():
    result = execute_python_code("print(2 + 3)")

    assert result["exit_code"] == 0
    assert result["is_success"] is True
    assert result["stdout"].strip() == "5"


def test_runtime_error():
    result = execute_python_code("print(10 / 0)")

    assert result["exit_code"] != 0
    assert result["is_success"] is False
    assert "ZeroDivisionError" in result["stderr"]


if __name__ == "__main__":
    test_successful_execution()
    test_runtime_error()

    print("All execution helper checks passed!")