
CONTRACT = {
    "GET /users/{id}": {
        "id": "int", "name": "str", "email": "str|null",
    },
}

TYPES = {"int": int, "str": str, "str|null": (str, type(None))}

def validate_contract(actual: dict, schema: dict) -> list:
    errors = []
    for field, typ in schema.items():
        if field not in actual:
            errors.append(f"{field} 缺失")
        elif not isinstance(actual[field], TYPES[typ]):
            errors.append(f"{field} 类型应为 {typ}")
    return errors

sample = {"id": "1", "name": "alice"}
print(validate_contract(sample, CONTRACT["GET /users/{id}"]))
sample_ok = {"id": 1, "name": "alice", "email": None}
print(validate_contract(sample_ok, CONTRACT["GET /users/{id}"]))
