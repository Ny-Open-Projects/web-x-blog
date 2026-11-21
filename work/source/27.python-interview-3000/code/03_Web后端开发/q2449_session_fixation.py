"""会话固定防护: 登录成功即轮换会话标识(纯标准库)。"""
import secrets


class SessionStore:
    def __init__(self):
        self.sessions = {}

    def create(self):
        sid = "sid-" + secrets.token_hex(8)
        self.sessions[sid] = {"user": None, "role": "guest"}
        return sid

    def get(self, sid):
        return self.sessions.get(sid)

    def rotate(self, old_sid):
        """登录成功后的固定三步: 造新标识 -> 搬运身份 -> 杀旧标识。"""
        data = self.sessions.get(old_sid)
        if data is None:
            return None
        new_sid = "sid-" + secrets.token_hex(8)
        self.sessions[new_sid] = dict(data)
        del self.sessions[old_sid]
        return new_sid

    def login(self, sid, user, role):
        row = self.sessions.get(sid)
        if row is None:
            return None
        row["user"], row["role"] = user, role
        return self.rotate(sid)


store = SessionStore()

# 攻击者先取得一个未认证会话, 设法让受害者带着这个 sid 去登录
attacker_sid = store.create()
print("攻击者固定 sid:", attacker_sid)

# 受害者在被固定的会话上完成登录, 服务端必须轮换
new_sid = store.login(attacker_sid, "victim", "member")
assert new_sid and new_sid != attacker_sid
print("登录后轮换 sid:", new_sid)

victim_row = store.get(new_sid)
assert victim_row == {"user": "victim", "role": "member"}
print("新会话内容:", victim_row)

# 旧 sid 已失效且不含任何身份, 攻击者拿它无法冒充
assert store.get(attacker_sid) is None
print("旧 sid 状态:", store.get(attacker_sid), "攻击者无法复用")

# 反例演示: 不轮换的登录会把身份种进攻击者已知的 sid
class BadStore(SessionStore):
    def login(self, sid, user, role):
        row = self.sessions.get(sid)
        if row is None:
            return None
        row["user"], row["role"] = user, role
        return sid                                # 错误: 返回原 sid

bad = BadStore()
fixed = bad.create()
kept = bad.login(fixed, "victim2", "admin")
assert kept == fixed
print("反例: 未轮换时攻击者用 {} 即可冒充 admin".format(kept))
print("要点: 防会话固定的口诀是 造新 搬运 杀旧, 任何权限提升的时机都必须换 sid, "
      "Cookie 层面同时重发 Set-Cookie 覆盖旧值")
