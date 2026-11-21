---
title: [Q498] Signature.bind 与动态调用
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q498 · Signature.bind 与动态调用

> 难度:★★★★ | 标签:inspect, 动态调用

**问**:从配置/请求里拿到一组 kwargs,如何安全地调用一个函数(多余参数要过滤、缺失参数要报错)?

**答**:裸 func(**kwargs) 遇到多余键直接 TypeError,且错误信息不友好。标准流程:取签名 → 按 sig.parameters 过滤掉目标函数不接受的键 → sig.bind(**accepted) 做完整校验(位置/关键字归属、必填缺失、重复传参都在此报错)→ apply_defaults 补齐 → func(*bound.args, **bound.kwargs)。这条流水线是配置驱动调用(CLI 分发、API handler 路由、任务队列参数解析)的通用骨架;bind 的价值在于「把调用协议的校验从运行时碰运气变成确定性预处理」。

```python
# file: code/01_语言核心与底层/q498_signature_bind.py
import inspect

def make_request(method, url, *, headers=None, timeout=30):
    return {"method": method, "url": url, "headers": headers or {}, "timeout": timeout}

CALL_SPEC = {"method": "GET", "url": "/api/items", "extra": "ignored by design"}

def call_with_mapping(func, spec):
    sig = inspect.signature(func)
    accepted = {k: v for k, v in spec.items() if k in sig.parameters}
    bound = sig.bind(**accepted)          # 缺失必填参数在这里报错
    bound.apply_defaults()
    return func(*bound.args, **bound.kwargs)

def volume(a, b, /, factor=1):            # 3.8 起支持 positional-only
    return a * b * factor

if __name__ == "__main__":
    print(call_with_mapping(make_request, CALL_SPEC))
    sig = inspect.signature(volume)
    bound = sig.bind(2, 3, factor=2)
    print("positional-only bind:", volume(*bound.args, **bound.kwargs))
```

**追问**:1) positional-only 参数(/)解决了什么?——让参数名成为实现细节,调用方不能写 a=1,重命名参数不破坏 API,内置函数如 len 就受益于此。2) bind 与 bind_partial 的差别?——bind 校验完整性,缺参抛 TypeError;bind_partial 允许缺参(后续补齐),两者都返回 BoundArguments;apply_defaults 再补默认值。3) 绑定算法的底层顺序?——按声明顺序处理 pos-only→pos-or-keyword→var-pos→kw-only→var-kw,冲突/多余参数抛 TypeError——等于用纯 Python 复刻了调用时字节码的参数打包逻辑。4) 生产陷阱?——把 bound.arguments 直接当 kwargs 透传丢失顺序语义,应 func(**bound.arguments) 或 func(*bound.args, **bound.kwargs);BoundArguments 复用前忘记重置。
