---
title: [Q034] __new__ 与单例模式
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q034 · __new__ 与单例模式

> 难度:★★★ | 标签:类, 设计模式

**问**:`__new__` 和 `__init__` 的职责区别?如何正确实现单例?

**答**:`__new__` 是静态方法,负责创建并返回实例,先于 `__init__` 执行;`__init__` 只负责初始化已返回的实例,不返回值。单例应重写 `__new__` 控制实例创建;多线程下要加锁,否则两个线程可能同时通过 `cls._instance is None` 检查。更 Pythonic 的替代是模块级单例或 `functools.lru_cache` 的构造缓存。

```python
# file: code/01_语言核心与底层/q034_singleton.py
import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:          # 双重检查,减少锁开销
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, config):
        self.config = config               # 注意:每次都会执行

if __name__ == "__main__":
    a = Singleton("dev")
    b = Singleton("prod")
    print(a is b)          # True
    print(a.config)        # prod,__init__ 被第二次调用覆盖了

    threads = [threading.Thread(target=Singleton, args=("t",)) for _ in range(8)]
    for t in threads: t.start()
    for t in threads: t.join()
    print(Singleton._instance is b)
```

**追问**:1) 单例的 `__init__` 重复执行怎么避免?——在 `__init__` 里检查已初始化标志,或干脆不在 `__new__` 之外做状态初始化。2) 多线程安全的单例怎么写?——`__new__` 内加 `threading.Lock` 双重检查,或直接用模块级实例(导入本身有锁);测试环境要提供重置入口,否则用例间状态污染。3) 单例的反模式是什么?——隐藏全局状态、并发下成为锁瓶颈、依赖注入与测试都困难;更可控的替代是显式传递的依赖或 DI 容器管理的单生命周期对象。
