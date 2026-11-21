---
title: [Q476] @contextmanager 的实现原理
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q476 · @contextmanager 的实现原理

> 难度:★★★★★ | 标签:上下文管理器, 生成器

**问**:手写一个 @contextmanager,异常路径上 throw 的语义要处理哪几种情况?

**答**:核心是一个把生成器包成上下文管理器的适配器:__enter__ 执行 next(gen) 推进到 yield 并取值;__exit__ 无异常时再 next 让生成器跑完(没跑完抛 RuntimeError);有异常时把异常 throw 进生成器的挂起点,然后处理三种结局——生成器抛 StopIteration 说明它吞掉了异常,返回 True 抑制;抛出的是同一个异常对象,返回 False 让它继续传播;抛了别的异常,把它作为新异常带上下文抛出。这套分支正是 contextlib 的精华,理解它就理解了「yield 分隔初始化与清理」的完整语义。

```python
# file: code/01_语言核心与底层/q476_contextmanager_internals.py
import functools

def my_contextmanager(func):
    """复刻 contextlib.contextmanager 的核心语义"""
    @functools.wraps(func)
    def helper(*args, **kwargs):
        return _GeneratorCM(func(*args, **kwargs))
    return helper

class _GeneratorCM:
    def __init__(self, gen):
        self.gen = gen

    def __enter__(self):
        return next(self.gen)                 # 执行到 yield,取值

    def __exit__(self, exc_type, exc, tb):
        if exc_type is None:
            try:
                next(self.gen)                # 正常:推进到函数结束
            except StopIteration:
                return False
            raise RuntimeError("generator did not stop")
        try:
            self.gen.throw(exc_type, exc, tb) # 异常:在 yield 处注入
        except StopIteration:
            return True                       # 生成器吞掉了异常 → 抑制
        except BaseException as new_exc:
            if new_exc is exc:
                return False                  # 原样重新抛出 → 继续传播
            raise new_exc from exc            # 改抛了别的异常 → 带上下文抛出

@my_contextmanager
def managed(label):
    print(f"enter {label}")
    try:
        yield label.upper()
    finally:
        print(f"exit {label}")

@my_contextmanager
def swallow_errors(label):
    print(f"enter {label}")
    try:
        yield
    except ValueError:
        print(f"{label} swallowed ValueError")
    finally:
        print(f"exit {label}")

if __name__ == "__main__":
    with managed("hello") as v:
        print("inside:", v)
    with swallow_errors("s"):
        raise ValueError("boom")
    print("survived swallow")
    try:
        with managed("m"):
            raise KeyError("pass-through")
    except KeyError as e:
        print("propagated:", e)
```

**追问**:1) contextlib 正式版比这个复刻多处理了什么?——启动生成器时的异常传播、同一实例二次 with 的不可重入检测、以及 _GeneratorContextManagerBase 支持 with cm as x 后继续用 cm() 拷贝出新实例。2) __enter__ 阶段抛错为什么不用特殊处理?——生成器体在 yield 前抛错属「初始化失败」,异常自然从 with 向上传播,此时清理逻辑还没登记;正式版只需保证异常不被 helper 吞掉。3) gen.throw 的签名演进?——3.12 起推荐单参 throw(exc),老的 (type, value, tb) 三参形式已弃用;复刻版的三个分支(吞掉/原样/替换)在两代签名下语义一致。4) 生产陷阱?——生成器函数里 yield 写进循环,第二次 yield 让 __exit__ 的 next 抛 RuntimeError("generator didn't stop");吞异常分支误吞 KeyboardInterrupt——「is exc」判断要精确,兜底 except BaseException 是反模式。
