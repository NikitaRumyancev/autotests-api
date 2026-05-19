from jsonschema import validate


schema = {
    "type": "object",
    "properties":{
        "name": {"type": "string"},
        "age": {"type": "number"},
        "time_to_work": {"type": "number"}
    },
    "required": ["name", "age"]
}

data = {
    "name": "Alice",
    "age": 21,
    "time_to_work": 22
}

validate(instance=data, schema=schema)