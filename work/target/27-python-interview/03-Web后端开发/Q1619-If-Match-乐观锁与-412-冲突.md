---
title: [Q1619] If-Match 乐观锁与 412 冲突
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1619 · If-Match 乐观锁与 412 冲突

> 难度:★★★☆ | 标签:并发控制, HTTP

**问**:不用数据库行锁,纯 HTTP 层怎么防丢失更新?If-Match 的完整判定流程是什么?

**答**:乐观锁三步:GET 时响应带当前强 ETag;PUT 时客户端回带 `If-Match`;服务端比对当前 ETag,不一致返回 412 Precondition Failed,一致才应用修改并更新 ETag。判定顺序有讲究:没有 If-Match 返回 428 要求先读后写;带弱标签返回 400,因为 If-Match 按规范只接受强校验器;最后才比对值是否等于当前 ETag。两个人同时编辑,A 的旧 ETag 在 B 写入后必然失配,这就是冲突信号——客户端重 GET、合并、再提交,而不是盲目覆盖。要求资源必须存在或不存在的场景还有 `If-None-Match: *`。

```python
# file: code/03_Web后端开发/q1619_if_match_optimistic.py
"""If-Match 乐观锁: 并发 PUT 的冲突判定(纯标准库)。"""
import hashlib


def etag_of(doc):
    return '"' + hashlib.sha256(doc.encode()).hexdigest()[:16] + '"'


class Resource:
    def __init__(self, doc):
        self.doc = doc

    def get(self):
        return {"doc": self.doc, "etag": etag_of(self.doc)}

    def put(self, new_doc, if_match):
        if not if_match:
            return 428, "需要 If-Match 先读后写"          # 428 Precondition Required
        if if_match.startswith("W/"):
            return 400, "If-Match 只接受强校验器"
        if if_match != etag_of(self.doc):
            return 412, "资源已被他人修改, 请重新 GET"
        self.doc = new_doc
        return 200, {"doc": self.doc, "etag": etag_of(self.doc)}


res = Resource("v1 草稿")
first = res.get()
print("A 拿到:", first)

status, info = res.put("B 的修改", first["etag"])          # B 抢先写入
print("B 写入:", status, info)

status, info = res.put("A 的修改", first["etag"])          # A 用旧 ETag 提交
print("A 提交:", status, info)

second = res.get()
status, info = res.put("A 的修改", second["etag"])         # 重读后再提交
print("A 重读后提交:", status, info)

status, info = res.put("弱标签也拒", 'W/%s' % second["etag"])
print("弱标签 If-Match:", status, info)
```

**追问**:
- 412 之后客户端该怎么办?——重新 GET 拿新 ETag,提示用户合并差异后再提交,不能自动覆盖。
- ETag 生成有什么要求?——同一状态必须稳定一致、状态变化必须变化,所以优先内容哈希而不是随机数。
