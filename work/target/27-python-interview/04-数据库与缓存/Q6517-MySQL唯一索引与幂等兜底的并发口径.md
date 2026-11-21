---
title: [Q6517] 唯一索引兜底：死锁与重复键的并发口径
date: 2026-11-19
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6517 · 唯一索引兜底的并发口径

> 难度:★★★ | 标签:唯一约束, 死锁, 幂等

**问**：用唯一索引做幂等兜底（A102 方案）在**高并发同键**下会遇到什么——「先查后插」为什么必炸？`INSERT ... ON DUPLICATE KEY UPDATE` / `INSERT IGNORE` / 唯一键捕获三种写法的死锁与语义差异是什么，怎么选？

**答**：① 「先 SELECT 有没有再 INSERT」在并发下是 TOCTOU 竞态：两个事务同时查到「没有」→ 双双插入 → 一个报重复键（可兜），但如果检查与插入之间还有其他动作（如先扣库存再插单），窗口更大——**正确性必须靠唯一约束本身，查只是优化**。② 三写法并发口径：`INSERT IGNORE`：冲突静默跳过（返回 0 行），语义「已存在就算成功」——适合幂等标记位，**但它也吞其他错误**（如数据截断警告变静默，坑）；`ON DUPLICATE KEY UPDATE`：冲突转更新，适合「计数器/最新状态」语义，但**高并发同键时 update 行锁串行化，且自增 ID 空洞暴涨**（冲突也消耗 auto_increment）；捕获 IntegrityError：语义最明确（知道「这次是重复」可查回原单返回终态），配合「不同事务顺序获取两行唯一键索引间隙锁」的死锁场景要重试。③ 选择矩阵：幂等标记 → IGNORE（或捕获）；状态覆盖 → ODKU；需要「区分首次/重复并返回原单」→ 捕获 IntegrityError + 查回。

```python
# 基线 SQLAlchemy 2.0 + SQLite（语义演示）；MySQL/PG 死锁口径见追问
import sqlalchemy as sa

meta = sa.MetaData()
pay = sa.Table("pay", meta,
    sa.Column("req_id", sa.String(36), primary_key=True),     # 唯一约束 = 幂等真相源
    sa.Column("amount", sa.Numeric(10, 2)),
    sa.Column("cnt", sa.Integer, default=1))

eng = sa.create_engine("sqlite://", connect_args={"check_same_thread": False})
meta.create_all(eng)

def first_time(conn, req_id, amount):
    """捕获路径：能区分「首次」与「重复」，重复时查回原单返回终态。"""
    try:
        conn.execute(pay.insert().values(req_id=req_id, amount=amount))
        return "created"
    except sa.exc.IntegrityError:
        row = conn.execute(sa.select(pay.c.cnt).where(pay.c.req_id == req_id)).one()
        return f"duplicate (cnt={row.cnt})"

def upsert_counter(conn, req_id, amount):
    """ODKU 口径（MySQL 语法；SQLite 用 ON CONFLICT 等价）：
    INSERT ... ON DUPLICATE KEY UPDATE cnt = cnt + 1 —— 计数语义。"""
    conn.execute(sa.text(
        "INSERT INTO pay (req_id, amount, cnt) VALUES (:r, :a, 1) "
        "ON CONFLICT(req_id) DO UPDATE SET cnt = cnt + 1"), {"r": req_id, "a": amount})
    return conn.execute(sa.select(pay.c.cnt).where(pay.c.req_id == req_id)).scalar()

if __name__ == "__main__":
    with eng.begin() as c:
        r1 = first_time(c, "req-1", 100)
        r2 = first_time(c, "req-1", 100)          # 客户端重试同键
    assert r1 == "created" and r2.startswith("duplicate")
    print("捕获路径:", r1, "/", r2)
    with eng.begin() as c:
        for _ in range(3):
            n = upsert_counter(c, "req-1", 100)
    print("ODKU 计数语义:", n, "（冲突转自增）")
    # 死锁口径：MySQL 并发 ODKU 同键 = 行锁串行（可接受）；并发 INSERT 新键互相插入意向锁
    # 间隙锁（gap lock）→ 死锁概率随并发升，解法：缩短事务、固定键获取顺序、捕获 40001 重试。
```

**追问**：1) 为什么高并发 `INSERT` 新键会死锁？——插入意向锁与间隙锁组合：事务 A 持有间隙锁准备插入键 10，事务 B 也要插键 10 附近 → 等待环；MySQL 5.7+ insert intention 锁改进但仍要事务短、键顺序固定；PG 的 MVCC 模型下无间隙锁，唯一冲突表现为等第一个写事务结果（`could not serialize` 概率低）。2) IGNORE 吞错的具体案例？——`INSERT IGNORE` 把数据截断（严格模式下应报错）降级为警告：金额字段溢出被静默截断入库——金融场景禁用 IGNORE 的理由。3) auto_increment 空洞除了难看还有什么害处？——溢出风险（int 用尽）与主从复制大事务放大；高并发计数器用 ODKU 前先评估键冲突率，冲突率高换 Redis 原子计数+定期落库。

## 背诵要点
1. 正确性靠唯一约束本身，「先查后插」只是优化——检查窗口内必有竞态。
2. 三写法矩阵：IGNORE=幂等标记（但吞数据错误，金融禁用）、ODKU=计数/状态覆盖（行锁串行+自增空洞）、捕获 IntegrityError=可查回原单返回终态。
3. 并发新键 INSERT 的死锁来自间隙锁组合：事务短、键顺序固定、捕获 40001 重试。

## 复盘追问
1. 你的幂等表用 ODKU 但 QPS 高时主从延迟飙升，为什么？（提示：同键行锁串行 + 冲突也消耗自增 + 复制重放串行——热点行问题，拆分片计数或 Redis 缓冲）
2. SQLite 演示与 MySQL 行为的主要差异是什么？（提示：SQLite 表级锁无死锁、ON CONFLICT 语义更细（DO NOTHING/DO UPDATE 可指定目标）——真实口径以 MySQL/PG 为准）
