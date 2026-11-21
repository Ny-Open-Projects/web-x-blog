"""会话持久化:版本化快照 schema + 乐观并发 + TTL 清理。"""
import json, time


class SessionStore:
    SCHEMA_VERSION = 2

    def __init__(self, ttl_sec=3600):
        self.db, self.ttl = {}, ttl_sec

    def save(self, sid, session):
        session["schema_v"] = self.SCHEMA_VERSION
        session["updated_at"] = time.time()
        old = self.db.get(sid)
        if old and old.get("version", 0) != session.get("base_version", old["version"]):
            raise ValueError("版本冲突,请重读会话后再写")
        session["version"] = session.get("base_version", old["version"] if old else 0) + 1
        session.pop("base_version", None)
        self.db[sid] = session
        return session["version"]

    def load(self, sid):
        s = self.db.get(sid)
        if not s:
            return None
        if time.time() - s["updated_at"] > self.ttl:
            del self.db[sid]                       # 僵尸会话回收
            return None
        if s["schema_v"] < self.SCHEMA_VERSION:
            s.setdefault("slots", {})              # 简单迁移示例
        return s


if __name__ == "__main__":
    store = SessionStore()
    sid = "s-1"
    v1 = store.save(sid, {"messages": [("user", "你好")], "slots": {}, "base_version": 0})
    print("首写版本:", v1)
    cur = store.load(sid)
    cur["messages"].append(("assistant", "你好,要办什么业务"))
    cur["slots"]["city"] = "北京"
    v2 = store.save(sid, {**cur, "base_version": v1})
    print("二次写版本:", v2, "槽位:", cur["slots"])

    stale = {**store.load(sid), "base_version": v1}   # 用旧版本并发写
    try:
        store.save(sid, stale)
    except ValueError as e:
        print("并发冲突被拦截:", e)

    store.db[sid]["updated_at"] = time.time() - 7200
    assert store.load(sid) is None
    print("TTL 回收生效,schema 版本:", SessionStore.SCHEMA_VERSION)
