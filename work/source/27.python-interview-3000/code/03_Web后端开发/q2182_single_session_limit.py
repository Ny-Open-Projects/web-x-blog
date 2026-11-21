"""会话并发的单会话限制: 注册表与设备类别策略(纯标准库)。"""
import itertools


class SessionRegistry:
    POLICY = {"web": 1, "mobile": 2}                # 每类设备允许的并发会话数

    def __init__(self):
        self.active = {}                            # (user, device) -> [sid 按登录时间]
        self.counter = itertools.count(1)

    def login(self, user, device_class):
        limit = self.POLICY.get(device_class, 1)
        bucket = self.active.setdefault((user, device_class), [])
        kicked = []
        while len(bucket) >= limit:
            kicked.append(bucket.pop(0))            # 最旧者被顶下线
        sid = "s-{}".format(next(self.counter))
        bucket.append(sid)
        return sid, kicked

    def validate(self, user, device_class, sid):
        return sid in self.active.get((user, device_class), [])


reg = SessionRegistry()
s1, kicked = reg.login("u1", "web")
print("第一次登录:", s1, "顶下线:", kicked)
s2, kicked = reg.login("u1", "web")
print("第二次登录:", s2, "顶下线:", kicked)
print("旧会话校验:", reg.validate("u1", "web", s1))       # False, 已被顶
print("新会话校验:", reg.validate("u1", "web", s2))
sm, _ = reg.login("u1", "mobile")
print("移动端会话:", sm, "| 不受 web 顶替影响:", reg.validate("u1", "mobile", sm))
assert not reg.validate("u1", "web", s1) and reg.validate("u1", "web", s2)
print("要点: 限制单位是设备类别; 被顶会话返回 401 加明确原因, 并写审计事件供盗号检测")
