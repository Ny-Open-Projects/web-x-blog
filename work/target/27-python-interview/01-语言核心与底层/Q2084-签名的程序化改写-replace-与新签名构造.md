---
title: [Q2084] 签名的程序化改写:replace 与新签名构造
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2084 · 签名的程序化改写:replace 与新签名构造

> 难度:★★★★☆ | 标签:inspect, Signature, 包装器

**问**:包装函数时怎么让它对外展示的签名与真实实现不同?Signature.replace 能改什么?

**答**:Signature 是不可变对象,replace(parameters=...) 返回新签名,可以增删参数、改默认值、改 kind(位置/关键字)与注解——这是做 API 门面与参数治理的工程杠杆:把内部参数从对外签名里摘除、把旧位置参数标成 KEYWORD_ONLY 再转发。改完挂到包装函数的 __signature__ 属性上,inspect.signature 与 help() 就按新签名呈现。注意边界:__signature__ 约束的是自省视图,不是运行时强约束——调用方硬传被摘除的 kwargs 仍会透传进真实函数,要真拦截得配合 Signature.bind 校验或显式弹参,demo 里 bind 对 trace 参数抛 TypeError 展示的正是「契约层」的拦截(签名内省基础见 Q497)。

```python
# file: code/01_语言核心与底层/q2084_signature_rewrite.py
"""Signature.replace:程序化构造新签名并挂到包装函数上。"""
import inspect


def query(sql, *, timeout=30, trace=False):
    return sql


def public_wrapper(*args, **kwargs):
    """对外隐藏 trace 参数,内部再补上。"""
    kwargs.setdefault("trace", False)
    return query(*args, **kwargs)


if __name__ == "__main__":
    sig = inspect.signature(query)
    print("原签名:", sig)

    kept = [p for name, p in sig.parameters.items() if name != "trace"]
    public_wrapper.__signature__ = sig.replace(parameters=kept)
    print("包装后对外签名:", inspect.signature(public_wrapper))

    bound = inspect.signature(public_wrapper).bind("select 1", timeout=5)
    print("bind 校验通过:", bound.arguments)

    try:
        inspect.signature(public_wrapper).bind("select 1", trace=True)
    except TypeError as e:
        print("trace 已移出对外契约:", e)
```

**追问**:1) __signature__ 是强约束吗?——只约束自省视图,运行时 kwargs 照样透传,真正拦截要 bind 校验或显式弹参;replace 典型用途?——API 演进时把位置参数改 KEYWORD_ONLY、改默认值、给包装器一个诚实的门面签名。2) replace 的能力面?——逐字段返回新 Signature(参数、返回注解);配合 functools.wraps 给 wrapper 挂 __signature__;C 扩展无签名时手工构造。3) 与 Q497/498 的闭环?——bind 按签名校验实参、replace 改签名、__signature__ 提供视图;三者组成「签名可编程」工具箱。4) 生产陷阱?——改了 __signature__ 但实现不匹配,自省说谎;漏 wraps 后 replace 也救不回元信息;签名演进不配合文档/schema。
