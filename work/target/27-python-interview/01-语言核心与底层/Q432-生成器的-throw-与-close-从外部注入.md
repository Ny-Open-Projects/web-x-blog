---
title: [Q432] 生成器的 throw 与 close:从外部注入异常
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q432 · 生成器的 throw 与 close:从外部注入异常

> 难度:★★★☆ | 标签:生成器, 异常

**问**:generator 的 throw 和 close 各自在什么位置抛异常?生成器可以「接住」它们吗?

**答**:`throw(exc)` 在生成器当前挂起的 yield 处抛出异常,等于从内部那个 yield 点把异常炸出来;生成器可以用 try/except 捕获它,捕获后继续 yield 就还能继续使用,异常于是成为「带外控制信号」。`close()` 是语法糖:在 yield 处抛 GeneratorExit,正常情况下生成器执行 finally/清理后退出,close 返回 None。两者都要求生成器已启动,否则没有挂起点可操作。

```python
# file: code/01_语言核心与底层/q432_generator_throw_close.py
def worker():
    try:
        while True:
            item = yield "ready"
            print("got", item)
    except ValueError as e:
        print("injected:", e)
        yield "recovered"             # 捕获后还能吐出新值继续用
    finally:
        print("cleanup in finally")

if __name__ == "__main__":
    g = worker()
    print(next(g))                          # 预激,得到 ready
    print(g.throw(ValueError("boom")))      # 在 yield 处注入,生成器捕获后返回 recovered
    try:
        g.send("hello")                     # recovered 之后的 yield 没有:except 块结束进 finally
    except StopIteration:
        print("finally ran, generator finished")

    g2 = worker()
    next(g2)
    g2.close()                              # 注入 GeneratorExit,只走 finally
    print("closed cleanly")
```

**追问**:1) close 时生成器如果又 yield 了新值会怎样?——协议禁止:会抛 RuntimeError "generator ignored GeneratorExit",因为关闭语义要求生成器必须退出。2) throw 与 close 的本质区别?——throw 注入任意异常由生成器决定接不接,close 固定注入 GeneratorExit 且协议强制退出;close 本质是 throw(GeneratorExit) 再加「不允许再 yield」的状态检查。3) return 与 StopIteration 什么关系?——生成器 return v 等价于 raise StopIteration(v),yield from 靠 StopIteration.value 接住子生成器返回值,这是委托链层层回传结果的地基。4) 生产陷阱?——用 throw 做「带外控制信号」时协议没有文档化,维护者不知道异常会被捕获继续运行;控制流异常要定义专用类型并写明契约。
