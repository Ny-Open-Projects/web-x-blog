"""纯逻辑模拟三种读现象, 帮助面试时口头推演"""
from dataclasses import dataclass, field


@dataclass
class Database:
    committed: dict = field(default_factory=dict)   # 已提交数据
    uncommitted: dict = field(default_factory=dict)  # 未提交数据

    def write(self, key: str, value: int) -> None:
        self.uncommitted[key] = value

    def commit(self) -> None:
        self.committed.update(self.uncommitted)
        self.uncommitted.clear()

    def rollback(self) -> None:
        self.uncommitted.clear()


def dirty_read(db: Database, key: str) -> int:
    """READ UNCOMMITTED: 读到别人未提交的值"""
    return db.uncommitted.get(key, db.committed.get(key, 0))


def committed_read(db: Database, key: str) -> int:
    """READ COMMITTED: 每次读最新已提交值 -> 两次读可能不同即不可重复读"""
    return db.committed.get(key, 0)


if __name__ == "__main__":
    db = Database(committed={"x": 100})
    db.write("x", 999)                      # 事务 A 修改但未提交
    print("RU 视角读到:", dirty_read(db, "x"))      # 999 脏读
    db.rollback()                           # A 回滚
    print("回滚后 RC 第一次读:", committed_read(db, "x"))  # 100
    db.write("x", 200)
    db.commit()                             # B 提交了新值
    print("RC 第二次读:", committed_read(db, "x"))        # 200 不可重复读
