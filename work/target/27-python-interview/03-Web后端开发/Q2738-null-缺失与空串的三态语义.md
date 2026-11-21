---
title: [Q2738] null、缺失与空串的三态语义
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2738 · null、缺失与空串的三态语义

> 难度:★★☆☆ | 标签:PATCH, 语义, 接口设计

**问**:PATCH 更新时,客户端没传某字段、传了 null、传了空串,三种情况语义怎么定?

**答**:三态规则必须显式:键缺失表示不动该字段(客户端不知道或不想改);null 表示显式清空,可空字段置 None,必填字段进错误列表;空串表示写入空值,与 null 是两回事。实现要点:用哨兵对象区分"没出现"与"出现了但值是 None",判断依据是原始请求体的键集合,JSON 反序列化后缺失与 null 天然可分,别用 dict.get 的默认值糊在一起。必填字段的 null 拒绝但要返回明确错误;空体 PATCH 等价于无操作,不是错误。这套语义与 JSON Merge Patch 的 RFC 定义一致,写进接口文档后,前端"清空手机号该传什么"就再也不用猜了。

```python
# file: code/03_Web后端开发/q2738_tri_state.py
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
```

**追问**:
- PUT 也有三态吗?——没有,PUT 是整资源替换,缺失即删除,这正是 PUT 与 PATCH 的语义分界。
- 怎么防止客户端把 null 当成没传?——契约文档加示例,校验器对必填字段的 null 返回专门错误码,测试用例覆盖三态各一条。
