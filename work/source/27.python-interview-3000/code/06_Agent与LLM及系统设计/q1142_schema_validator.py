"""JSON Schema 校验桩:支持 type/required/enum/minimum,供结构化输出管线判据使用。"""


def validate(obj, schema, path="$"):
    errors = []
    t = schema.get("type")
    type_ok = {
        "object": lambda x: isinstance(x, dict),
        "string": lambda x: isinstance(x, str),
        "integer": lambda x: isinstance(x, int) and not isinstance(x, bool),
        "number": lambda x: isinstance(x, (int, float)) and not isinstance(x, bool),
    }.get(t, lambda x: True)(obj)
    if not type_ok:
        return [f"{path}: 期望 {t} 实际 {type(obj).__name__}"]
    if t == "object":
        for k in schema.get("required", []):
            if k not in obj:
                errors.append(f"{path}.{k}: 必填缺失")
        for k, sub in schema.get("properties", {}).items():
            if k in obj:
                errors += validate(obj[k], sub, f"{path}.{k}")
    if "enum" in schema and obj not in schema["enum"]:
        errors.append(f"{path}: {obj!r} 不在枚举 {schema['enum']}")
    if "minimum" in schema and isinstance(obj, (int, float)) and obj < schema["minimum"]:
        errors.append(f"{path}: {obj} 小于下限 {schema['minimum']}")
    return errors


SCHEMA = {
    "type": "object",
    "required": ["city", "days"],
    "properties": {
        "city": {"type": "string"},
        "days": {"type": "integer", "minimum": 1},
        "grade": {"type": "string", "enum": ["low", "mid", "high"]},
    },
}


class FakeLLM:
    def __init__(self, outputs):
        self.outputs = iter(outputs)

    def generate(self, prompt):
        return next(self.outputs)


if __name__ == "__main__":
    cases = [
        ('{"city": "北京", "days": 3, "grade": "high"}', []),
        ('{"city": "北京", "days": 0}', ["$.days: 0 小于下限 1", "$.grade: 必填缺失"]),
        ('{"city": 123, "days": 2, "grade": "bad"}', []),
    ]
    import json
    for raw, _ in cases:
        errs = validate(json.loads(raw), SCHEMA)
        print(f"{raw[:34]:<36} -> {errs or '合法'}")
    assert validate({"city": "北京", "days": 3, "grade": "high"}, SCHEMA) == []
    assert len(validate({"city": 123, "days": 2, "grade": "bad"}, SCHEMA)) >= 2
    print("schema 校验桩通过")
