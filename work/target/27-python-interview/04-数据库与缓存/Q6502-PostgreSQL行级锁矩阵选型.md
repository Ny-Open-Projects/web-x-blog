---
title: [Q6502] PostgreSQL 行级锁矩阵:FOR UPDATE / SKIP LOCKED / NOWAIT
date: 2026-11-18
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6502 · PostgreSQL 行级锁矩阵:FOR UPDATE / SKIP LOCKED / NOWAIT

> 难度:★★★ | 标签:PostgreSQL, 锁, 并发

**问**：三个场景——抢单任务分发、库存扣减、秒杀瞬时冲突——都会碰到行锁。FOR UPDATE、SKIP LOCKED、NOWAIT 三者的语义边界和适用矩阵是什么？选错会发生什么线上事故？

**答**：结论：这三个后缀是三种并发策略，本质区别是"遇锁时等、跳、还是炸"。任务队列用 SKIP LOCKED（跳过别人在处理的行，worker 互不阻塞）；强一致扣减用 FOR UPDATE（必须等到锁，宁可排队不可超卖）；避免级联等待用 NOWAIT（拿不到立刻报错，由应用决定重试或降级）。选错的症状很典型：队列用了 FOR UPDATE → worker 串行化、连接堆积；扣减用了 SKIP LOCKED → 跳过即视为无库存，白白丢单；秒杀用默认等待 → 锁队列越排越长，雪崩式超时。

取舍与实战：
- SKIP LOCKED 的正确姿势是"ORDER BY + LIMIT 1 + 子查询"三件套：外层 FOR UPDATE SKIP LOCKED，`FOR UPDATE SKIP LOCKED` 不能直接套在带 ORDER BY/LIMIT 的聚合语义上时用 CTE 或子查询锁主键，再回表取数据。锁完立刻处理并 commit，锁窗口越短吞吐越高。
- NOWAIT 适合"冲突概率低但后果重"的场景：抢注用户名、防重复开票。拿锁失败抛 `55P03 lock_not_available`，应用层转成业务失败而不是重试风暴。
- 事故复盘：某队列系统 worker 把 FOR UPDATE 加在 JOIN 大查询上，锁从目标行蔓延到连接的宽范围，加上事务里有慢 HTTP 调用，锁持有 8 秒以上，其他 worker 全部等待超时。修复三板斧：先只锁主键（子查询）、事务内不做 IO、超时配 `lock_timeout` 而不是让应用干等。

```python
# 基线:PostgreSQL 12+ / SQLAlchemy 2.0;缺库时 demo 部分可直接运行
from sqlalchemy import text  # pip install sqlalchemy psycopg2-binary (缺库降级见 demo)

# ---- 三种取任务/扣库存的 SQL 形态(伪代码注释,真实执行走 engine) ----
SQL_QUEUE = """
WITH picked AS (
    SELECT id FROM job
    WHERE status = 'ready'
    ORDER BY priority DESC, id
    FOR UPDATE SKIP LOCKED          -- 跳过已被其他 worker 锁住的行,不排队
    LIMIT 1
)
UPDATE job SET status = 'running', worker = :w
WHERE id IN (SELECT id FROM picked)
RETURNING id;
"""
SQL_DECREMENT = """
UPDATE sku SET stock = stock - :n
WHERE id = :id AND stock >= :n
RETURNING stock;                     -- 单条原子扣减,条件扣不到即返回空=售罄
"""
SQL_GRAB_NOWAIT = """
SELECT id FROM invoice WHERE order_id = :oid FOR UPDATE NOWAIT   -- 拿不到立即 55P03
"""

def pick_strategy(conflict_rate: float, consistency: str) -> str:
    """选型矩阵:按冲突率与一致性要求决定策略(可运行)。"""
    if consistency == "strong":          # 强一致:不允许多扣/少扣
        return "FOR UPDATE" if conflict_rate < 0.5 else "原子 UPDATE + 条件"
    if consistency == "queue":           # 多 worker 分发
        return "FOR UPDATE SKIP LOCKED"
    return "FOR UPDATE NOWAIT"           # 低冲突高后果:拿不到就快速失败

if __name__ == "__main__":
    print(pick_strategy(0.9, "queue"))    # FOR UPDATE SKIP LOCKED
    print(pick_strategy(0.8, "strong"))   # 原子 UPDATE + 条件
```

**追问**：
- 一层追问：SKIP LOCKED 的任务如果 worker 半路崩了怎么办？——锁随连接断开释放，但 status 还停在 running。必须配租约/心跳：取出时写 `lease_until = now()+N s`，另有回收器扫 `running AND lease_until < now()` 重置为 ready，否则任务黑洞。
- 二层追问：FOR UPDATE 排队会不会造成死锁？——会，两个事务以相反顺序锁多行即死锁。PG 检测到后杀一个（40P01），应用要捕获重试；预防靠"按同一 ORDER BY 加锁"的约定。
- 三层追问：为什么扣库存不用 SELECT FOR UPDATE 而推荐条件 UPDATE？——条件 UPDATE 是单语句原子操作，锁窗口只有行级写锁的一瞬，且把"检查+扣减"合并不留 TOCTOU 窗口；FOR UPDATE 需要额外往返且事务更长。
