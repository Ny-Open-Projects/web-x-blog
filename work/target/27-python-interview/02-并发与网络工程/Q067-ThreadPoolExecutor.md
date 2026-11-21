---
title: [Q067] ThreadPoolExecutor
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q067 · ThreadPoolExecutor

> 难度:★★☆ | 标签:concurrent.futures, 线程池

**问**:ThreadPoolExecutor 相对手动 Thread 的优势?submit 和 map 的区别?

**答**:线程池复用线程、统一管理生命周期,返回 Future 对象,可拿结果、异常和回调。`submit` 逐个提交,立即返回 Future,可乱序取结果;`map` 按提交顺序阻塞式产出结果,写法简洁。务必用 with 管理池,退出时自动 shutdown(wait=True)。

```python
# file: code/02_并发与网络工程/q067_thread_pool.py
import time
from concurrent.futures import ThreadPoolExecutor


def fetch(url: str) -> str:
    time.sleep(0.2)  # 模拟网络请求
    return f"内容 of {url}"


if __name__ == "__main__":
    urls = [f"https://example.com/page{i}" for i in range(5)]

    with ThreadPoolExecutor(max_workers=3) as pool:
        # map: 按顺序返回
        for result in pool.map(fetch, urls):
            print("map:", result)

        # submit: 返回 Future, 可乱序处理
        futures = [pool.submit(fetch, u) for u in urls]
        for fut in futures:
            print("submit:", fut.result(timeout=5))
```

**追问**:
- submit 和 map 怎么选?——要逐个 Future、自定义异常与重试用 submit;简单批量按序消费用 map,注意 map 迭代中遇异常会中断。
- shutdown(wait=False) 会怎样?——不再接新任务但已提交的继续执行;Python 3.9+ 的 `cancel_futures=True` 能清空未开始的任务,收尾更快。
- Future 的异常什么时候暴露?——只有调用 result()/exception() 或在回调里检查才可见;不观察的失败就是静默失败。

---
