---
title: "[Q6710] REPLICA IDENTITY 缺失导致逻辑复制变更丢失"
date: 2026-11-23
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6710 · REPLICA IDENTITY 缺失导致逻辑复制变更丢失

难度：P6 ｜ 标签：事故复盘、逻辑复制、WAL、CDC

基线：Python 3.12；PostgreSQL 10+；纯 Python 演示 UPDATE 事件的旧值构造。

**问**：把一张新表加入逻辑复制发布后，INSERT 都同步正常，但 UPDATE 在订阅端报错、DELETE 直接没生效。表结构没问题、复制槽也在推进。最可能漏了什么？

**答**：
- **结论**：漏了 `REPLICA IDENTITY`。逻辑复制的 UPDATE/DELETE 事件必须携带**旧行值**，订阅端才能定位要改/删的那一行。默认 `REPLICA IDENTITY DEFAULT` 用主键定位；表没有主键或合适唯一索引时，UPDATE/DELETE 无法构造旧值，订阅端报错或跳过。解决：给表加主键（首选），或 `ALTER TABLE t REPLICA IDENTITY USING INDEX ...`，兜底是 `REPLICA IDENTITY FULL`（把整行旧值写进 WAL）。
- **取舍**：DEFAULT（主键）WAL 最省、性能最好；USING INDEX 折中；FULL 不需要任何键但**每条 UPDATE/DELETE 都要记录完整旧行**，WAL 体积和 CPU 开销显著上升，高频更新表上代价很大。所以 FULL 是兜底不是默认。
- **实战**：把"发布表必须有主键或显式 replica identity"写进建表规范和上线检查单；上线前用 `UPDATE`/`DELETE` 做端到端验证，别只看 INSERT；监控订阅端 apply worker 的错误日志；对确需 FULL 的表评估 WAL 增长并扩容磁盘。

```python
def build_update_event(
    old: dict | None, new: dict, replica_identity: str
) -> dict | None:
    """逻辑复制的 UPDATE 需要旧值定位；无键 + default 时无法构造。"""
    if replica_identity == "default" and old is None:
        return None  # 没有主键等定位信息，变更事件丢失
    return {"op": "U", "old": old, "new": new}


if __name__ == "__main__":
    new = {"id": 1, "status": "paid"}
    old = {"id": 1, "status": "init"}
    print("有主键(default):", build_update_event(old, new, "default"))
    print("无主键(default):", build_update_event(None, new, "default"))
    print("FULL 兜底:", build_update_event(old, new, "full"))
```

**追问一**：为什么 INSERT 正常，只有 UPDATE/DELETE 出问题？
→ 解析：INSERT 只需新值即可插入，不依赖旧行定位；UPDATE/DELETE 必须知道改/删哪一行，需要旧值（主键或整行），缺 REPLICA IDENTITY 时就构造不出事件。

**追问二**：`REPLICA IDENTITY FULL` 的代价具体体现在哪？
→ 解析：它把整行旧值写进 WAL，WAL 体积和解码 CPU 上升，复制槽堆积风险变大，网络和订阅端落库压力也增加。高频更新表上要评估磁盘与带宽，能用主键就别用 FULL。
