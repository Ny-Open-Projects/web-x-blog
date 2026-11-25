---
title: "[Q5597] 线程池 submit 每任务固定成本账"
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5597 · 线程池 submit 每任务固定成本账与批量化

难度：P6 | 标签：成本工程 | concurrent.futures | 微基准

**问**：把 10 万个小函数丢进 `ThreadPoolExecutor`，为什么比串行还慢？submit 一次的固定成本有哪些？什么时候该用 chunk 批量化而不是逐任务提交？

**答**：
结论：submit 每次固定成本包括：① 构造 Future 对象 + 内部锁与回调链表；② pickle 无关但需要把 (fn, args) 打包进简单队列表项并 append（受 GIL 保护）；③ 完成侧 wake-up（条件变量 notify）与结果状态迁移。小任务（微秒级）下这些开销远超任务本身，且 worker 线程频繁加锁、切换，吞吐反而低于单线程循环。实测口径：`map` 比"逐个 submit+result"省一层 Future 管理语义但仍逐项调度；真正的批量化是把 N 个小任务合并成 K 个大任务（`pool.map(fn, chunks)` 或传入批量参数），把固定成本摊薄 N/K 倍。
取舍：批量化牺牲了"单任务取消/超时/结果独立性"的粒度；失败传播也从单项变整批，需要任务本身返回逐项状态。
实战：决策阈值经验值 = 单任务耗时 < ~1ms 且任务数 > 数千时考虑 chunk；用 `time.perf_counter` 微基准跑出自己环境里的拐点，别拍脑袋。

```python
import time
from concurrent.futures import ThreadPoolExecutor

WORKERS = 4

def tiny(i):
    return i + 1           # 亚微秒级任务：固定成本主导

def batch_of(js):
    return [j + 1 for j in js]   # 批量版：一次 submit 做 K 项

N = 100_000

# 1) 串行基线
t0 = time.perf_counter()
out = [tiny(i) for i in range(N)]
t_seq = time.perf_counter() - t0

# 2) 逐任务 submit + result（最贵：Future 全量语义）
pool = ThreadPoolExecutor(WORKERS)
t0 = time.perf_counter()
futs = [pool.submit(tiny, i) for i in range(N)]
res = [f.result() for f in futs]
t_submit = time.perf_counter() - t0

# 3) pool.map（省逐项 result 调用，仍逐项调度）
t0 = time.perf_counter()
res2 = list(pool.map(tiny, range(N)))
t_map = time.perf_counter() - t0

# 4) 批量化：K=1000 个大任务
K = 1000
t0 = time.perf_counter()
res3 = list(pool.map(batch_of, [range(k * (N // K), (k + 1) * (N // K)) for k in range(K)]))
t_chunk = time.perf_counter() - t0
pool.shutdown()

flat3 = [x for sub in res3 for x in sub]
assert res == res2 == flat3 == out
print(f"串行循环        {t_seq*1000:7.1f} ms")
print(f"submit+result   {t_submit*1000:7.1f} ms  ({t_submit/t_seq:.1f}x 串行)")
print(f"pool.map        {t_map*1000:7.1f} ms")
print(f"chunk 批量(K=1e3){t_chunk*1000:7.1f} ms  ({t_chunk/t_seq:.2f}x 串行)")
print(f"submit 每任务固定成本 ≈ {(t_submit-t_seq)/N*1e6:.2f} us")

# 5) 对照：真实耗时 1ms 的任务，线程池才有正收益
def heavy(i):
    s = 0
    for _ in range(60_000):   # ~1ms 级
        s += i
    return s
t0 = time.perf_counter()
with ThreadPoolExecutor(WORKERS) as p:
    list(p.map(heavy, range(400)))
t_h = time.perf_counter() - t0
t0 = time.perf_counter()
[heavy(i) for i in range(400)]
t_hs = time.perf_counter() - t0
print(f"1ms 级任务×400: 线程 {t_h:.2f}s vs 串行 {t_hs:.2f}s (加速 {t_hs/t_h:.2f}x)")
```

**追问 1**：为什么 `submit` 比 `map` 贵？
- 追问 2 层：submit 返回 Future 供取消/回调，内部建链表+锁；map 内部也用 submit 但配合结果迭代，少一层用户侧 result 状态查询，差异在小任务时占比明显。
- 追问 3 层：`as_completed` 又比 map 多一层完成通知管理，微任务场景全部让位于固定成本。

**追问 2**：批量化的失败边界怎么设计？
- 追问 2 层：批内单项异常默认让整个 Future 失败——批函数应捕获单项异常返回 (idx, ok, val) 元组，保留逐项状态。
- 追问 3 层：取消粒度同理，批内无法单独取消；关键任务和小任务要分池，避免批量化把可取消性也摊没了。

## 背诵要点
1. submit 固定成本 = Future 构造 + 队列操作 + 唤醒，小任务下大于任务本身，甚至慢于串行。
2. 阈值经验：单任务 <1ms 且量大时 chunk 批量化，摊薄 N/K 倍固定成本；批函数返回逐项状态保留失败边界。
3. 微基准先跑拐点：串行/submit/map/chunk 四条曲线，别凭直觉开线程池。

## 复盘追问
1. 为什么"加线程池变慢"的工单常见于日志/指标上报？——上报函数微秒级、量巨大，固定成本主导；改批量攒批后吞吐回升。
2. GIL 对这个账有什么影响？——纯 Python 小任务线程池无并行收益，成本账更差；批量化+释放 GIL 的 C 调用才是正解。
