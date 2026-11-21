import random


class MigrationManager:
    def __init__(self, read_percent: int = 0):
        self.old: dict[int, dict] = {}
        self.new: dict[int, dict] = {}
        self.read_percent = read_percent  # 阶段开关:读新库比例
        self.mismatch_log: list = []

    def write(self, uid: int, data: dict) -> str:
        self.old[uid] = data                       # 旧库为主
        try:
            if random.random() < 0.9:              # 模拟新库偶发失败
                self.new[uid] = data
            else:
                raise ConnectionError("new db down")
        except ConnectionError:
            self.mismatch_log.append(uid)          # 只记录,不阻断
        return "dual-write ok"

    def read(self, uid: int) -> dict:
        # 按用户分桶灰度切读,同一用户始终走同一侧,结果稳定
        use_new = uid % 100 < self.read_percent
        return self.new[uid] if use_new else self.old[uid]

    def reconcile(self) -> int:
        """对账:找出两边不一致的用户并修复新库。"""
        fixed = 0
        for uid in set(self.old) | set(self.new):
            if self.old.get(uid) != self.new.get(uid):
                self.new[uid] = self.old.get(uid)
                fixed += 1
        self.mismatch_log.clear()
        return fixed


if __name__ == "__main__":
    random.seed(1)
    m = MigrationManager(read_percent=30)
    for uid in (1, 2, 3, 4, 5, 101):   # 101 与 1 同桶(101%100==1),验证分桶读
        m.write(uid, {"name": f"u{uid}"})
    print("mismatch fixed:", m.reconcile())
    print(m.read(1), m.read(101))  # 同一桶内读侧一致
