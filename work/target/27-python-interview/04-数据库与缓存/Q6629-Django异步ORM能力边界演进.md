---
title: [Q6629] Django ORM 异步能力的边界演进（4.2→5.1）与迁移点
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6629 · Django ORM 异步能力的边界演进（4.2→5.1）与迁移点

难度：P6 ｜ 标签：版本演进 / Django / 异步

**问**：Django 从 4.2 到 5.1/5.2，异步 ORM 一直在"逐步解锁"。项目想全异步化（ASGI + async views），为什么直接把 `objects.get()` 换成 `.aget()` 并不等于真异步？哪些路径仍是"线程池模拟"，升级时要注意什么破坏点？

**答**：
- **结论**：Django 的异步 ORM 是**适配层演进**：3.0 起 async views，4.1 起 aget/acreate 等单对象异步接口——但底层仍是 `sync_to_async`（线程池包一层同步 ORM，SynccToAsync 的 thread_sensitive 模式），4.2 补齐 QuerySet 迭代（aiter）、流式与部分关系接口，5.0-5.1 继续"逐个方法转原生"。所以换 `aget()` 后事件循环不再被阻塞（它跑在线程池里），**并没有减少数据库连接占用、没有带来 IO 多路复用**——真并发的收益来自"多个请求各自的线程池任务并行"，而不是一条连接上的非阻塞 IO。升级破坏点集中在：① `DJANGO_ASYNC_UNSAFE` 环境下在事件循环里直接调同步 ORM 会抛错（4.x 起的保护），混写代码上线才炸；② 事务边界——`atomic` 是同步上下文，异步视图里要用 `connection.aexecute` 配套的异步事务封装，跨事务的 async 接口调用有隐式断连语义；③ 自定义 manager/QuerySet 方法要自己补 `a` 前缀版本，否则静默退回线程池路径且没有告警。
- **取舍**：全异步化还是"async views + 同步 ORM"？收益判断标准：应用是 IO 密集且并发连接数是容量瓶颈（Q7584 连接账）→ 全异步值得做；CPU 密集或 DB 单点已饱和 → 异步化不解决瓶颈，先做连接池与慢查询治理。线程池模拟路径有上限：默认 threadpool 大小（通常 40 左右）就是异步视图的隐形并发天花板，超过后排队——这与"异步解放连接"的直觉相反。
- **实战**：① 迁移按"视图层 → 管理命令 → 中间件"顺序，单对象 API（aget/acreate/afirst）收益最直接先迁；② 用 `djago` 5.x 的 `async_unsafe` 检测 + 测试套件强制跑 ASGI 客户端，抓混写；③ 给自定义 QuerySet 方法建立"a 前缀必须存在"的 CI 检查；④ 监控线程池队列长度（all_threadpool 饱和即假异步信号）。

```python
# Django 异步 ORM 本质: sync_to_async 线程池适配层, 并发上限=线程池大小
# 基线: Python 3.9+ 标准库 (演示用线程池模拟 Django 的适配语义)
import time
from concurrent.futures import ThreadPoolExecutor


class FakeThreadpoolAdapter:
    """Django sync_to_async(thread_sensitive=True) 的简化模型:
    所有异步 ORM 调用排进同一个 worker, 串行执行。"""

    def __init__(self, db_latency_s: float = 0.05):
        self.pool = ThreadPoolExecutor(max_workers=1)  # thread_sensitive
        self.db_latency_s = db_latency_s

    async def aget(self, pk: int) -> str:
        import asyncio
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(self.pool, self._sync_get, pk)

    def _sync_get(self, pk: int) -> str:
        time.sleep(self.db_latency_s)              # 模拟 DB 同步调用
        return f"row:{pk}"


async def fetch_many(adapter: FakeThreadpoolAdapter, n: int) -> float:
    import asyncio
    t0 = time.monotonic()
    await asyncio.gather(*(adapter.aget(i) for i in range(n)))
    return time.monotonic() - t0


def main() -> None:
    import asyncio
    adapter = FakeThreadpoolAdapter(0.05)
    elapsed = asyncio.run(fetch_many(adapter, 10))
    # 线程池串行: 10 个并发 aget = 10 x 50ms, 并不并行
    assert abs(elapsed - 0.5) < 0.2, elapsed
    print(f"10 个并发 aget 耗时 {elapsed:.2f}s (串行 0.5s, 非真异步多路复用)")
    print("OK: aget 只是线程池适配, 连接占用不变; 真并发上限=线程池大小")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么说 `thread_sensitive=True` 让所有异步 ORM 调用串行化？这对"异步化提升并发"意味着什么？
→ 一句话提示：thread_sensitive 模式复用单个执行上下文保证请求局部数据一致（request 对象不能跨线程），代价是 DB 调用互相排队——异步化的收益主要是"不阻塞事件循环"，吞吐提升取决于线程池配置，不是 IO 多路复用。

**追问 2**：自定义 Manager 方法没有 a 前缀版本时会发生什么？怎么在 CI 抓住？
→ 一句话提示：async 视图里调用会静默走 sync_to_async 退化路径（功能对但假异步），测试环境开 DJANGO_ASYNC_UNSAFE 才报错——CI 加"每个自定义方法必须有 a 版本"的静态检查是唯一可靠闸门。

## 背诵要点
- Django 异步 ORM 是 sync_to_async 线程池适配层演进（3.0 视图 → 4.1 单对象 API → 4.2 迭代/流式 → 5.x 逐步原生），aget 不减连接占用、非 IO 多路复用。
- thread_sensitive 模式下调用串行，线程池大小是假异步并发天花板；async_unsafe 保护上线才炸混写代码。
- 全异步化的判据：IO 密集 + 连接数瓶颈；CPU 密集或 DB 饱和先做池化与慢查询治理。

## 复盘追问
- 怎么区分"真异步 ORM 路径"和"线程池退化路径"？提示：看调用是否命中原生异步实现（官方 a 前缀全集）还是被 sync_to_async 包裹——用 trace 工具看线程切换即可判别。
- 异步视图里事务边界最容易踩什么？提示：同步 atomic 块里 await 其他异步操作会把事务窗口拉长且上下文不一致，必须用配套异步事务封装并让所有 DB 操作都在其内部。
