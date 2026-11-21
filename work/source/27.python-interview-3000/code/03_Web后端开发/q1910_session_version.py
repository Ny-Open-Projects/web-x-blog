"""会话失效与并发登录踢出: 版本号方案的实现(纯标准库)。"""
import itertools


class SessionStore:
    """每用户维护版本号与会话集: 验证时同时校验 sid 存在与版本一致。

    全端下线改一个版本号即生效, 不必逐个会话删除; 并发上限踢最早登录。
    """

    def __init__(self, max_concurrent=3):
        self.users = {}
        self.max_concurrent = max_concurrent
        self.ids = itertools.count(1)

    def login(self, user):
        rec = self.users.setdefault(user, {"version": 0, "sessions": {}})
        sid = str(next(self.ids))
        rec["sessions"][sid] = rec["version"]
        if len(rec["sessions"]) > self.max_concurrent:      # 踢出最早登录
            oldest = min(rec["sessions"], key=lambda k: int(k))
            rec["sessions"].pop(oldest)
            return sid, "evicted-" + oldest
        return sid, "ok"

    def validate(self, user, sid):
        rec = self.users.get(user)
        if rec is None or sid not in rec["sessions"]:
            return False
        return rec["sessions"][sid] == rec["version"]       # 版本不匹配视为已失效

    def logout_all(self, user):
        self.users[user]["version"] += 1                     # 一次写操作全局生效
        self.users[user]["sessions"] = {}


store = SessionStore(max_concurrent=3)
s1, _ = store.login("alice")
s2, ev = store.login("alice")
s3, _ = store.login("alice")
s4, evicted = store.login("alice")
print("第 4 次登录踢出最早会话:", evicted)
assert evicted.startswith("evicted-")
print("存活会话验证:", store.validate("alice", s2), store.validate("alice", s1))
assert store.validate("alice", s2) and not store.validate("alice", s1)

store.logout_all("alice")
print("全端下线后逐一验证:", [store.validate("alice", s) for s in (s2, s3, s4)])
assert all(not store.validate("alice", s) for s in (s2, s3, s4))

store.login("alice")
print("要点: 版本号把全端下线变成 O(1) 写操作, 密码改签、风控踢出、注销所有设备共用这一机制")
