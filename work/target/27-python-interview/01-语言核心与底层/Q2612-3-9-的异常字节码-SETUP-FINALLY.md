---
title: [Q2612] 3.9 的异常字节码:SETUP_FINALLY 与块栈
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2612 · 3.9 的异常字节码:SETUP_FINALLY 与块栈

> 难度:★★★★☆ | 标签:字节码, 异常, dis

**问**:3.9 里 `try/except/finally` 编译成什么样的字节码?为什么说它的异常处理不是零成本的?

**答**:3.9 用「块栈」实现异常处理:进入 try 时执行 `SETUP_FINALLY` 往内部块栈压一个记录,正常离开要 `POP_BLOCK`,捕获时要 `DUP_TOP` 复制异常、`JUMP_IF_NOT_EXC_MATCH` 做类型匹配、`POP_EXCEPT` 清块栈,finally 通过同一机制在块栈里挂清理入口,重抛用 `RERAISE`。这套结构的代价是:即使没有异常发生,进出 try 也要执行压栈弹栈两条指令——不像 3.11 的异常表方案把正常路径变成零开销。读懂这段字节码对排查很有用:比如 `finally` 里的 return 会提前 `RETURN_VALUE` 并吞掉挂起的异常,在字节码层面一目了然。

```python
# file: code/01_语言核心与底层/q2612_try_bytecode.py
"""3.9 的异常处理块栈:SETUP_FINALLY 到 RERAISE 的完整链路。"""
import dis


def tri(x):
    try:
        v = int(x)
    except ValueError:
        v = 0
    finally:
        print("done")
    return v


if __name__ == "__main__":
    tri("42")
    tri("x")
    dis.dis(tri)
```

**追问**:1) 3.11 的零成本异常改变了什么?——编译期生成静态异常表,正常路径不再有任何 SETUP/POP 指令,try 的常量开销归零,匹配异常改由表驱动跳转。2) 3.9 块栈的机制?——SETUP_FINALLY/POP_BLOCK 维护运行时块栈,进入 try 即付指令成本;异常表时代这些指令消失(Q1260 的故事);traceback 行号改由 linetable 提供。3) 与「异常做控制流」的关系?——3.11+ 的 EAFP 在热路径上不再有 try 税;真正抛异常仍贵(构造 traceback);跨版本性能结论要分开测。4) 生产陷阱?——按 3.9 的「try 有开销」写 if-else 优化;3.10- 部署仍是块栈;依赖异常字节码细节的 hack。
