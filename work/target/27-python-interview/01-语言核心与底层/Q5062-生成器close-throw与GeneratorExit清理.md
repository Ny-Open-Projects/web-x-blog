---
title: [Q5062] 生成器 close/throw 与 GeneratorExit 清理
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5062 · 生成器 close/throw 与 GeneratorExit 清理

> 难度:★★★★★ | 标签:原理深挖, 生成器, GeneratorExit, 资源清理

**问**：生成器被 GC 回收时 `close()` 会注入 `GeneratorExit`。为什么在 finally 里 `yield` 会炸出 `RuntimeError: generator ignored GeneratorExit`？`throw()` 与 `close()` 的状态机差异是什么？写带资源清理的生成器有哪些红线？

**答**：结论：生成器挂起点（yield 处暂停）被销毁时，解释器先调 `close()`：在暂停点注入 `GeneratorExit`（继承 `BaseException`，**故意不继承 Exception**，防止业务代码的 `except Exception` 把它吞掉）。生成器在清理路径（try/finally、with 块）里必须"安静退出"：不许再 yield——再 yield 就抛 `RuntimeError: generator ignored GeneratorExit`；也不许吞掉后继续。`throw(exc)` 是"在暂停点抛指定异常"，生成器可以捕获并 yield 新值（throw 会返回这个值，这就是向协程"注入错误"的机制）；`close()` 注入的 GeneratorExit 是单行道，只能清理不能续命。三条红线：a) finally 里禁止 yield/send（清理路径不得产出）；b) `with` 块内暂停的生成器，close 时按正常 with 退出协议跑 `__exit__`，所以释放型资源（文件/锁/连接）放 with 里是对的；c) 生成器若挂在非 yield 点（没启动过），close 直接返回不注入。实战：想保证清理一定执行，用 `with contextlib.closing(gen)` 或显式 `gen.close()`，别指望 GC——CPython 引用计数会及时回收，但 PyPy/循环引用下延迟不确定，跨解释器边界（celery/多线程）必显式关。

```python
# file: code/01_语言核心与底层/q5062_generator_close.py
import sys

def resource_gen(log):
    print("acquire")
    try:
        for i in range(3):
            yield i
    finally:
        print("release")   # close/GC 时执行清理

g = resource_gen(log=None)
print(next(g))          # 0, 挂在第一个 yield
g.close()               # 注入 GeneratorExit -> finally 执行
print("closed ok")

# 1) finally 里 yield: RuntimeError
def bad_gen():
    try:
        yield 1
    finally:
        yield 2         # 清理路径再产出 -> 违规

b = bad_gen()
next(b)
try:
    b.close()
except RuntimeError as e:
    print("ignored GeneratorExit:", e)

# 2) throw: 暂停点注入异常, 生成器可捕获并继续 yield
def resilient():
    total = 0
    while True:
        try:
            x = yield total
        except ValueError as e:
            x = -1      # 吞掉业务异常继续干活
        total += x

r = resilient()
print(next(r))                       # 0
print(r.send(10))                    # 10
print(r.throw(ValueError("bad")))    # 11 (10 + -1)

# 3) GeneratorExit 不被 except Exception 吞
def careful():
    try:
        yield 1
    except Exception:
        yield "swallowed"        # 不会命中: GeneratorExit 是 BaseException
    finally:
        print("cleanup done")

c = careful()
next(c)
c.close()
print("BaseException 设计生效")
print(sys.version_info[:2])
```

**追问**：1) 为什么 GeneratorExit 继承 BaseException 而不是 Exception？——防止生成器内部宽泛的 `except Exception` 清单误吞关闭信号导致清理路径变成业务路径；同理 KeyboardInterrupt/SystemExit 也继承 BaseException。2) async generator 的 aclose 语义有什么不同？——必须 await `aclose()`，且清理路径里可以 await（async with/async for）；事件循环 shutdown_asyncgens 兜底遍历挂起的 agen，但嵌套对象持有时不保证及时，fastapi 依赖的 yield 依赖 teardown 依赖这个机制（另见 03 类）。3) 生成器没启动就 close 会怎样？——没挂起就无注入点，close 直接把状态置 CLOSED，不执行任何清理代码——所以"清理必须挂在 try/finally 里且至少 next 过一次"是契约前提。

## 背诵要点
- close() 在 yield 暂停点注入 GeneratorExit（继承 BaseException 防被 except Exception 吞），finally 里再 yield 抛 `generator ignored GeneratorExit`。
- throw(exc) 在暂停点注入异常且可被捕获继续 yield（协程注入错误机制）；GeneratorExit 单行道只能清理。
- 别指望 GC 做清理：显式 close()/contextlib.closing；finally 禁 yield 是红线，未启动的生成器 close 不跑清理。

## 复盘追问
- 你们管道类代码里生成器是否都显式关闭？有没有依赖进程退出"顺带"释放连接/文件的隐性假设？（提示：找 yield 挂起后路径被丢弃的代码，演练 PyPy/循环引用下的延迟）
- 有没有 finally 里 yield/await 的写法混进生产？（提示：AST 扫描 Finally 节点下的 Yield/Await；对照三条红线逐条过）
