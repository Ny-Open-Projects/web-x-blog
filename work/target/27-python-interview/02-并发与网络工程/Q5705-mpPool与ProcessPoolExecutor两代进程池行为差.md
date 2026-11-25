---
title: "[Q5705] mp.Pool 与 ProcessPoolExecutor：两代进程池的行为差"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5705 · mp.Pool 与 ProcessPoolExecutor：两代进程池的行为差

难度：P6 ｜ 标签：multiprocessing.Pool、ProcessPoolExecutor、map、chunksize、异常传播、terminate

**问**：代码里同时见过 `multiprocessing.Pool` 和 `concurrent.futures.ProcessPoolExecutor`，两者都是进程池，迁移时要注意什么？`pool.map` 和 `executor.map` 在异常传播和结果产出时机上的差异是什么？为什么一个报错会立刻抛、另一个能先拿到部分结果？`terminate()` 和 `shutdown(cancel_futures=True)` 分别怎么关门？

**答**：
结论：`mp.Pool` 是 multiprocessing 时代的老 API，`ProcessPoolExecutor` 是 concurrent.futures 的现代 API（3.7+ 起行为对齐更稳）。核心差异有三：a) **异常与结果产出时机**——`executor.map` 返回惰性迭代器，按输入顺序逐个产出结果，迭代到出错的位置才抛异常，之前的正常结果已经拿到手；`pool.map` 是急切收集，任何子任务失败后整批抛出，一次失败毁掉整批结果。b) **关门方式**——`Pool.terminate()` 立刻杀 worker（可能有任务被腰斩），`Pool.close()+join()` 才是温和排空；Executor 只有 `shutdown(wait=True, cancel_futures=True)`，语义上是"取消排队任务+等在途任务"，没有硬杀档位。c) **chunksize**——`pool.map` 支持 chunksize 把任务打包发 worker 减少通信次数（大任务量小计算时显著），`executor.map` 没有这个概念（每任务一次提交）。

取舍：a) 新代码默认 `ProcessPoolExecutor`：接口统一（与线程池一致）、异常语义更细、与 `asyncio.run_in_executor` 无缝；b) `mp.Pool` 仅在依赖 `imap_unordered`、`chunksize`、`apply_async` 回调这套老生态时保留；c) 迁移陷阱：`pool.map` 出错即抛的行为变成 `executor.map` 的"迭代中途抛"，调用方要处理"已经拿到的部分结果"；d) 大量微小任务用 Executor 会放大提交开销，这是 `mp.Pool` chunksize 仍然占优的场景；e) 两代的任务函数都必须可 pickle 且模块级可见，spawn 启动方式下还要保证子进程能重新 import 主模块。

实战：事故形态是"从 mp.Pool 迁到 Executor 后，批处理脚本把 `pool.map` 的整批 try/except 换成 `for r in ex.map(...)`，坏数据在第 1000 条抛异常，前 999 条结果没落库就崩了，重跑又从头来；修复是迭代器逐条 try/except 落库 + 失败清单，把部分成功显式化"。下面对比两代 map 在"最后一个任务失败"时的产出差异。

```python
import multiprocessing as mp
import time
from concurrent.futures import ProcessPoolExecutor


def work(i):
    time.sleep(0.05 * (5 - i))          # 后面的任务先完成
    if i == 4:
        raise ValueError("boom-4")
    return i * i


def pool_version():
    pool = mp.Pool(2)
    try:
        return ("pool.map", pool.map(work, range(5)))
    except ValueError as e:
        return ("pool.map 一次性抛出", str(e))
    finally:
        pool.terminate()


def executor_version():
    out = []
    with ProcessPoolExecutor(2) as ex:
        try:
            for r in ex.map(work, range(5)):
                out.append(r)
        except ValueError as e:
            return ("executor.map 已先产出", out, "随后抛", str(e))
    return out


if __name__ == "__main__":
    print("[1]", pool_version())
    print("[2]", executor_version())
```

**追问一**：`executor.map` 已经产出 4 个结果后抛异常，剩下没跑的任务还会继续执行吗？—— 会。map 只是提交了全部任务并按序转发结果，迭代器中途抛异常不会自动取消在途/排队的任务；主循环抛出后 task 仍在 worker 里跑完。要真正止损得自己记录 Future 并 `executor.shutdown(cancel_futures=True)`，或者把 map 拆成 submit + 分批管理。这和 `asyncio.gather` 中途异常不取消兄弟任务是同一个模式：聚合器失败不等于成员任务取消。

**追问二**：`Pool.terminate()` 与 `Executor.shutdown(cancel_futures=True)` 的语义差在什么场景会咬人？—— `terminate()` 是硬杀：worker 直接被 SIGTERM/关闭管道，正在执行的任务没有清理机会，适合"上游已确认失败，尽快止血"；Executor 没有 kill 档位，`shutdown(wait=True)` 会等在途任务自然结束，如果某个任务卡死（网络不设超时），整个 shutdown 就挂住。所以迁到 Executor 后必须给每个任务自己加超时（子进程内部超时或外部超时 + 强杀整池），"优雅关闭"依赖任务本身可中断。

## 背诵要点
- `executor.map` 惰性逐个产出、迭代到坏位才抛，部分结果可救；`pool.map` 急切收集、整批抛。
- `Pool.terminate()` 硬杀 vs `close()+join()` 温和；Executor 只有 `shutdown(cancel_futures=True)`，无硬杀档。
- `pool.map` 的 chunksize 是微小任务场景的通信优化；Executor 无 chunksize，微小任务提交开销放大。

## 复盘追问
- 迁到 executor.map 后第 1000 条坏数据炸了，前 999 条结果去哪了？（迭代器已产出，调用方没落库就崩）
- executor.shutdown 遇到卡死任务会怎样？（wait=True 等在途任务，无 kill 档，需任务自带超时）
