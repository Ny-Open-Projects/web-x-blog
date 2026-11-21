---
title: [Q1355] 错误响应中 details 的结构契约
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1355 · 错误响应中 details 的结构契约

> 难度:★★ | 标签:错误码, 接口设计

**问**:校验失败要返回多个字段错误,details 结构怎么定才稳定?有什么绝对不能放进响应?

**答**:定三层:message 给人看(一句中文概括),error 给程序判断(语义名),details 是数组、每项固定 `field + reason(+ input)`,字段路径用点分字符串(`body.address.city`)。**敏感输入绝不能回显**:password、token、身份证这类字段即使客户端传了,details 里也只能有校验结论不能有原值——回显错误输入是最常见的泄露路径。details 的 key 一旦发布就不许改名,加字段可以、删字段要按弃用流程走。

```python
# file: code/03_Web后端开发/q1355_error_details.py
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
```

**追问**:
- 字段路径要不要带 body/query 前缀?——要,同名参数在不同位置含义不同,定位报错必须有位置信息。
- details 里能给内部堆栈吗?——绝对不行,堆栈只进服务端日志,对外是信息泄露。
