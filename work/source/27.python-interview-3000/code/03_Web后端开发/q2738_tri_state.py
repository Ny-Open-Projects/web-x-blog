"""null、缺失与空串的三态语义: PATCH 更新的三种意图(纯标准库)。"""

MISSING = object()  # 哨兵: 键根本没出现在请求体里


def apply_patch(resource, raw_body):
    """三态规则:

    - 键缺失   -> 不动该字段(客户端不知道或不想改);
    - 值为 null -> 显式清空, 可空字段置 None, 必填字段报错;
    - 空串     -> 写入空串, 与 null 是两回事(姓名真的叫空串的业务不多, 但传真是)。
    raw_body 用解析时保留的键序集合判断"出现过", json 反序列化天然分不出缺失与 null。
    """
    updated = dict(resource)
    errors = []
    for key in ("name", "phone", "fax"):
        value = raw_body.get(key, MISSING)
        if value is MISSING:
            continue
        if value is None:
            if key == "name":
                errors.append("name 必填, 不能清空")
                continue
            updated[key] = None
        else:
            updated[key] = value
    return updated, errors


base = {"name": "Ann", "phone": "13800000000", "fax": None}
u1, e1 = apply_patch(base, {"phone": "139"})          # 只改 phone
assert e1 == [] and u1["name"] == "Ann" and u1["phone"] == "139" and u1["fax"] is None
u2, e2 = apply_patch(base, {"fax": None, "phone": None})  # 显式清空 fax 与 phone
assert e2 == [] and u2["phone"] is None and u2["fax"] is None and u2["name"] == "Ann"
u3, e3 = apply_patch(base, {"name": "", "phone": ""})     # 空串是合法值, 不是清空
assert e3 == [] and u3["name"] == "" and u3["phone"] == ""
u4, e4 = apply_patch(base, {"name": None})                # 必填字段拒绝清空
assert e4 == ["name 必填, 不能清空"] and u4["name"] == "Ann"
u5, _ = apply_patch(base, {})                              # 空体 = 无操作
assert u5 == base
print("缺失=不改, null=清空, 空串=写空值; 必填字段的 null 进 errors 不进结果")
