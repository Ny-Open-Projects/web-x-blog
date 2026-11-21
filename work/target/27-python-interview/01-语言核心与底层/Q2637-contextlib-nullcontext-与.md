---
title: [Q2637] contextlib.nullcontext 与 closing:占位与收尾的两个小工具
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2637 · contextlib.nullcontext 与 closing:占位与收尾的两个小工具

> 难度:★★☆☆☆ | 标签:contextlib, 资源管理, 设计模式

**问**:一个函数有时有上下文有时没有,怎么避免两套 with 分支?

**答**:`contextlib.nullcontext` 是「什么都不做」的上下文管理器,可选资源场景的万能占位:有锁就用 `lock`,没有就给 `nullcontext()`,主流程只有一条 with;它还能带值(`nullcontext(42)` 进 as),用于「可选默认值」的统一。`contextlib.closing` 补另一半:对象有 `close()` 但不是上下文管理器(老式句柄、第三方对象),closing 负责退出时兜底 close。两者都让「控制流归一」:调用方不必知道资源是否存在,异常路径的清理也由 with 结构保证。搭配 ExitStack(见 Q448)可把任意多个可选资源摊平成一组 with。

```python
# file: code/01_语言核心与底层/q2637_nullcontext_closing.py
"""nullcontext 占位与 closing 收尾:控制流归一。"""
import contextlib


class OldHandle:
    """有 close 但不是上下文管理器的老式对象。"""

    def __init__(self):
        self.closed = False

    def close(self):
        self.closed = True
        print("    OldHandle.close 被调用")


def work(lock):
    """lock 可为 None:nullcontext 统一分支。"""
    with contextlib.nullcontext() if lock is None else lock:
        return "done"


def use_handle():
    with contextlib.closing(OldHandle()) as h:
        return h


if __name__ == "__main__":
    print("带锁:", work(contextlib.nullcontext()))
    print("无锁:", work(None))

    h = use_handle()
    print("退出 with 后 closed =", h.closed)

    with contextlib.nullcontext(42) as v:
        print("nullcontext 带值:", v)
```

**追问**:1) nullcontext 支持重入吗?——支持,它每次进入原样返回构造时的值,可同时用于多个 with,没有状态冲突。2) 两工具的定位?——nullcontext:可选上下文的占位(配置开关时有/无真实 CM 统一写法);closing:只要 close 不要 with 体值(x.close() 兜底);两者都是「接口占位」让代码无分支。3) 与 ExitStack 的组合?——动态选择 CM(None→nullcontext)后统一进栈(Q448);closing 处理非 CM 资源(fd/socket)。4) 生产陷阱?——nullcontext 返回值被误用;closing 的对象没有 close 也会被调用(要求有);占位 CM 掩盖「忘了真资源」的 bug。
