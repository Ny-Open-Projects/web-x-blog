---
title: [Q446] run_once 与 deprecated:状态记忆型装饰器
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q446 · run_once 与 deprecated:状态记忆型装饰器

> 难度:★★★☆ | 标签:装饰器, warnings

**问**:如何让装饰器「记住」自己是否已执行过?deprecated 告警为什么每个调用点只警告一次?

**答**:在闭包里维护状态标志即可:run_once 记录是否已计算并缓存结果;deprecated 记录是否已告警,避免日志风暴。关键细节:状态是闭包私有变量,必须 nonlocal 修改;告警用 warnings.warn + DeprecationWarning + stacklevel=2,让告警指向调用方而不是装饰器内部。这类「一次性」状态在多线程下是 check-then-act 竞态,严格场景要加锁或改用 threading.Lock 保护。

```python
# file: code/01_语言核心与底层/q446_run_once_deprecated.py
import functools
import warnings

def run_once(func):
    """真实逻辑只执行一次,之后返回缓存结果"""
    result = None
    called = False

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal result, called
        if not called:
            result = func(*args, **kwargs)
            called = True
        return result
    return wrapper

def deprecated(reason):
    def deco(func):
        warned = False

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal warned
            if not warned:                    # 只警告一次
                warnings.warn(
                    f"{func.__name__} is deprecated: {reason}",
                    DeprecationWarning,
                    stacklevel=2,
                )
                warned = True
            return func(*args, **kwargs)
        return wrapper
    return deco

@run_once
def init_config():
    print("  [init_config] heavy work")
    return {"mode": "prod"}

@deprecated("use new_api instead")
def old_api():
    return "old result"

if __name__ == "__main__":
    print(init_config())
    print(init_config())                      # 不再打印 heavy work
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        print(old_api())
        print(old_api())                      # 第二次不重复告警
        print("warnings captured:", len(caught))
```

**追问**:1) 把状态放在闭包里 vs 放函数属性上,取舍是什么?——闭包状态不可见不可测;函数属性(wrapper.cache_hit 之类)可检查可测试,团队库更推荐后者。2) run_once 的竞态后果?——两线程同时读到 called=False 各执行一次,后写覆盖先写;初始化场景可能双份资源(两个连接池),解法是 threading.Lock 或 lru_cache(maxsize=1)(C 实现自带锁)。3) warnings 去重的底层机制?——__warningregistry__ 按 (message, category, lineno) 记录已告警位置,命中即跳过;stacklevel=2 让归属记到调用方,否则弃用告警指向装饰器内部文件,过滤策略失准。4) 生产陷阱?——DeprecationWarning 默认只在 __main__ 显示,用户根本看不到库的弃用告警,必须同步写进文档与变更日志;闭包标志在 fork 子进程里被复制,可能双重初始化。
