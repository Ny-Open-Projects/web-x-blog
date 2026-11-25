---
title: "[Q6266] 批量接口的 207：逐条 savepoint 与全有或全无的取舍"
date: 2026-11-25
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6266 · 批量接口的 207：逐条 savepoint 与全有或全无的取舍

难度：P7 ｜ 标签：批量接口、207、幂等、savepoint、事务、部分成功

基线：CPython 3.12.2，纯标准库；用 `sqlite3` 内存库与 `SAVEPOINT` 演示"全有或全无"和"逐条提交 + 207"两种批量语义。

**问**：批量导入接口一次收 1000 条记录，代码在一个大事务里逐条 `insert`。第 900 条因为唯一键冲突抛了 `IntegrityError`，外层 `except` 打了日志、返回 200 和 `{"success": 1000}`——实际上整个事务已回滚，一条都没进库。客户端看到"成功"就不再重试，数据丢了 3 天。另一个版本改成逐条提交，返回 200 + `success: 999, failed: 1`，但客户端重试整个批次时，前 999 条又因为唯一键冲突全部失败。批量接口到底该原子还是逐条？207 表示什么？重试怎么保证幂等？

**答**：

- **结论**：批量接口没有唯一正确答案，只有**契约**：① **全有或全无**——一个外层事务，任一条失败就 `ROLLBACK`，返回 409/400，客户端知道"整批没生效"，实现简单、状态一致，但一条坏数据会拖死 999 条好数据；② **逐条独立**——每条一个 `SAVEPOINT`（或独立事务），失败的只回滚该条，成功的保留，整体返回 **207 Multi-Status**，body 里逐条给 `201/409/422`，客户端能精确重试失败项；③ **fail-fast**——遇到第一条失败就停，返回已成功的条数，语义介于两者之间，但客户端最难处理。207 只表示"有多个独立结果"，**不代表原子**；它也不是普通 REST API 的默认选择，很多客户端只认 2xx/4xx，需要文档和 SDK 配合。
- **取舍**：全有或全无适合"批次是一个业务整体"（对账、转账），逐条适合"批量导入/同步"（部分成功可接受）。逐条的代价是：① 部分状态需要业务能容忍；② 响应体膨胀（1000 条结果）；③ 每条一个 savepoint 有额外开销，但远小于 1000 个独立事务（SQLite 里 savepoint 比 `BEGIN/COMMIT` 轻）；④ 失败项重试必须幂等，否则重复插入。另一个坑是"逐条提交 + 外层事务"混用：外层没提交，savepoint 释放了也没落盘，进程崩溃全丢；必须明确最外层事务边界。
- **实战**：事故版本把 `IntegrityError` 吞了还返回 200，根因是"异常处理与事务边界脱节"。修复：① 改成逐条 savepoint，响应 207 + 每条 `{index, status, error}`；② 全批加 `Idempotency-Key`，服务端记录"该 key 已处理的结果"，重试直接返回上次的 207，而不是重新插入；③ 唯一键冲突返回 409 并标记 `duplicate`，客户端只重试 5xx/429；④ 监控 `batch_partial_success` 比例，超过 5% 告警（说明上游数据质量或契约有问题）。上线后重复导入归零，丢数据事故归零。

下面用 SQLite 验证：全有或全无在冲突时回滚到 0 行；逐条 savepoint 得到 `[201, 201, 409]` 且保留 2 行；重复批次因主键幂等，仍然只保留 2 行。

