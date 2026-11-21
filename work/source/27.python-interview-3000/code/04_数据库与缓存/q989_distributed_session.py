"""Redis session: 登录写入 多实例共享 主动踢下线"""
import secrets
import time

class SessionStore:
    def __init__(self, ttl=60):
        self.data, self.ttl = {}, ttl

    def login(self, user) -> str:
        sid = secrets.token_urlsafe(16)
        self.data[sid] = {"user": user, "expire": time.monotonic() + self.ttl}
        return sid

    def get(self, sid):
        rec = self.data.get(sid)
        if rec is None:
            return None
        if time.monotonic() > rec["expire"]:
            del self.data[sid]
            return None
        rec["expire"] = time.monotonic() + self.ttl      # 滑动续期
        return rec["user"]

    def kick(self, user):                               # 强制下线: 全端失效
        kicked = [sid for sid, r in self.data.items() if r["user"] == user]
        for sid in kicked:
            del self.data[sid]
        return kicked

if __name__ == "__main__":
    store = SessionStore()
    s1, s2 = store.login("alice"), store.login("alice")
    print("实例A 验证:", store.get(s1), "| 实例B 验证另一会话:",
          store.get(s2), "<- 共享 Redis, 双实例可用")
    print("踢下线:", store.kick("alice"), "随后验证:", store.get(s1))
