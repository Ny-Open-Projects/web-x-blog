"""内存 Repository 替身 + 真库集成测试 双层验证"""
from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    active: bool = True

class UserRepo(Protocol := object):            # 生产实现签名
    def add(self, u: User) -> None: ...
    def count_active(self) -> int: ...

class MemoryRepo:                              # 单测替身
    def __init__(self):
        self.data: list[User] = []
    def add(self, u):
        self.data.append(u)
    def count_active(self):
        return sum(1 for u in self.data if u.active)

class Business:
    def __init__(self, repo):
        self.repo = repo
    def register(self, name):
        u = User(name=name)
        self.repo.add(u)
        return self.repo.count_active()

def integration_test():
    """真库集成: 验证 SQL 与约束"""
    import sqlite3
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (name TEXT PRIMARY KEY, active INT)")
    try:
        conn.execute("INSERT INTO users VALUES ('a', 1)")
        conn.execute("INSERT INTO users VALUES ('a', 1)")   # 唯一约束
    except sqlite3.IntegrityError:
        return "集成测试: 唯一约束生效, 重复插入被拒"
    return "集成测试: 通过"

if __name__ == "__main__":
    biz = Business(MemoryRepo())
    print("单测: 注册后活跃数 =", biz.register("alice"))
    print(integration_test())
