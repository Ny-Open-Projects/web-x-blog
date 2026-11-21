"""SAGA 编排式: 步骤失败逆序补偿"""
import sqlite3

class SagaOrchestrator:
    def __init__(self):
        self.executed = []

    def run(self, steps):
        for do, undo, name in steps:
            try:
                do()
                self.executed.append((name, undo))
                print(f"  步骤 {name} 成功")
            except Exception as e:
                print(f"  步骤 {name} 失败: {e} -> 开始逆序补偿")
                for done_name, undo in reversed(self.executed):
                    undo()
                    print(f"  补偿 {done_name}")
                return False
        return True

if __name__ == "__main__":
    db = {"order": None, "stock": 10, "coupon": "unused", "point": 0}
    log = []

    steps = [
        (lambda: (db.__setitem__("order", "O1"), log.append("创建订单")),
         lambda: db.__setitem__("order", None), "创建订单"),
        (lambda: db.__setitem__("stock", db["stock"] - 1),
         lambda: db.__setitem__("stock", db["stock"] + 1), "扣库存"),
        (lambda: (_ for _ in ()).throw(RuntimeError("积分服务不可用")),
         lambda: None, "加积分"),
    ]
    ok = SagaOrchestrator().run(steps)
    print("事务结果:", "完成" if ok else "已补偿回滚",
          "库存:", db["stock"], "订单:", db["order"])
