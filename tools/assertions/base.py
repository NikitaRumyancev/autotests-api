from typing import Any


def assert_status_code(actual: int, expected: int):
    assert actual == expected, (
        "Incorrect status code. "
        f"Expected status code: {expected}. "
        f"Actual status code: {actual}. "
    )

def assert_equals(actual: Any, expected: Any, name: str):
    assert actual == expected, (
        f"Incorrect value {name}. "
        f"Expected value: {expected}. "
        f"Actual value: {actual}. "
    )