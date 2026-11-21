"""校验错误收敛为稳定 details 结构,并过滤敏感输入(纯标准库)。"""

SENSITIVE = {"password", "token", "id_card", "bank_no"}


def validation_error(raw_errors):
    details = []
    for e in raw_errors:
        field = ".".join(str(p) for p in e["loc"])
        item = {"field": field, "reason": e["msg"]}
        if field.split(".")[-1] not in SENSITIVE:
            item["input"] = e.get("input")     # 非敏感字段才回显原值
        details.append(item)
    return {"error": "VALIDATION_FAILED", "message": "请求参数校验失败", "details": details}


raw = [
    {"loc": ("body", "email"), "msg": "不是合法邮箱", "input": "a#example.com"},
    {"loc": ("body", "password"), "msg": "至少 8 位", "input": "secret123"},
    {"loc": ("body", "address", "city"), "msg": "不能为空", "input": None},
]
import json
print(json.dumps(validation_error(raw), ensure_ascii=False, indent=1))
