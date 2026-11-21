
class Legacy:
    def __init__(self):
        self.rows = {}

class Target:
    def __init__(self):
        self.rows = {}

legacy, target = Legacy(), Target()

def write_order(order_id: str, amount: int, dual: bool = True) -> str:
    legacy.rows[order_id] = amount
    if dual:
        target.rows[order_id] = amount
    return "dual-write ok"

write_order("o1", 100)
write_order("o2", 50, dual=False)     # 迁移前的旧路径数据

backfill = {k: v for k, v in legacy.rows.items() if k not in target.rows}
target.rows.update(backfill)          # 回填补齐
print("一致性校验:", legacy.rows == target.rows)
