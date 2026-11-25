---
title: "[Q6751] binlog 三种格式：statement 重放 RAND() 分叉，row 贵但可复现"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6751 · binlog 三种格式：statement 重放 RAND() 分叉，row 贵但可复现

难度：P6 ｜ 标签：MySQL、binlog、复制一致性、statement/row/mixed

基线：Python 3.12；用 sqlite3 双连接模拟主从，RAND_SALT 自定义函数模拟非确定性语句。

**问**：从库自增 ID 与主库对不上、`NOW()` 写入的时间差了几秒、带 `RAND()` 的活动抽奖结果主从完全不同——这些都是 binlog_format 引起的。`statement`、`row`、`mixed` 三种格式到底怎么选？为什么大量老系统还在用 statement，而新规范都要求 row？

**答**：
- **结论**：`statement` 复制的是 SQL 文本，从库**重新执行**这条语句；只要语句含非确定成分（`NOW()`、`RAND()`、`UUID()`、`LIMIT` 无 ORDER BY、依赖会话变量），主从执行环境不同就会**分叉**，且分叉不可检测地累积。`row` 复制的是**行的前后镜像**，从库做的是"幂等替换"而非"重算"，天然一致；代价是 binlog 体积大（一条 UPDATE 影响 1 万行就是 1 万个行事件）、且 `binlog_row_image` 默认 FULL。`mixed` 让 MySQL 自动在两种格式间切换：默认 statement，遇到非确定语句降级为 row。
- **取舍**：① 上游应用（尤其 Python 写的定时任务）经常造出非确定 SQL（`UPDATE ... SET seed=RAND()`），statement 的风险是**静默的**——不报错、不告警，某天对账才发现；② row 的风险是**显式的**：binlog 涨、主从延迟涨、误删恢复时闪回工具依赖 row 格式；③ mixed 看似折中，但切换边界由版本决定，审计时"到底记了什么"说不清；④ 用 binlog 做下游订阅（canal 类）或闪回，**只能 row**。
- **实战**：① 生产一律 `binlog_format=ROW`，把它写进 SQL 审核工单的静态检查；② 改格式的切换窗口在低峰期做并观察 `Seconds_Behind_Master`；③ row 下大事务照旧要拆（Q896/Q6686），因为行事件数等于影响行数；④ 抽奖、发号这类必须精确可复现的逻辑，把随机种子放应用层并落库，别指望数据库函数。

```python
"""statement 复制重算非确定语句 -> 主从分叉；row 复制行镜像 -> 幂等一致。"""
import random
import sqlite3


def new_db() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE ticket(id INTEGER PRIMARY KEY, weight REAL, ts TEXT)")
    conn.execute("INSERT INTO ticket VALUES (1, 1.0, '2026-11-24 09:00:00')")
    # 模拟 MySQL 的 RAND()：主从各自执行时拿到不同随机数
    conn.create_function("RAND_SALT", 0, lambda: random.random())
    return conn


class RowEvent:
    """row 格式的事件：只带前后镜像，不重算。"""

    def __init__(self, before: tuple, after: tuple) -> None:
        self.before, self.after = before, after

    def replay(self, conn: sqlite3.Connection) -> None:
        conn.execute(
            "UPDATE ticket SET weight=?, ts=? WHERE id=?",
            (self.after[1], self.after[2], self.after[0]),
        )


def master_update(conn: sqlite3.Connection) -> tuple:
    conn.execute("UPDATE ticket SET weight = weight * RAND_SALT(), ts='09:00:01'")
    conn.commit()
    return conn.execute("SELECT id, weight, ts FROM ticket").fetchone()


if __name__ == "__main__":
    random.seed(7)
    master = new_db()
    sql_text = "UPDATE ticket SET weight = weight * RAND_SALT(), ts='09:00:01'"
    after = master_update(master)
    print("master:", after)

    # --- statement 格式：从库重放 SQL 文本，随机数不同 ---
    slave_s = new_db()
    slave_s.execute(sql_text)          # 重算！
    slave_s.commit()
    got = slave_s.execute("SELECT id, weight, ts FROM ticket").fetchone()
    print("statement 从库:", got, "| 分叉:", abs(got[1] - after[1]) > 1e-9)

    # --- row 格式：主库把行事件（前/后镜像）发过来，从库幂等替换 ---
    slave_r = new_db()
    RowEvent((1, 1.0, "2026-11-24 09:00:00"), after).replay(slave_r)
    got = slave_r.execute("SELECT id, weight, ts FROM ticket").fetchone()
    print("row 从库:      ", got, "| 一致:", got == after)

    # --- NOW() 的分叉：statement 重放时刻不同，各写各的本地时间 ---
    slave_t = new_db()
    slave_t.create_function("TIME_TEXT", 0, lambda: "09:00:07")  # 从库的"当前时间"
    slave_t.execute(sql_text.replace("'09:00:01'", "TIME_TEXT()"))
    slave_t.commit()
    got = slave_t.execute("SELECT ts FROM ticket").fetchone()[0]
    print("NOW() 类语句: 主库 ts=09:00:01, 从库重放 ts=%s -> 时间语义漂移" % got)

    # --- 体积账：UPDATE 影响 N 行，statement 1 条文本，row N 个行事件 ---
    for rows in (1, 10_000, 1_000_000):
        print(f"影响 {rows:>8,} 行: statement ~1 条 SQL 文本, "
              f"row ~{rows:,} 个行事件（默认 binlog_row_image=FULL）")
    print("结论：要可复现选 row；statement 的分叉是静默的，等对账爆出来已经晚了")
```

**追问一**：`mixed` 既然会自动降级，为什么不直接全用 mixed？

→ 解析：降级的判定是"语句是否被标记为不安全"，这个清单随版本变化，而且只覆盖 MySQL 自己认识的模式——应用层把随机数算好拼进 SQL（`SET v = 0.7234`）它就识别不出来，但语义上同样不可复现。mixed 让"binlog 里到底记了什么"变成运行时行为，排障、审计、闪回工具都要处理两种事件格式。确定性格式（row）+ 静态审核拦非确定写法，比把确定性交给运行时判定可靠。

**追问二**：row 格式下为什么从库应用行事件也会丢一致性？

→ 解析：row 事件按主键幂等替换，但从库**表结构漂移**（字段缺失、类型不同）会让替换失败或截断（Q6652 主从 schema 漂移就是这类事故）；另外 `binlog_do_db`/过滤规则、以及无主键表的回放（Q6738）都会破坏"幂等替换"的前提。row 解决的是"重算不确定"，不解决"两边结构不一致"——所以 schema 变更必须先从库、后主库，保持回放期间的兼容。
