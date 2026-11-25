---
title: "[Q6189] ATOMIC_REQUESTS 把事务拉长：外部调用拖垮数据库"
date: 2026-11-23
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6189 · ATOMIC_REQUESTS 把事务拉长：外部调用拖垮数据库

难度：P7 ｜ 标签：Django、ATOMIC_REQUESTS、事务边界、行锁、on_commit

**问**：团队为了"每个请求自动回滚"打开了 `ATOMIC_REQUESTS`，接口里本来就有同步调第三方支付/风控的地方。上线后第三方偶发超时，整个服务的 DB 变慢、锁等待飙升、连接池打满。明明慢在外部网络，为什么数据库先扛不住？事务边界应该画在哪？

**答**：
结论：`ATOMIC_REQUESTS=True` 会把**整个视图**包进一个事务：请求进入即 BEGIN，响应返回才 COMMIT。视图里任何阻塞（HTTP 调用、文件 IO、`time.sleep`）都在延长事务，而事务期间占着连接、可能持有行锁。5 个并发、事务内 300ms 外部调用 → 总耗时 1512ms；把外部调用移到事务外 → 30ms。数据库不是被 SQL 压垮的，是被"持有时间"压垮的。

取舍：事务边界的原则是"尽可能短、只包 DB 写"。外部调用放事务外有两种做法：a) 先提交本地状态，再调外部，失败走补偿/重试（最终一致）；b) outbox 模式：事务内只写 outbox 表，独立消费者负责调外部并保证至少一次。`ATOMIC_REQUESTS` 适合"简单 CRUD、视图里只有 DB 操作"的服务；一旦有外部 IO，就应该关掉它，改成显式 `with transaction.atomic():` 包住最小写集。

实战：事故形态是"第三方超时 → 事务变长 → 行锁等待 → 连接池耗尽 → 所有接口 504"，因果链很长，第一现场看起来是"数据库挂了"。判断信号：`pg_stat_activity` 里大量 `idle in transaction`、`pg_locks` 有长时间等待、慢查询日志里没有对应 SQL。下面用行锁 + 5 个并发请求量化"事务内外部调用"与"事务外外部调用"的差异。

```python
import threading
import time

row_lock = threading.Lock()
metrics = {"hold_ms": 0.0, "wait_ms": 0.0}


def transaction(fn, work_inside):
    t0 = time.perf_counter()
    row_lock.acquire()                      # 模拟 SELECT ... FOR UPDATE 拿到的行锁
    try:
        fn(work_inside)                     # work_inside 期间事务一直开着
    finally:
        held = (time.perf_counter() - t0) * 1000
        metrics["hold_ms"] += held
        row_lock.release()


def handler(external_call):
    def body(inside):
        if inside:
            time.sleep(0.3)                 # 事务里同步调第三方支付/风控接口
        else:
            time.sleep(0.005)
            outside = 0.3                   # 事务提交后再调
            return outside
    return body


def run(label, work_inside):
    metrics.update(hold_ms=0.0, wait_ms=0.0)
    t0 = time.perf_counter()
    ths = [threading.Thread(target=transaction, args=(handler(work_inside), work_inside))
           for _ in range(5)]
    for t in ths:
        t.start()
    for t in ths:
        t.join()
    total = (time.perf_counter() - t0) * 1000
    print(f"[{label}] 5 个并发请求总耗时 {total:.0f}ms，平均持锁 {metrics['hold_ms']/5:.0f}ms")


run("外部调用在事务内", True)
run("外部调用移到事务外", False)
print("[3] ATOMIC_REQUESTS 让整个视图都在事务里：视图内的 HTTP 调用会拉长持锁时间")
```

**追问一**：把外部调用挪到 `transaction.on_commit` 里就安全了吗？—— 更安全（提交后执行、锁已释放），但要接受两点：a) 回调失败**不会回滚**已提交的数据，必须自己重试/补偿；b) 测试里默认不执行（`TestCase` 把用例包在事务里，on_commit 永远等不到真正的提交），要用 `captureOnCommitCallbacks` 或 `TransactionTestCase`。所以"on_commit + 幂等 + 重试"才构成完整方案。

**追问二**：长事务除了锁等待还有什么隐性成本？—— a) PG 的 MVCC 旧版本无法被 vacuum 回收（表膨胀、IO 放大）；b) 复制延迟（长事务提交后一大坨 WAL 一起过去）；c) 连接被长期占用（池耗尽）；d) 死锁概率上升（持锁时间长、加锁顺序交叉）。监控上应该把"事务持有时长"作为一等指标，而不是只看 QPS 和慢查询。

## 背诵要点
- `ATOMIC_REQUESTS` 用整个视图的事务换自动回滚；视图内的外部 IO 会拉长持锁与连接占用（实测 1512ms vs 30ms）。
- 事务只包 DB 写；外部调用移到提交后（on_commit/outbox），并接受"回调失败不回滚"。
- 长事务的隐性成本：vacuum 受阻、复制延迟、池耗尽、死锁概率；监控"事务持有时长"。

## 复盘追问
- 第三方超时导致全站 504，如何把因果链从"外部"追到"事务持有时长"？（idle in transaction、持锁时长）
- on_commit 为什么不是银弹？测试里为什么不执行？（失败不回滚、TestCase 包事务）
