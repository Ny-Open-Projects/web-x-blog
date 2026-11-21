---
title: [Q497] inspect.signature:签名内省
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q497 · inspect.signature:签名内省

> 难度:★★★☆ | 标签:inspect, 函数

**问**:运行时如何知道一个函数接受哪些参数、哪些是关键字-only、默认值是什么?

**答**:inspect.signature(func) 返回 Signature,其 parameters 是有序字典,每个 Parameter 带 name、kind(POSITIONAL_ONLY/POSITIONAL_OR_KEYWORD/KEYWORD_ONLY/VAR_POSITIONAL/VAR_KEYWORD)、default(缺省哨兵 empty)。在此基础上能做:参数校验(见 Q445)、生成 API 文档、构建通用代理与适配器。配套 bind/apply_defaults 把实参归一化为 arguments 字典,是所有「动态调用前先理解签名」需求的基石。注意 property、装饰过的函数要看 __wrapped__,C 函数部分能读但不可 bind。

```python
# file: code/01_语言核心与底层/q497_inspect_signature.py
import inspect

def transfer(amount, *, from_acc="A", to_acc="B", fee=0.0):
    return f"{from_acc} -> {to_acc}: {amount} fee={fee}"

if __name__ == "__main__":
    sig = inspect.signature(transfer)
    for name, param in sig.parameters.items():
        default = "REQUIRED" if param.default is inspect.Parameter.empty else param.default
        print(f"{name:10s} kind={param.kind.name:20s} default={default}")

    bound = sig.bind(100, to_acc="C")
    bound.apply_defaults()
    print("normalized:", dict(bound.arguments))
    print(transfer(*bound.args, **bound.kwargs))
```

**追问**:1) 怎么区分「没传默认值」和「默认值恰好是 None」?——Parameter.empty 是专用哨兵,`param.default is inspect.Parameter.empty` 才是缺省,不能用 None 判断。2) bind 相比手工拼参数强在哪?——Signature.bind 把任意调用形式归一成「参数名→值」映射,统一处理位置/关键字/默认值/*args/**kwargs/kw-only 各种声明,手工解析必漏边角。3) signature 的来源与限制?——inspect 沿 __signature__ 或代码对象反射构建;C 扩展函数没有 Python 帧时要靠 __text_signature__(ArgumentClinic 生成),否则拿到 (*args, **kwargs) 占位。4) 生产陷阱?——装饰器漏 wraps 使签名变 (*args, **kwargs),参数校验静默失效;Signature 不可变,replace 返回新对象,原地改签名无效。
