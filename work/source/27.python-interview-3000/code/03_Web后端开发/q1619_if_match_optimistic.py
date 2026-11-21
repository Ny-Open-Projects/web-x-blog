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
