from typing import Any
from jsonschema import validate, Draft202012Validator


def validate_json_schema(instance: Any, schema: dict) -> None:
    validate(
        instance=instance,
        schema=schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )