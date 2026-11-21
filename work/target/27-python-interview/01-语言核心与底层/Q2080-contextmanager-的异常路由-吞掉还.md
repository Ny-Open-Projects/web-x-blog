---
title: [Q2080] contextmanager 的异常路由:吞掉还是放行
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2080 · contextmanager 的异常路由:吞掉还是放行

> 难度:★★★★☆ | 标签:contextmanager, 异常路由, 清理

**问**:@contextmanager 的生成器里,with 体抛出的异常是从哪里进来的?怎么实现「吞掉某些异常」?

**答**:路由机制:with 体抛异常时,contextlib 会对生成器调用 gen.throw(exc),异常在 **yield 表达式处**注入生成器——所以生成器里把 yield 包进 try/except 就能拦截 with 体的异常。关键语义在于是否重新抛出:except 捕获后不 raise,生成器正常走到结尾,contextmanager 视为 __exit__ 返回 True,异常被抑制,with 体之后的代码继续执行;不捕获(或捕获后又 raise),异常从 yield 处穿出,经 __exit__ 继续向外传播。清理代码必须放 finally——无论吞掉、放行还是无异常,清理都执行,demo 两条路径分别演示。

```python
# file: code/01_语言核心与底层/q2080_cm_exception_route.py
"""@contextmanager 的异常路由:yield 处是被注入异常的入口。"""
import contextlib


@contextlib.contextmanager
def checked(tag):
    print(f"[{tag}] 进入")
    try:
        yield "resource"           # with 体的异常从这里注入生成器
    except ValueError:
        print(f"[{tag}] 捕获 ValueError,选择吞掉")
        # 不重新抛出 == __exit__ 返回 True,异常被抑制
    finally:
        print(f"[{tag}] 清理:无论路由结果如何都执行")


@contextlib.contextmanager
def passing(tag):
    try:
        yield "resource"
    finally:
        print(f"[{tag}] 清理后放行异常")
    # 生成器不吞:异常在 yield 处穿出,继续向外传播


if __name__ == "__main__":
    with checked("吞异常型") as r:
        print("拿到资源:", r)
        raise ValueError("坏值")
    print("with 体之后继续执行,异常没有穿出\n")

    try:
        with passing("放行型"):
            raise KeyError("缺失键")
    except KeyError as e:
        print("异常穿出 with:", e)
```

**追问**:1) yield 放 try 里还是 finally 里有区别吗?——清理写进 finally 才能覆盖「吞掉、放行、无异常」全部路由;想「只抑制特定异常」怎么办?——except 特定类型后 pass,其余异常不捕获自然放行,与 contextlib.suppress 同构(见 Q1819)。2) 异常路由的三种结局?——生成器吞掉(StopIteration→抑制)、原样重抛(继续传播)、抛新异常(带上下文替换)——这正是 contextlib 的核心分支(Q476)。3) yield 位置的语义?——yield 在 try 内:异常注入点在受保护区域,清理在 finally;yield 在 try 外:清理逻辑不会被异常路径执行——这是写 CM 生成器的分水岭。4) 生产陷阱?——yield 写在 try 外漏清理;吞掉 BaseException;清理代码抛错顶掉业务异常(Q526)。
