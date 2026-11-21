"""登录限速: 按 IP 与按账号双维度失败窗口(纯标准库)。"""
from collections import deque

WINDOW, IP_LIMIT, ACCT_LIMIT = 900.0, 5, 5      # 15 分钟窗口


class FailWindow:
    """只记录失败: check 不消费, record 才入窗, 成功登录不清空其他键。"""

    def __init__(self):
        self.hits = {}

    def _prune(self, key, now):
        dq = self.hits.setdefault(key, deque())
        while dq and now - dq[0] >= WINDOW:
            dq.popleft()
        return dq

    def limited(self, key, now):
        limit = IP_LIMIT if key.startswith("ip:") else ACCT_LIMIT
        return len(self._prune(key, now)) >= limit

    def record(self, key, now):
        self._prune(key, now).append(now)


fails = FailWindow()


def login(ip, account, password, now):
    ip_key, acct_key = "ip:" + ip, "acct:" + account
    if fails.limited(ip_key, now) or fails.limited(acct_key, now):
        return 429, "尝试过于频繁, 请稍后再试"     # 统一话术, 不透露哪个维度触发
    if password != "right":
        fails.record(ip_key, now)
        fails.record(acct_key, now)
        return 401, "用户名或密码错误"
    return 200, "登录成功"


for i in range(6):
    print(f"alice 第{i + 1}次:", login("1.2.3.4", "alice", "wrong", i))
print("第7次 密码正确也被锁:", login("1.2.3.4", "alice", "right", 6))
print("同 IP 换账号 bob:", login("1.2.3.4", "bob", "right", 7))
print("换 IP 登录 bob:", login("5.6.7.8", "bob", "right", 8))
print("要点: 账号维度宽松防爆破单账号, IP 维度严格防撞库, 话术一致防枚举")
