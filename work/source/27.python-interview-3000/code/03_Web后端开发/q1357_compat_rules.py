"""接口 schema 变更的兼容性检查器(纯标准库)。"""


def diff_api(old, new):
    """old/new: {request_required: [..], response_fields: {字段: 类型}}"""
    breaking, safe = [], []
    for f in old["request_required"]:
        if f not in new["request_required"]:
            safe.append(f"请求移除必填字段 {f}:放宽,兼容")
    for f in new["request_required"]:
        if f not in old["request_required"]:
            breaking.append(f"请求新增必填字段 {f}:旧客户端将 422")
    for f, t in old["response_fields"].items():
        if f not in new["response_fields"]:
            breaking.append(f"响应删除字段 {f}:旧客户端可能取空崩溃")
        elif new["response_fields"][f] != t:
            breaking.append(f"响应字段 {f} 类型 {t} 改为 {new['response_fields'][f]}")
    for f, t in new["response_fields"].items():
        if f not in old["response_fields"]:
            safe.append(f"响应新增字段 {f}:向前兼容")
    return breaking, safe


old = {"request_required": ["user_id", "amount"],
       "response_fields": {"id": "int", "name": "str", "fee": "int"}}
new = {"request_required": ["user_id", "amount", "currency"],
       "response_fields": {"id": "int", "name": "str", "amount": "int"}}
breaking, safe = diff_api(old, new)
print("破坏性变更:")
for b in breaking:
    print(" -", b)
print("安全变更:")
for s in safe:
    print(" -", s)
