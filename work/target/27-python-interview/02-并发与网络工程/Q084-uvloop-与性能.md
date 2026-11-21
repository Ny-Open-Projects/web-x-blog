---
title: [Q084] uvloop 与性能
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q084 · uvloop 与性能

> 难度:★★☆ | 标签:uvloop, 事件循环, 性能

**问**:uvloop 是什么?为什么快?有什么限制?

**答**:uvloop 是基于 libuv 的 asyncio 事件循环替代实现,把 selector、定时器、回调调度全部下沉到 C 层,吞吐和延迟通常比默认循环好 2-4 倍。用法是 `uvloop.install()` 或把 EventLoopPolicy 传入 asyncio.run。限制:只支持 Unix 平台(macOS/Linux),Windows 不可用;它是标准循环的替代品,API 完全兼容,代码无需改动。

```python
# file: code/02_并发与网络工程/q084_uvloop.py
import asyncio
import time


async def workload(n: int) -> int:
    total = 0
    for i in range(n):
        await asyncio.sleep(0)  # 频繁让出, 压测循环调度
        total += i
    return total


async def bench(label: str) -> None:
    start = time.perf_counter()
    await asyncio.gather(*(workload(2000) for _ in range(100)))
    print(f"{label} 耗时 {time.perf_counter() - start:.2f}s")


def run_with_uvloop() -> None:
    try:
        import uvloop  # 第三方库, 未安装则跳过演示
    except ImportError:
        print("uvloop 未安装, 跳过 (pip install uvloop)")
        return
    uvloop.install()
    asyncio.run(bench("uvloop"))


if __name__ == "__main__":
    asyncio.run(bench("默认事件循环"))
    run_with_uvloop()
```

**追问**:
- uvloop 为什么快?——libuv 把 selector、定时器、缓冲管理下沉到 C,减少 Python 层对象操作与系统调用开销,并发模型本身没变。
- 生产上启用要注意什么?——API 兼容但调试特性与堆栈信息略有差异;预发压测对比、灰度开启、保留环境变量开关可回退。
- 怎么和现有框架组合?——脚本用 `uvloop.run(main)`;uvicorn/FastAPI 用 `--loop uvloop` 或 UvicornWorker,配置一行完成。

---
