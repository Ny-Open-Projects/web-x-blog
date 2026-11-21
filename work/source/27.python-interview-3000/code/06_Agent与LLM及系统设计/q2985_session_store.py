"""Q2985 会话存储的完整实现:追加、恢复、过期与截断。

会话存储是聊天产品的地基,三个硬要求:消息只追加不改写(历史是
审计依据);按会话 id 可完整恢复;过期由注入时钟驱动,读时惰性
清理即可,不必起后台任务。另外要有长度上限:超限从头丢弃最老的
消息但保住系统消息,防止长会话把上下文撑爆。
"""

import time


class SessionStore:
    def __init__(self, max_messages=6, ttl_seconds=3600, clock=None):
        self.max_messages = max_messages
        self.ttl = ttl_seconds
        self.now = clock or time.time
        self._data = {}            # sid -> {"msgs": [...], "updated": ts}

    def append(self, sid, role, content):
        s = self._data.setdefault(sid, {"msgs": [], "updated": self.now()})
        s["msgs"].append({"role": role, "content": content,
                          "ts": self.now()})
        s["updated"] = s["msgs"][-1]["ts"]
        self._trim(sid)
        return len(s["msgs"])

    def _trim(self, sid):
        s = self._data[sid]
        while len(s["msgs"]) > self.max_messages:
            # 系统消息永远保留,从最老的非系统消息开始丢
            if s["msgs"][0]["role"] == "system" and \
               any(m["role"] != "system" for m in s["msgs"]):
                s["msgs"].pop(1)
            else:
                s["msgs"].pop(0)

    def restore(self, sid):
        """读时惰性过期:过期返回空并清除,未过期返回全部消息。"""
        s = self._data.get(sid)
        if s is None:
            return []
        if self.now() - s["updated"] > self.ttl:
            del self._data[sid]                 # 整段会话过期即删
            return []
        return list(s["msgs"])

    def count(self):
        return len(self._data)


def main():
    store = SessionStore(max_messages=4, ttl_seconds=60, clock=lambda: 1000.0)
    store.append("s1", "system", "你是客服助手")
    store.append("s1", "user", "查订单")
    store.append("s1", "assistant", "订单号是多少")
    assert store.restore("s1")[0]["role"] == "system"     # 可恢复
    assert len(store.restore("s1")) == 3

    # 超限截断:系统消息保住,最老的用户消息被丢
    store.append("s1", "user", "o_9")
    store.append("s1", "assistant", "已退款")
    msgs = store.restore("s1")
    assert len(msgs) == 4, len(msgs)
    assert msgs[0]["role"] == "system"
    assert all(m["content"] != "查订单" for m in msgs)   # 最老消息被丢
    assert msgs[-1]["content"] == "已退款"               # 最新消息保住

    # 过期:注入时钟前进,读时清理
    t2 = [1000.0]
    store2 = SessionStore(max_messages=10, ttl_seconds=60,
                          clock=lambda: t2[0])
    store2.append("s2", "user", "hi")
    assert store2.restore("s2")                  # 未过期可恢复
    t2[0] = 1120.0                               # 模拟 120 秒后
    assert store2.restore("s2") == []            # 过期返回空
    assert store2.count() == 0                   # 且被清理

    # 新会话不存在,恢复得空列表而不是 KeyError
    assert store.restore("ghost") == []
    print("会话条数上限内:", len(store.restore("s1")))
    print("过期清理后剩余会话:", store2.count())


if __name__ == "__main__":
    main()
