---
title: [Q2088] functools.wraps 缺席的实测后果
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2088 · functools.wraps 缺席的实测后果

> 难度:★★★☆☆ | 标签:functools.wraps, 元数据, 装饰器

**问**:装饰器不加 @functools.wraps,除了 __name__ 变成 wrapper 还会丢什么?

**答**:实测后果是四连丢:__name__ 变 'wrapper'、__doc__ 变 None、__qualname__ 失真,inspect.signature 退化成 (*args, **kwargs)——调用方看 help() 与 IDE 提示全是错的,基于签名的参数校验、文档生成、序列化框架全部跟着失真。此外丢失 __wrapped__ 引用,inspect.unwrap 无法穿透多层装饰还原原函数,层层包装后元数据丢失会复合。修复零成本:被装饰的 wrapper 上加 @functools.wraps(func),它把 __name__、__doc__、__qualname__、__module__、__dict__ 复制过来并设置 __wrapped__(与 Q013、Q447 一致)。规则:任何手写装饰器模板的第一行就是 wraps。

```python
# file: code/01_语言核心与底层/q2088_wraps_missing.py
"""functools.wraps 缺席的实测后果:元数据丢失清单。"""
import functools
import inspect


def loud(func):
    def wrapper(*args, **kwargs):
        print("调用前")
        return func(*args, **kwargs)
    return wrapper


def loud_fixed(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("调用前")
        return func(*args, **kwargs)
    return wrapper


@loud
def charge(amount):
    """扣款:金额必须为正。"""
    return amount


@loud_fixed
def charge_fixed(amount):
    """扣款:金额必须为正。"""
    return amount


if __name__ == "__main__":
    print("无 wraps -> __name__:", charge.__name__, "| __doc__:", charge.__doc__)
    print("无 wraps -> 签名:", inspect.signature(charge))
    print("有 wraps -> __name__:", charge_fixed.__name__, "| __doc__:", charge_fixed.__doc__)
    print("有 wraps -> 签名:", inspect.signature(charge_fixed))
    print("__wrapped__ 指向原函数:", charge_fixed.__wrapped__.__name__)
```

**追问**:1) wraps 对调试还有什么贡献?——保留 __qualname__ 让 traceback 与 pdb 显示真实函数名;多层装饰器怎么办?——每一层的 wrapper 都要加 wraps,否则元数据在最外层先丢。2) 缺席的完整后果链?——__name__ 变 wrapper → 监控/日志聚合失效;签名变 (*args, **kwargs) → 自省与参数校验失效(Q497);__doc__ 丢 → help 无效;__wrapped__ 缺 → 签名链断。3) wraps 拷贝什么?——__module__/__name__/__qualname__/__doc__/__dict__,并设 __wrapped__;签名还原沿 __wrapped__ 链(Q447)。4) 生产陷阱?——第三方装饰器漏 wraps(给自家 wrapper 补);多层装饰只有最外层 wraps;按 __name__ 做路由的代码被 wrapper 名坑。
