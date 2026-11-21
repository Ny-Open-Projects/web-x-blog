"""越权回归:端点 x 主体 x 期望 的用例矩阵自动执行(纯标准库)。"""

documents = {101: {"owner": "u1", "title": "doc-a"},
             102: {"owner": "u2", "title": "doc-b"}}


def api_get(doc_id, user):
    """模拟对象接口:归属不符与不存在同响应 404。"""
    doc = documents.get(doc_id)
    if doc is None or doc["owner"] != user:
        return 404
    return 200


def build_cases(documents, actors=("u1", "u2", "u9")):
    cases = []
    for doc_id, meta in documents.items():
        for user in actors:
            expect = 200 if meta["owner"] == user else 404
            cases.append((f"GET /docs/{doc_id} as {user}", doc_id, user, expect))
    return cases


failures = 0
for name, doc_id, user, expect in build_cases(documents):
    got = api_get(doc_id, user)
    ok = got == expect
    failures += not ok
    print(("PASS" if ok else "FAIL"), name, "expect", expect, "got", got)
print("用例总数:", len(build_cases(documents)), "失败:", failures)
assert failures == 0
