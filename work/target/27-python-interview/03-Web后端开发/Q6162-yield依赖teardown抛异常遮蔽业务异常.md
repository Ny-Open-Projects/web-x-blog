---
title: "[Q6162] yield 依赖 teardown 抛异常遮蔽业务异常"
date: 2026-11-23
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6162 · yield 依赖 teardown 抛异常遮蔽业务异常

难度：P7 ｜ 标签：yield 依赖、异常链、finally、根因遮蔽、事故复盘

**问**：`yield` 依赖里 `try: yield resource finally: cleanup()`，如果请求处理抛出业务异常、而 `finally` 的清理又抛了异常，调用方最终拿到的是哪个？为什么业务异常"消失"了、只留在 `__context__` 里？这和 Q6002/Q6092 讲的"取消时 finally 是否执行"是同一类问题吗？如何设计 teardown 才能既记录清理失败又不掩盖根因？

**答**：
结论：最终抛出的是 **`finally` 里那个清理异常**，业务异常被降级到新异常的 `__context__`（异常链上游）——这是 Python 异常语义的必然：在同一 `try/finally` 中，`finally` 的 `raise` 会替换正在传播的异常，解释器把被替换者挂到 `__context__`。对 FastAPI 依赖而言，`yield` 之后的 teardown 生成器在上下文管理器退出时执行，所以"业务抛 `ValueError` → teardown 抛 `RuntimeError`"时，客户端/上层捕获到的是 `RuntimeError`，日志里只看到"清理失败"，真正的根因 `ValueError` 藏在 `e.__context__`——这就是**根因遮蔽**。与 Q6002/Q6092 不同：那两题关心"取消到达时 finally 在哪个时机跑、能否再 await"；本题关心"清理阶段抛异常时谁的异常胜出"——一个管时序，一个管异常优先级。

取舍：teardown 的黄金律是"**清理失败只记录、不抛出，除非没有正在传播的业务异常**"。实现上用 `try/finally` 内再包一层 `try/except`，把清理异常写入日志/指标/错误列表，让业务异常原样透传；若确实要把"清理失败"暴露给调用方，用 `ExceptionGroup` 或 `add_note()` 附带信息，而不是 `raise` 替换。对数据库事务依赖尤其重要——`finally` 里 `commit()` 失败若覆盖了业务层的 `IntegrityError`，排查会完全跑偏。

实战：事故形态是"下单接口报 'connection close failed'，但真正原因是库存校验失败；日志里只有连接关闭错误"——排查第一步就是打印 `e.__context__`。下面用 stdlib `contextmanager` 把"遮蔽"和"安全 teardown"两种写法跑出来，并展示异常链。

```python
from contextlib import contextmanager

# 1) 危险写法：finally 抛异常，业务异常被降级到 __context__
@contextmanager
def bad_dep():
    try:
        yield "conn"
    finally:
        raise RuntimeError("cleanup failed")

try:
    with bad_dep():
        raise ValueError("business error: stock check")
except BaseException as e:
    print("BAD caught :", type(e).__name__, "-", e)
    print("  context  :", type(e.__context__).__name__, "-", e.__context__)

# 2) 安全写法：清理失败记录但不抛，业务异常原样透传
@contextmanager
def safe_dep(errors):
    try:
        yield "conn"
    finally:
        try:
            raise RuntimeError("cleanup failed")
        except RuntimeError as ce:
            errors.append(ce)                 # 记录，不替换业务异常

errors = []
try:
    with safe_dep(errors):
        raise ValueError("business error: stock check")
except BaseException as e:
    print("SAFE caught:", type(e).__name__, "-", e)
    print("  cleanup logged:", len(errors), "-", errors[0])

# 3) 无业务异常时，清理失败仍可被上报（此时没有东西可遮蔽）
errors2 = []
with safe_dep(errors2):
    pass
print("cleanup-only:", len(errors2), "-", errors2[0])
```

**追问一**：为什么 `__context__` 而不是 `__cause__`？——`__context__` 是解释器在异常自动传播时**隐式**设置的上游异常（"在 handling A 时发生了 B"）；`__cause__` 只由显式 `raise B from A` 设置，表达"我明确知道 B 由 A 引起"。`finally` 里直接 `raise` 属于前者，所以根因进 `__context__`；若你在 teardown 里写 `raise CleanupError from original`，则进 `__cause__`——但前提是你能拿到 original（通常拿不到，它在生成器内部传播）。

**追问二**：`ExceptionGroup` 能解决 teardown 遮蔽吗？——能表达"业务异常 + 清理异常同时存在"，但你必须在 teardown 里拿到业务异常对象才能把它放进组里——而标准 `yield` 依赖的结构里，业务异常是"穿过 yield 点传播"的，生成器可以在 `except BaseException as e:` 里捕获它、再 `raise ExceptionGroup("req", [e, cleanup_err])`。这比"记录日志"更结构化，但改变了上层捕获类型（要 `except*`），迁移成本高；团队通常选"日志 + 指标记录清理失败"这种低侵入方案。

## 背诵要点
- `finally` 里的 `raise` 会替换正在传播的业务异常，根因降级到 `__context__`（不是 `__cause__`，后者要 `raise ... from`）。
- teardown 黄金律：清理失败只记录不抛（日志/指标/errors 列表），业务异常原样透传；无业务异常时才上报清理失败。
- 与 Q6002/Q6092 区分：那两题管取消时 finally 的时机，本题管清理异常的优先级；可用 ExceptionGroup/add_note 结构化附带但迁移成本高。

## 复盘追问
- 下单接口报"连接关闭失败"但根因是库存校验失败，如何用异常链定位并修复 teardown？（打印 `__context__`、清理失败只记录不抛、讨论 ExceptionGroup 的代价）
- 为什么 `__context__` 里的异常不能指望被上层 `except ValueError` 捕获？（正在传播的是替换后的 RuntimeError，讨论异常链只是信息而非控制流）
