"""RFC 7807 application/problem+json 的构造与必备成员校验(纯标准库)。"""
import json


def problem(status, title, detail=None, instance=None, ptype="about:blank", **extra):
    """构造符合 RFC 7807 的问题详情体;extra 是扩展成员。"""
    body = {"type": ptype, "title": title, "status": status}
    if detail is not None:
        body["detail"] = detail
    if instance is not None:
        body["instance"] = instance
    body.update(extra)
    return body


def validate(body, http_status):
    """校验必备成员与语义一致性,返回错误列表。"""
    errors = []
    if "type" not in body:
        errors.append("缺少 type")
    elif not body["type"].startswith(("http://", "https://", "about:")):
        errors.append("type 必须是 URI")
    if "title" not in body:
        errors.append("缺少 title")
    if "status" not in body:
        errors.append("缺少 status")
    elif body["status"] != http_status:
        errors.append("status 成员应与 HTTP 状态码一致")
    return errors


body = problem(422, "参数校验失败", detail="limit 不能超过 100", instance="/v1/orders?page=3",
               ptype="https://api.example.com/problems/invalid-param", limit=100)
print(json.dumps(body, ensure_ascii=False, sort_keys=True))
print("响应头 Content-Type: application/problem+json")
print("校验结果:", validate(body, 422) or "通过")

bad = {"type": "invalid-param", "status": 500}
print("坏样本:", validate(bad, 422))
