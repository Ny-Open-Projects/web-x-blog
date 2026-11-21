---
title: [Q077] 异步生成器与 async for
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q077 · 异步生成器与 async for

> 难度:★★☆ | 标签:asyncio, 异步生成器

**问**:什么是异步生成器?它和普通生成器的区别?

**答**:在 async def 中使用 yield 即定义异步生成器,用 `async for` 消费,每个 yield 之间可以 await 做 IO。适合逐块产出数据的场景,如分页拉取、逐行读大文件。注意异步生成器不能用 for 直接迭代,关闭时由事件循环调用其 athrow/aclose,常配 `async with aclosing(...)` 或在 finally 中清理。

```python
# file: code/02_并发与网络工程/q077_async_generator.py
import asyncio


async def paginated_fetch(total_pages: int) -> int:
    for page in range(total_pages):
        await asyncio.sleep(0.1)  # 模拟请求一页
        yield page * 100


async def consume() -> None:
    async for item in paginated_fetch(3):
        print("拿到一页数据:", item)


async def main() -> None:
    gen = paginated_fetch(2)
    print("异步生成器对象:", gen)
    await consume()


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:
- 异步生成器和异步迭代器什么关系?——异步迭代器是实现 `__aiter__/__anext__` 的对象;异步生成器是含 yield 的 async def,自动满足异步迭代器协议。
- 异步生成器怎么保证清理执行?——用 `contextlib.aclosing(gen)` 包住 async for,退出时调用 aclose;否则依赖 GC 触发,时机不定。
- 它支持 yield from 吗?——不支持,异步生成器不能 yield from,委托要用 async for 循环转发。

---
