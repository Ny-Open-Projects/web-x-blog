"""读写路由: 写后 N 秒内该用户的读走主库, 模拟读己之写会话粘性"""
import time

class Cluster:
    def __init__(self):
        self.primary = {"users": {"alice": 1}}
        self.replica = {"users": {"alice": 1}}
        self.sticky_until = {}          # user -> 走主库的截止时间

    def write(self, user, level):
        self.primary["users"][user] = level
        self.sticky_until[user] = time.monotonic() + 2.0   # 写后 2 秒粘主库

    def read(self, user):
        to_primary = time.monotonic() < self.sticky_until.get(user, 0)
        db = self.primary if to_primary else self.replica
        return db["users"][user], "主库" if to_primary else "从库"

if __name__ == "__main__":
    c = Cluster()
    c.write("alice", 99)                 # 主库已更新, 从库还在延迟中
    c.replica["users"]["alice"] = 1      # 模拟从库尚未同步
    print("写后立即读:", c.read("alice"))
    time.sleep(2.1)
    print("粘性过期后读:", c.read("alice"))
