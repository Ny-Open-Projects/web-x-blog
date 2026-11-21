---
title: [Q068] ProcessPoolExecutor
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q068 · ProcessPoolExecutor

> 难度:★★☆ | 标签:concurrent.futures, 进程池

**问**:ProcessPoolExecutor 和 multiprocessing.Pool 该用哪个?有什么坑?

**答**:新代码推荐 ProcessPoolExecutor:API 与线程池一致,便于在池间切换。坑:提交的函数与参数、返回值都必须可 pickle;函数必须是模块顶层定义(lambda 和闭包会报错);Windows/macOS 的 spawn 启动要求主模块有 `if __name__ == "__main__":` 保护;某任务抛异常会在 result() 时重新抛出。

```python
# file: code/02_并发与网络工程/q068_process_pool.py
import math
from concurrent.futures import ProcessPoolExecutor


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def count_primes(limit: int) -> int:
    return sum(1 for n in range(limit) if is_prime(n))


if __name__ == "__main__":
    limits = [100_000, 150_000, 200_000, 250_000]
    with ProcessPoolExecutor(max_workers=4) as pool:
        for limit, count in zip(limits, pool.map(count_primes, limits)):
            print(f"<{limit} 的素数个数: {count}")
```

**追问**:
- lambda 为什么不能提交给进程池?——pickle 按模块限定名序列化函数,lambda/闭包没有可导入名字;必须用模块顶层 def。
- worker 卡死怎么办?——`future.result(timeout=...)` 有限等待,但卡死的 worker 杀不掉,只能重建池;`max_tasks_per_child`(3.11+)可按任务数回收进程防内存膨胀。
- 池大小怎么定?——默认 os.cpu_count();IO 混合可放宽,但进程内存开销大,通常不超过 2 倍核,配合压测确认。

---
