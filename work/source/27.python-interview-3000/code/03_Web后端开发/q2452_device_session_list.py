"""登录设备的会话列表与远程下线(纯标准库)。"""
import time


class DeviceRegistry:
    """每个用户一份会话清单: 设备 IP 最近活跃, 支持单个与批量下线。"""

    def __init__(self):
        self.sessions = {}                       # sid -> 元数据

    def open(self, user, device, ip, now):
        sid = "{}|{}|{}".format(user, device, now)
        self.sessions[sid] = {"user": user, "device": device,
                              "ip": ip, "last_seen": now}
        return sid

    def touch(self, sid, now):
        row = self.sessions.get(sid)
        if row:
            row["last_seen"] = now

    def revoke(self, sid):
        return self.sessions.pop(sid, None) is not None

    def revoke_others(self, user, keep_sid):
        """远程下线其他设备: 返回被下线的设备名列表。"""
        removed = []
        for sid, row in list(self.sessions.items()):
            if row["user"] == user and sid != keep_sid:
                del self.sessions[sid]
                removed.append(row["device"])
        return removed

    def listing(self, user):
        rows = [dict(r, sid=sid) for sid, r in self.sessions.items()
                if r["user"] == user]
        return sorted(rows, key=lambda r: -r["last_seen"])


reg = DeviceRegistry()
T = 1700000000.0
s_phone = reg.open("alice", "iPhone-15", "1.2.3.4", T)
s_web = reg.open("alice", "Chrome-Mac", "5.6.7.8", T + 3600)
s_pad = reg.open("alice", "iPad", "9.9.9.9", T + 7200)
reg.open("bob", "Android", "1.1.1.1", T + 10)

reg.touch(s_phone, T + 8000)                     # 手机刚刚还在活跃
rows = reg.listing("alice")
print("alice 的设备列表 按最近活跃排序:")
for r in rows:
    print("  {:10s} ip={} last_seen=+{:.0f}s".format(r["device"], r["ip"],
                                                     r["last_seen"] - T))
assert [r["device"] for r in rows] == ["iPhone-15", "iPad", "Chrome-Mac"]

removed = reg.revoke_others("alice", keep_sid=s_web)
print("从 Chrome-Mac 点下线其他设备, 移除:", removed)
assert removed == ["iPhone-15", "iPad"]
rows_after = reg.listing("alice")
assert [r["device"] for r in rows_after] == ["Chrome-Mac"]
assert reg.revoke(s_web) is True and reg.revoke(s_web) is False
print("再次下线同一会话 -> False, 幂等安全")
assert len(reg.listing("bob")) == 1, "bob 的会话不受影响"
print("要点: 会话列表的核心字段 设备 IP 最近活跃, 下线分 单个 revoke 与 其他全下线, "
      "改密与可疑登录后应触发 revoke_others")
