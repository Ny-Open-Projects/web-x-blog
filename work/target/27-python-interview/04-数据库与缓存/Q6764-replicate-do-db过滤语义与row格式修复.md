---
title: "[Q6764] 只想复制订单库：replicate-do-db 过滤的语义坑与 row 格式修复"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6764 · 只想复制订单库：replicate-do-db 过滤的语义坑与 row 格式修复

难度：P7 ｜ 标签：MySQL、复制过滤、binlog、statement 格式、数据一致性

基线：Python 3.12；模拟 binlog 事件流在 statement 与 row 格式下的过滤结果，复现 statement 格式下跨库 UPDATE 被误滤的事故。

**问**：给分析团队搭一台只含订单库（`orders`）的从库，配置 `replicate-do-db = orders` 就完事了？有同事说"这样配置，跨库的 UPDATE 会静默丢数据"。过滤规则到底按什么判定？statement 格式和 row 格式的行为为什么不一样？怎么验证从库没有悄悄少数据？

**答**：
- **结论**：`replicate-do-db` 的判定对象在两种 binlog 格式下完全不同：**statement 格式按"当前默认数据库（USE 的库）"判定**——一条 `UPDATE` 写在别的连接上下文里执行（没有 USE orders，或从其他库跨库写 `orders.t`），其默认库不是 orders，整条语句被过滤丢弃，即使它修改的是 orders 的表；**row 格式按"事件中行所属的库"判定**——每行变更自带表所在库，`orders` 表的行变更无论从哪个连接发出都会被复制。所以：**过滤场景强制 row 格式**（Q6751 已论证 row 的可复现性，这里再加一条理由），或改用 `replicate-wild-do-table = orders.%` 精确到表。过滤配置是"静默少数据"的高发地：被滤掉的事件不报错，只能靠对账发现。
- **取舍**：① 库级过滤（do-db）vs 表级过滤（wild-do-table）：表级更精确但要枚举表，新表漏配置就丢——变更流程里加"新表入过滤清单"检查项；② 过滤从库不能当数据源再级联：GTID 空洞会让下游复制报错，级联链上要么全过滤同款要么不做过滤；③ 过滤从库的校验和与主库必然不同（少数据是预期），对账要按"过滤后的期望子集"做，不能用全库 checksum；④ 临时表与跨库外键在过滤边界上最容易出鬼，规避。
- **实战**：① 上线过滤从库前，用"主库抽样比对"（Q1409）跑一轮预期子集校验；② 监控两个指标：SQL 线程是否报错（不该报）、过滤从库行数增长率与主库 orders 增长率的比例（偏差即丢数据信号）；③ 配置进版本库走评审，禁手改运行时配置；④ 灾备从库不做过滤，过滤从库只承担分析类旁路角色——别把容灾和过滤混在一台实例上。

```python
"""复制过滤语义模拟：statement 按默认库过滤 vs row 按行所属库过滤。"""
from dataclasses import dataclass


@dataclass
class StmtEvent:
    """statement 格式事件：只有 SQL 文本 + 发起连接的默认库。"""
    default_db: str
    sql: str


@dataclass
class RowEvent:
    """row 格式事件：每行变更加自带 (库, 表, 主键)。"""
    rows: list  # [(db, table, pk)]


@dataclass
class FilterConfig:
    do_db: str  # replicate-do-db


def apply_filter_stmt(events: list, cfg: FilterConfig) -> tuple[int, list]:
    """statement 格式: 按事件的默认库(USE 的库)判定, 不看 SQL 内容。"""
    applied, dropped = 0, []
    for ev in events:
        if ev.default_db == cfg.do_db:
            applied += 1
        else:
            dropped.append(f"默认库={ev.default_db} != do_db={cfg.do_db}")
    return applied, dropped


def apply_filter_row(events: list, cfg: FilterConfig) -> tuple[int, list]:
    """row 格式: 按行自带所属库判定, 与连接默认库无关。"""
    applied, dropped = 0, []
    for ev in events:
        if any(db == cfg.do_db for db, _, _ in ev.rows):
            applied += 1
        else:
            dropped.append(f"行库集合={ {db for db, _, _ in ev.rows} } 不含 {cfg.do_db}")
    return applied, dropped


if __name__ == "__main__":
    cfg = FilterConfig("orders")
    # 事故现场: 报表程序连在报表库, 跨库回写订单状态 (statement 语义下默认库=report)
    events = [
        StmtEvent("orders", "UPDATE orders.t_order SET status='paid' WHERE id=1"),
        StmtEvent("report", "UPDATE orders.t_order SET status='paid' WHERE id=2"),
        StmtEvent("report", "INSERT INTO report.t_agg ..."),   # 本就该滤掉
    ]
    n, dropped = apply_filter_stmt(events, cfg)
    print(f"statement 格式: 复制 {n}/3 条")
    for d in dropped:
        print(f"    丢弃: {d}")
    print("    -> 事故: 跨库 UPDATE 被静默滤掉, 从库少一行数据, 无任何报错\n")

    # row 格式: 同一批写拆成行事件, 行自带所属库
    row_events = [RowEvent([("orders", "t_order", 1), ("report", "t_agg", 9)]),
                  RowEvent([("orders", "t_order", 2)])]
    n2, dropped2 = apply_filter_row(row_events, cfg)
    print(f"row 格式重放: 复制 {n2}/2 条, 丢弃 {[d for d in dropped2]}")
    print("    -> orders 的行变更被完整复制, report 的被滤, 与连接默认库无关")
    print("\n结论：过滤从库必须 row 格式或 wild-do-table; 过滤是静默丢数据,")
    print("      只能靠'过滤子集对账'与增长率比值监控兜住")
```

**追问一**：为什么过滤从库不能作为级联复制的中间节点？

→ 解析：过滤从库只重放了一部分事务，但 GTID 集合里这些事务的号可能"跳号"（被过滤的事务号不落在它的 executed 集合里，具体取决于 MySQL 版本的 `gtid_mode` 与过滤交互，历史上产生过"空洞导致下游 RETRIEVED_GTID_SET 校验失败"）。下游从这台级联时，要么报 GTID 不一致中断复制，要么被迫关掉一致性校验——两条路都不可接受。所以架构上过滤节点放链路末端（分析旁路），级联链用全量复制节点。真要做"过滤后再分发"，用 binlog 订阅端自己过滤（Q974 的 canal 模式），订阅端按事件路由比 SQL 线程过滤可控得多。

**追问二**：怎么发现过滤从库在静默丢数据？

→ 解析：三层防线。第一层是**增长率比值**：过滤从库 orders 表的行增长/主库 orders 的行增长应恒等于 1（误差为复制延迟的波动），比值跌破阈值立即告警——成本最低、发现最快。第二层是**抽样对账**：按主键范围抽样主库与过滤从库比对（Q1409 的分块 checksum 思路），低峰跑、分块跑。第三层是**变更流程门禁**：新增表/新增跨库写入的上线检查项里加"过滤清单确认"，把最常见的事故源（新表没进过滤清单）挡在发布前。过滤配置的审计日志也保留：谁改过 do-db 列表，出事能定位变更窗口。
