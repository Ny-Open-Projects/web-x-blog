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
