---
title: [Q552] sys.settrace:调试器与覆盖率的原理
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q552 · sys.settrace:调试器与覆盖率的原理

> 难度:★★★★ | 标签:settrace, 调试

**问**:coverage.py 怎么知道执行了哪些行?自己实现一个行级 tracer 要处理什么性能问题?

**答**:sys.settrace(tracer) 安装全局追踪函数:每个新函数调用触发 call 事件,返回局部 trace 函数后每执行一行触发 line 事件(还有 return/exception 事件),事件携带 frame 可读 f_lineno。coverage 的原理就是收集 line 事件的 f_code.co_filename + f_lineno 集合;pdb 单步、seq diag、AST 装饰器工具同源。性能:line 事件每行一次 Python 回调,慢 10-100 倍,所以生产用 C 实现的 sys.monitoring(3.12+)或带开关的采样;全局 tracer 一次只能装一个,第三方库悄悄 settrace 会互相覆盖。

```python
# file: code/01_语言核心与底层/q552_settrace.py
import sys

lines_executed = set()

def tracer(frame, event, arg):
    if frame.f_code.co_filename == __file__:
        if event == "line":
            lines_executed.add(frame.f_lineno)
    return tracer                          # 返回自己:继续逐行追踪

def measured():
    x = 1
    if x > 0:
        y = x + 1
    return y

if __name__ == "__main__":
    old = sys.gettrace()
    sys.settrace(tracer)
    measured()
    sys.settrace(old)

    first = measured.__code__.co_firstlineno
    covered = sorted(l for l in lines_executed if first <= l <= first + 5)
    print("lines of measured():", covered)
    print("total traced lines in file:", len(lines_executed))
```

**追问**:1) 3.12 的 sys.monitoring 强在哪?——按事件类型注册、C 层回调、零包装帧开销,目标就是把 coverage/profiler 的税从数量级降到常数级;settrace 是纯 Python 回调的上一代方案。2) settrace 的开销模式?——每行/每调用一次 Python 回调,数量级 5-10 倍慢,所以只用于调试器与开发期覆盖率;每次回调要拷贝 f_locals,高频路径上成本显著。3) 事件模型?——'call'/'line'/'return'/'exception'/'opcode',全局 trace 返回局部 trace;asyncio/greenlet 的上下文切换会让「当前帧」与直觉不符。4) 生产陷阱?——生产环境开 settrace 或覆盖率(慢且改时序,海森 bug);调试器与 profiler 同时注册互相顶掉;3.12+ 的工具应迁移 sys.monitoring,而不是继续叠 settrace 补丁。
