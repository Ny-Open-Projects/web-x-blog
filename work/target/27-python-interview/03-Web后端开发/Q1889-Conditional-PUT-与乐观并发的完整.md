---
title: [Q1889] Conditional PUT 与乐观并发的完整协议
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1889 · Conditional PUT 与乐观并发的完整协议

> 难度:★★★☆ | 标签:HTTP, 并发控制

**问**:If-Match 除了防覆盖,完整的条件写协议还包括什么?

**答**:完整协议覆盖建、改两条路径。建档用 If-None-Match: * 表达"仅当资源不存在时执行",重复建档返回 412,防止并发 PUT 覆盖已有数据;更新用 If-Match 携带上次读到的 ETag,版本不一致返回 412 并回传当前 ETag,客户端重读合并后重试,这就是 HTTP 层的 CAS。服务端可以对关键资源强制前置条件,裸 PUT 返回 428 Precondition Required,把"忘记带版本"从静默覆盖变成显式错误。PUT 成功后响应必须回显新 ETag,让客户端拿到下一轮版本号;ETag 用内容哈希生成时天然随体变化。If-Match: * 是另一语义(仅当存在才改),与 If-None-Match: * 正好互补,组合起来能表达完整的状态机约束。

```python
# file: code/03_Web后端开发/q1889_conditional_put.py
"""条件写协议: If-Match 更新与 If-None-Match 建档的乐观并发(纯标准库)。"""
import hashlib


class Store:
    """带 ETag 的键值存储; ETag 由内容哈希生成, 写入时即变更。"""

    def __init__(self):
        self.items = {}

    @staticmethod
    def etag_of(body):
        return '"{}"'.format(hashlib.sha256(body.encode("utf-8")).hexdigest()[:16])

    def put(self, key, body, if_match=None, if_none_match=None,
            require_precondition=False):
        """返回 (status, headers); 实现条件写的完整协议。"""
        exists = key in self.items
        current = self.items.get(key)

        # 1) 建档保护: If-None-Match: * 表示"仅当资源不存在时执行"
        if if_none_match == "*":
            if exists:
                return 412, {"ETag": current[0]}
        # 2) 更新保护: If-Match 表示"仅当版本仍是我看到的那个"
        elif if_match is not None:
            if not exists:
                return 404, {}
            if if_match != "*" and if_match != current[0]:
                return 412, {"ETag": current[0]}
        # 3) 服务端策略: 关键资源强制要求带前置条件, 裸 PUT 返回 428
        elif require_precondition:
            return 428, {}

        etag = self.etag_of(body)
        self.items[key] = (etag, body)
        status = 201 if not exists else 204
        return status, {"ETag": etag}


store = Store()
# 建档: 带 If-None-Match: *, 成功 201
s, h = store.put("doc/1", "v1", if_none_match="*")
print("建档 If-None-Match: * ->", s, h["ETag"])
# 重复建档: 412 防止覆盖
s, h = store.put("doc/1", "v2", if_none_match="*")
print("重复建档 ->", s, "当前版本", h["ETag"])
# 裸更新被策略拦截: 428 Precondition Required
s, _ = store.put("doc/1", "v3", require_precondition=True)
print("裸更新 ->", s)
# 带旧版本更新: 412 并回传当前版本, 客户端重读后重试
s, h = store.put("doc/1", "v4", if_match='"stale-etag"')
print("过期 If-Match ->", s, "服务端当前版本", h["ETag"])
# 带正确版本更新: 204 并回传新 ETag
s, h = store.put("doc/1", "v5", if_match=h["ETag"])
print("正确 If-Match ->", s, "新版本", h["ETag"])
assert s == 204
print("要点: PUT 回显 ETag 让客户端拿最新版本, 412 即 CAS 失败, 428 是服务端强制策略")
```

**追问**:
- 412 与 409 怎么选?——412 是前置条件失败版本冲突,重试可能成功;409 是状态机语义冲突,必须人工介入。
- If-Match 的 ETag 该存哪?——客户端随读随存,服务端不维护版本表,ETag 本身就是版本的载体。