```python
# 批量写入: 全有或全无 vs 逐条 savepoint + 207
import sqlite3

conn = sqlite3.connect(":memory:", isolation_level=None)
conn.execute("CREATE TABLE items (id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE)")


def batch_all_or_nothing(rows):
    conn.execute("BEGIN")
    try:
        for item_id, name in rows:
            conn.execute("INSERT INTO items VALUES (?, ?)", (item_id, name))
        conn.execute("COMMIT")
        return 201, {"inserted": len(rows)}
    except sqlite3.IntegrityError as exc:
        conn.execute("ROLLBACK")
        return 409, {"error": str(exc), "inserted": 0}


rows = [(1, "a"), (2, "b"), (1, "duplicate-id")]
status, body = batch_all_or_nothing(rows)
count = conn.execute("SELECT COUNT(*) FROM items").fetchone()[0]
print("[1] 全有或全无:", status, body, "| 行数:", count)
assert status == 409 and count == 0


def batch_per_item(rows):
    results = []
    for index, (item_id, name) in enumerate(rows):
        conn.execute("SAVEPOINT sp")
        try:
            conn.execute("INSERT INTO items VALUES (?, ?)", (item_id, name))
            conn.execute("RELEASE sp")
            results.append({"index": index, "status": 201})
        except sqlite3.IntegrityError as exc:
            conn.execute("ROLLBACK TO sp")
            conn.execute("RELEASE sp")
            results.append({"index": index, "status": 409, "error": str(exc)})
    overall = 207 if any(r["status"] != 201 for r in results) else 201
    return overall, results


status, results = batch_per_item(rows)
count = conn.execute("SELECT COUNT(*) FROM items").fetchone()[0]
print("[2] 逐条:", status, results, "| 行数:", count)
assert status == 207
assert [r["status"] for r in results] == [201, 201, 409]
assert count == 2

# 重试同一批: 已成功的两条幂等冲突, 不会重复写入
status, results = batch_per_item(rows)
count = conn.execute("SELECT COUNT(*) FROM items").fetchone()[0]
print("[3] 重试:", [r["status"] for r in results], "| 行数:", count)
assert [r["status"] for r in results] == [409, 409, 409]
assert count == 2, "主键保证幂等, 不会重复插入"

# 部分成功后的查询: 只有 a/b
names = [row[0] for row in conn.execute("SELECT name FROM items ORDER BY id")]
print("[4] 最终数据:", names)
assert names == ["a", "b"]

print("[5] 结论: 207 只表示多条独立结果; 原子性由事务边界决定; 重试靠唯一键/幂等键")
```

**追问一**：`SAVEPOINT` 和嵌套 `BEGIN` 有什么区别？—— SQLite 不支持真正的嵌套事务，`BEGIN` 在已有事务中会报错；`SAVEPOINT` 是命名保存点，可以在同一个外层事务里多次 `ROLLBACK TO sp` / `RELEASE sp`，实现"部分回滚"。在 PostgreSQL 里叫 `SAVEPOINT`，语义类似；MySQL InnoDB 也支持。注意 `ROLLBACK TO sp` 之后保存点仍然存在，需要再 `RELEASE sp` 释放（或继续复用），否则会一直留在事务栈里。

**追问二**：207 的响应体应该怎么设计？—— 至少包含：整体 `status`、每条记录的稳定标识（`index` 或业务 ID）、该条的 HTTP 状态/错误码、可读错误信息、是否可重试。不要只返回一个 `success: 999, failed: 1` 的汇总，客户端无法知道哪条失败、该重试什么。对于超大 batch，响应体本身也可能成为负担，可以只返回失败项 + 总数（206? 不，仍是 207），成功的默认视为 201，并在文档里写清楚。

## 背诵要点

- 全有或全无：外层事务 + 任一失败 `ROLLBACK`，返回 4xx，状态一致但坏一条拖死全批。
- 逐条：每条 `SAVEPOINT`，失败只回滚该条，整体 207 + 逐条结果；207 不代表原子。
- 重试幂等靠唯一键/幂等键；异常处理必须和事务边界对齐，不能吞异常还返回 200。

## 复盘追问

- 为什么"逐条 savepoint + 外层未提交"仍然可能全丢？（savepoint 只释放到外层事务，进程崩溃/外层回滚会一起丢）
- 207 和 200 + 自定义 `results` 数组怎么选？（207 是 HTTP 语义、可被通用客户端识别；200 更兼容但需要 SDK 解析约定）
