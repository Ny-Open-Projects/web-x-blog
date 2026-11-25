---
title: "[Q6186] get_or_create 的并发窗口：唯一约束才是权威判据"
date: 2026-11-23
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6186 · get_or_create 的并发窗口：唯一约束才是权威判据

难度：P6 ｜ 标签：Django、get_or_create、IntegrityError、幂等、savepoint

**问**：注册/建租户接口用 `get_or_create(email=...)`，"先查后插"逻辑看着天衣无缝，压测时偶发 500：`IntegrityError: duplicate key value violates unique constraint`。查和插之间到底发生了什么？为什么不能直接 `try/except` 吞掉？在事务里捕获它还会引出什么新问题？

**答**：
结论：`get_or_create` 是 check-then-act：先 SELECT，没有就 INSERT。两个请求同时查不到 → 同时 INSERT → 唯一约束让其中一个失败。这不是框架 bug，而是并发系统的常态；唯一约束才是**权威判据**，正确姿势是"捕获冲突 → 回滚 → 重新查询 → 返回已有对象"，让接口对并发幂等。直接吞掉异常返回 None/500 会把"已存在"错误地表达成失败。

取舍：三种实现。a) `get_or_create` + 捕获 `IntegrityError` 再 `get`（Django 内部就是这个逻辑，但在**外层事务**里必须用 savepoint，否则事务被标记为 aborted，后续查询全报 `current transaction is aborted`）；b) `INSERT ... ON CONFLICT DO NOTHING`（PG）/ `INSERT IGNORE`（MySQL）一步到位，再 SELECT；c) 悲观锁 `SELECT ... FOR UPDATE`（适合"必须先读再决定"的复杂逻辑，代价是串行化）。注册这类场景推荐 a 或 b。

实战：事故形态是"压测 200 并发建同一个租户，10% 报 500，重试就成功，所以监控上只是零星错误率"。另一个连锁事故是"在 `atomic()` 里 catch 了 IntegrityError 继续执行业务，后续所有 SQL 都报事务 aborted"，根因就是没开 savepoint。下面用 sqlite 复现两个线程同时 get_or_create，再演示"捕获后重查"的幂等实现。

```python
import sqlite3
import threading

con = sqlite3.connect(":memory:", check_same_thread=False)
con.execute("CREATE TABLE account (id INTEGER PRIMARY KEY, email TEXT UNIQUE, created INTEGER)")
lock = threading.Lock()
barrier = threading.Barrier(2)
results = []


def get_or_create(email):
    row = con.execute("SELECT id FROM account WHERE email = ?", (email,)).fetchone()
    if row:
        return row[0], "hit"
    barrier.wait()                      # 两个线程都确认"不存在"
    try:
        with lock:
            cur = con.execute("INSERT INTO account (email, created) VALUES (?, 0)", (email,))
        return cur.lastrowid, "created"
    except sqlite3.IntegrityError as e:
        return None, f"IntegrityError: {e}"


def worker():
    results.append(get_or_create("a@example.com"))


ts = [threading.Thread(target=worker) for _ in range(2)]
for t in ts:
    t.start()
for t in ts:
    t.join()

print("[1] 两个线程同时 get_or_create:", results)
print("[2] 实际落库行数:", con.execute("SELECT COUNT(*) FROM account").fetchone()[0])


def get_or_create_retry(email):
    for _ in range(3):
        row = con.execute("SELECT id FROM account WHERE email = ?", (email,)).fetchone()
        if row:
            return row[0], "hit"
        try:
            with lock:
                cur = con.execute("INSERT OR IGNORE INTO account (email, created) VALUES (?, 0)", (email,))
            if cur.rowcount:
                return cur.lastrowid, "created"
        except sqlite3.IntegrityError:
            pass                            # 输给了并发，回到循环顶部重查
    raise RuntimeError("conflict retry exhausted")


barrier = threading.Barrier(2)
results.clear()
print("[3] 捕获冲突后重查:", get_or_create_retry("b@example.com"), get_or_create_retry("b@example.com"))
print("[4] 行数:", con.execute("SELECT COUNT(*) FROM account").fetchone()[0])
```

**追问一**：为什么在 `atomic()` 里直接 `except IntegrityError` 会引出 "transaction aborted"？—— PostgreSQL 里任何语句报错都会把整个事务置为失败态，后续语句一律被拒，直到 ROLLBACK 或回滚到 savepoint。Django 的嵌套 `atomic()` 就是 savepoint，所以正确写法是 `with transaction.atomic():` 内层包住 INSERT，冲突时内层回滚到 savepoint、外层事务继续可用。

**追问二**：`update_or_create` 也有同样问题吗？—— 有，而且更糟：并发时两个事务都能拿到"行存在"，然后各自 UPDATE，后写的覆盖先写的（丢更新），接口层面看不出错误。要么 `select_for_update()` 锁行，要么用乐观锁（版本号 `WHERE version = ?`）检测冲突并重试。唯一约束只能防"重复插入"，防不了"覆盖更新"。

## 背诵要点
- `get_or_create` 是 check-then-act，并发下必撞唯一约束；唯一约束是权威判据，必须"捕获 → 回滚 → 重查"。
- 事务内捕获要 savepoint（Django 嵌套 atomic），否则 PG 事务 aborted，后续全报错。
- 更新场景靠 `select_for_update` 或乐观锁版本号，唯一约束管不了丢更新。

## 复盘追问
- 注册接口 10% 概率 500 且重试成功，如何定位并改成幂等？（并发窗口、IntegrityError、重查）
- 为什么"catch 掉异常继续跑"会引发连锁失败？（事务 aborted、savepoint）
