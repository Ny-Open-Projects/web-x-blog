---
title: [Q991] SAGA: 长事务的补偿链
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q991 · SAGA: 长事务的补偿链

> 难度:★★★★ | 标签:分布式事务, SAGA

**问**:SAGA 模式怎么工作?与 TCC 的本质区别?补偿失败怎么办?

**答**:SAGA 把长事务拆成 T1..Tn 本地事务序列,每个 Ti 配补偿 Ci(反向),正向全部成功则完成;某步失败则逆序执行 Cn-1..C1 已完成步骤的补偿。与 TCC 区别:TCC 是"预留-确认"两阶段、中间态资源被冻结,强一致语义;SAGA 每步都是真实提交、靠逆向补偿回滚,中途对外可见中间状态,最终一致。编排两种形态:编排式(orchestration,中心状态机驱动,清晰可控)与协同式(choreography,事件链各自触发,松耦合难追踪)。补偿失败要有重试与人工兜底——补偿本身也可能失败,所以补偿操作要设计成"必然可重试成功"(幂等、不依赖不可用资源)。适合跨系统长流程(订票+酒店+支付),不适合对中间态零容忍的资金原子性。

```python
# file: code/04_数据库与缓存/q991_saga.py
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
```

**追问**:
- 补偿的顺序必须是严格逆序吗?——通常逆序(后创建的先撤销),但无依赖关系的补偿可并行,编排器按依赖图调度更高效。
- SAGA 中途对外可见的中间态怎么处理?——业务接口返回"处理中",查询走状态机;必要时用"软状态+对账"把最终态收敛(Q993/Q994)。

---
