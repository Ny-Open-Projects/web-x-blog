---
title: [Q2643] 保存异常对象的后患:__traceback__ 引用链与内存滞留
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2643 · 保存异常对象的后患:__traceback__ 引用链与内存滞留

> 难度:★★★★☆ | 标签:内存泄漏, traceback, 引用链

**问**:把 except 里的异常对象存进列表做「错误收集」,为什么会内存泄漏?

**答**:异常对象的 `__traceback__` 指向整条帧链:每一帧又持有其局部变量,于是「一个错误对象」实际钉住了抛出路径上所有函数的全部局部状态——大列表、大 buffer 全部滞留。实测:在抛异常的帧里造一个大对象,用弱引用观察,只要异常对象活着它就不被回收,`del` 异常对象后立刻回收。规则有三:except 块结束后 `sys.exc_info()` 会被清空,但**自己存下来的引用不会**;必须长期保存错误时,保存提炼后的信息(类型、消息、格式化后的 traceback 字符串)而不是异常对象本身;确需保留对象,至少 `exc.__traceback__ = None` 掐断帧链。这与 Q1294 的隐式 del 是同一机制的两面。

```python
# file: code/01_语言核心与底层/q2643_traceback_retention.py
"""保存异常对象会钉住整条帧链的局部变量。"""
import gc
import weakref


class Payload:
    pass


def failing():
    payload = Payload()                 # 大对象,本函数结束后应可回收
    marker = weakref.ref(payload)
    try:
        raise ValueError("boom")
    except ValueError as exc:
        return exc, marker


if __name__ == "__main__":
    exc, marker = failing()
    gc.collect()
    print("异常对象活着时,帧内 payload 仍被钉住:", marker() is not None)

    exc.__traceback__ = None            # 掐断帧链
    gc.collect()
    print("掐断 __traceback__ 后回收:", marker() is None)

    # 对照:保存提炼信息才是长存姿势
    exc2, marker2 = failing()
    brief = f"{type(exc2).__name__}: {exc2}"
    del exc2
    gc.collect()
    print("只存摘要后可回收:", marker2() is None, "| 摘要:", brief)
```

**追问**:1) traceback.format_exc 之后再删异常还有风险吗?——格式化字符串只含文本,与帧链脱钩,是安全的;风险全部来自对异常对象本身的存活引用。2) __traceback__ 引用链的机制?——异常对象持 tb 链,tb 每帧持 frame,frame 持局部变量——一个没处理的异常对象把整条调用链钉在内存(Q1256);全局 list 存异常对象是经典泄漏。3) 正确姿势?——格式化成文本后丢弃对象;需要结构化信息提取 e.args/属性后丢弃;聚合错误用文本/摘要而不是对象列表。4) 生产陷阱?——errors.append(e) 的全局收集器;日志系统缓存异常对象;pytest last failed 之外的插件长期持有。
