---
title: [Q6079] Django 中间件的 async 演进与 sync/async 适配链
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6079 · Django 中间件的 async 演进与 sync/async 适配链

> 难度:★★★☆ | 标签:版本演进, Django, 中间件, async

**问**：Django 1.10 的 MIDDLEWARE 设置取代 MIDDLEWARE_CLASSES 后，中间件的钩子（process_request/process_view/process_response）与 `__call__` 形态怎么演进？3.1+ 的 `async_capable`/`sync_capable` 双标志机制是什么？一个 sync 中间件混在 ASGI 链路里会发生什么（性能与语义）？`process_exception` 与新式 `__call__` try/except 的关系？

**答**：结论：演进主线是"钩子式 → 可调用式 → 双模式可调用"：a) 1.10 前 `MIDDLEWARE_CLASSES` 靠 process_request/view/response/exception 五个钩子拼装；1.10 起新式中间件就是"工厂函数返回 `__call__(get_response)` 闭包"，请求流是纯函数包裹链，钩子变成可选 sugar；b) 3.1 引入 `async_capable = True/False` + `sync_capable` 类属性：Django 的 handler 会按链路模式（WSGI 全 sync；ASGI 视宿主视图而定的混合模式）**自动适配**——链中遇到不匹配的中间件，用 `SyncToAsync/AsyncToSync`（asgiref）包装转换；c) 混合链的语义陷阱：一个 sync 中间件混进 async 链，它的执行会被丢进**线程池**（`sync_to_async(thread_sensitive=True)` 默认串行化所有 sync 段到同一线程！），性能塌方点就在这里——thread_sensitive 设计是为了保护 Django 的请求级状态（如 locale、connection），代价是 async 链里的 sync 中间件们互相排队（Q6006 线程池耗尽的中间件版）；d) `process_exception` 等价物在新式形态里就是 `__call__` 里的 try/except 包住 `response = get_response(request)`，视图异常在内层抛、中间件层接——但注意 **process_view/exception 的执行时机差异**：钩子式只在 sync 视图前生效点不同，迁移时旧钩子逻辑要逐个重审。迁移清单：`grep process_ ` 找钩子中间件、确认链路模式（WSGI 部署不用管）、ASGI 下把重中间件改写成 async_capable 或拆到边缘层、压测对比 sync 段串行化的吞吐差。

```python
# file: code/03-Web后端开发/q6079_django_middleware.py
import sys, time

# 1) 新式中间件形态: 工厂 -> __call__ 闭包 (1.10+)
class TimingMiddleware:
    sync_capable = True
    async_capable = False            # 关键标志: 决定 Django 是否做适配包装

    def __init__(self, get_response):
        self.get_response = get_response   # 下一段(可能是视图或更内层中间件)

    def __call__(self, request):
        t0 = time.perf_counter()
        response = self.get_response(request)   # try/except 即 process_exception 等价物
        response["X-Timing"] = f"{(time.perf_counter()-t0)*1000:.1f}ms"
        return response

# 2) 双模式中间件: 3.1+ 按链路模式分派 sync/async 路径
class DualModeMiddleware:
    sync_capable = True
    async_capable = True

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.is_async:                     # ASGI 链路(混合模式): 返回协程即可
            return self._async_path(request)
        return self._sync_path(request)

    def _sync_path(self, request):
        return self.get_response(request)

    async def _async_path(self, request):
        return await self.get_response(request)

# 3) sync 中间件混进 async 链的适配成本(asgiref 包装语义演示)
try:
    from asgiref.sync import sync_to_async, async_to_sync

    def sync_only_thing():
        return "sync work"

    a = sync_to_async(sync_only_thing)           # 默认 thread_sensitive=True
    import asyncio
    out = asyncio.run(a())
    print("sync_to_async 包装:", out, "| thread_sensitive=True 时所有 sync 段串行到同一线程")

    # 串行化成本演示: 两个"线程敏感"sync 段不能并发
    async def two_sync_segments():
        t0 = time.perf_counter()
        await asyncio.gather(sync_to_async(lambda: time.sleep(0.1))(),
                             sync_to_async(lambda: time.sleep(0.1))())
        return (time.perf_counter() - t0) * 1000
    print(f"两个 thread-sensitive sync 段 gather: {asyncio.run(two_sync_segments()):.0f}ms (串行=200ms 而非并行 100ms)")
except ImportError:
    print("asgiref 未安装: pip install asgiref (Django 自带依赖)")

# 4) 钩子式(1.10 前)与新式等价关系速记
print("process_request -> __call__ 里 get_response 之前的代码")
print("process_response -> get_response 之后的代码; process_exception -> try/except")
print("python:", sys.version.split()[0])
```

**追问**：1) 为什么 thread_sensitive 要把所有 sync 段串到一个线程？——Django 请求级全局状态（数据库连接绑定线程、locale、cache 绑定）假设"一个请求在一个线程内完成"；ASGI 混合模式下 asgiref 用单一"敏感线程"执行所有 sync 段来保住这个假设，代价是 sync 段全局串行——这是 Django async 化最大的隐性性能税。2) `request.is_async` 在什么链路下为 True？——仅当部署为 ASGI 且该请求走 async 路径；WSGI 部署下永远 sync；混合模式里同一项目可同时服务 sync 视图与 async 视图，中间件必须双标志都声明否则 handler 启动时报 "cannot adapt"。3) 中间件顺序在 async 适配下还可靠吗？——适配包装改变的是执行线程不是顺序，顺序语义保留；但 sync 段串行意味着"内层 async 中间件并发处理请求 A、外层 sync 中间件串行等"，观测到的时序与直觉不同，排查并发问题时要看 anyio/asgiref 的线程模型。

## 背诵要点
- 演进主线：钩子式（1.10 前）→ `__call__` 闭包式（1.10）→ `sync_capable/async_capable` 双模式（3.1）；钩子的新式等价物是 get_response 前后代码与 try/except。
- sync 中间件混进 async 链会被 sync_to_async(thread_sensitive=True) 包装：所有 sync 段串行到同一"敏感线程"，是 Django async 化的最大隐性税。
- WSGI 部署不用管双标志；ASGI 混合模式下链中每个中间件都要能适配，不能适配启动即报错。

## 复盘追问
- 你们 Django 项目的中间件链里有多少 sync 钩子老中间件？ASGI 化后有没有量过敏感线程串行的吞吐损失？（提示：压测对比 WSGI/ASGI 两种部署同一接口的 QPS，把 sync 段耗时加总即串行税上限）
- 如果要做"中间件 async 化"专项，优先级怎么排？（提示：按"每请求耗时×QPS"给中间件排税额，重 IO 的（外部调用）先改 async_capable，纯内存操作留着无害）
