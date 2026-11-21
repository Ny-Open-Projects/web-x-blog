---
title: [Q6576] 分区数上限与 planner 变慢的容量账
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6576 · 分区数上限与 planner 变慢的容量账

难度：P7 ｜ 标签：PostgreSQL / 分区表 / 容量规划

**问**：按天分区保留 3 年，一张表 1000+ 分区，应用反馈简单查询有时要几百毫秒才返回。分区数量到底有多少能承受？容量账怎么算？

**答**：
- **结论**：分区是双刃剑——裁剪（partition pruning）省扫描，但每个分区都是独立规划单元：planner 要为每个分区估算路径、锁每个分区、`PREPARE` 语句的 generic plan 与继承层级叠加后，编译时间随分区数线性甚至平方增长。经验边界：PG 12+ 千级分区可用但 prepared statement 与复杂 join 会先恶化；数千分区时锁表（每分区一个 `pg_class` 锁）与 catalog 膨胀成为主要瓶颈。容量账公式：`单查询编译开销 ≈ 分区数 × 每分区规划代价 + 锁开销`，规划代价又随 join 表数放大。
- **取舍**：按天 vs 按月分区：热数据高频查询、TTL 按天删除的场景按天分区收益大（drop partition 秒级）；查询跨大时间范围且写入平稳的场景按月分区让分区数缩小 30 倍。另一个取舍是"分区数 vs 分区键裁剪率"：如果查询大部分不带分区键，分区纯属负资产。
- **实战**：治理动作：① 用 `EXPLAIN (ANALYZE)` 看 Planning Time 是否随时间上涨——它是分区病的直接指标；② 保留窗口与分区粒度联动（3 年保留 + 按月分区 = 36 个分区）；③ 历史分区合并到月/年表；④ 应用侧 prepared statement 的连接池注意 plan cache 与 DDL（新分区）失效交互。

```python
# 分区容量账：Planning Time 随分区数与 join 数的模拟（纯标准库）
# 基线：Python 3.9+


def planning_time_ms(n_partitions: int, n_joins: int = 1, per_part_us: float = 30) -> float:
    """每分区规划代价 × 分区数 × join 表数（简化线性模型）"""
    return n_partitions * n_joins * per_part_us / 1000


def recommend_granularity(retention_days: int, daily_query_ratio: float) -> str:
    """按查询裁剪率推荐分区粒度"""
    if daily_query_ratio > 0.8 and retention_days <= 400:
        return "day"
    return "month" if retention_days <= 1200 else "quarter"


def main() -> None:
    for parts, joins in [(36, 1), (1000, 1), (1000, 4)]:
        t = planning_time_ms(parts, joins)
        print(f"partitions={parts} joins={joins} -> planning≈{t:.0f}ms")
    assert planning_time_ms(1000, 4) > 100  # 千分区+4表join 编译即超百毫秒
    print("推荐:", recommend_granularity(1095, daily_query_ratio=0.9))  # 3年+高热日查询
    print("推荐:", recommend_granularity(1095, daily_query_ratio=0.3))


if __name__ == "__main__":
    main()
```

**追问 1**：PG 13+ 的 runtime partition pruning 与 plan-time pruning 有什么区别，对 Python 应用意味着什么？
→ 一句话提示：带参数的 prepared statement 在 plan 阶段不知道分区键值，PG 会生成 init plan 在执行时裁剪——psycopg/asyncpg 的参数化查询能享受 runtime pruning，但 EXPLAIN 不带参数时看到的是全分区展开，别误判。

**追问 2**：分区过多时锁有什么问题？
→ 一句话提示：每次查询要对每个分区拿 `AccessShareLock`，DDL（加分区）要 `ExclusiveLock`，千分区下 DDL 与查询的锁排队可见恶化，`lock_timeout` 会开始报警。

## 背诵要点
- Planning Time 是分区病的直接指标：编译开销 ≈ 分区数 × join 数 × 单分区规划代价。
- 经验边界：千级分区可用、数千分区锁与 catalog 先恶化；粒度选择 = 保留窗口 + 裁剪率。
- 裁剪两种：plan-time（字面量）与 runtime（参数化 prepared statement），EXPLAIN 验证要带参数。

## 复盘追问
- 为什么"分区越多查询越快"是伪命题？提示：收益来自裁剪率不是分区数，裁剪不了时分区纯付规划税。
- 如果必须保留千级分区，应用侧能做什么？提示：强制查询都带分区键（SQL 审核门禁）、限制 join 数、控制 prepared plan cache 失效频率。
