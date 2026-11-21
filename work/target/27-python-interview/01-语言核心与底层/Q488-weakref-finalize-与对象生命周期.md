---
title: [Q488] weakref.finalize 与对象生命周期钩子
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q488 · weakref.finalize 与对象生命周期钩子

> 难度:★★★★ | 标签:weakref, 资源管理

**问**:__del__ 写清理逻辑有什么坑?weakref.finalize 为什么更可靠?

**答**:finalize(register, callback, *args) 把「对象死亡时执行 callback」注册到独立对象上,它不依赖 __del__:callback 与参数被 finalize 对象持有而不是被目标对象持有,不存在「复活对象」问题,异常会打印而不是静默,且支持 atexit 兜底与显式调用(detach 语义)。__del__ 的坑:解释器关闭期全局名可能已清空、异常被忽略、对象复活导致二次终结不可预期、以及与 GC 周期回收的时序耦合。生产清理(临时文件、句柄、C 扩展资源)优先 finalize;必须 __del__ 时只做最小且不依赖全局的动作。

```python
# file: code/01_语言核心与底层/q488_weakref_finalize.py
import weakref

class TempFile:
    pass

def cleanup(name):
    print(f"[finalize] cleaning {name}")

if __name__ == "__main__":
    f = TempFile()
    ref = weakref.finalize(f, cleanup, "tmp123")
    print("alive:", ref.alive)
    del f                          # 对象回收,回调被调用
    print("alive after del:", ref.alive)
    ref()                          # 再次调用:已死,安全 no-op
    print("calling a dead finalizer is safe")

    g = TempFile()
    ref2 = weakref.finalize(g, cleanup, "tmp456")
    ref2()                         # 也可以主动触发并解除注册
    print("alive after manual call:", ref2.alive)
```

**追问**:1) finalize 的回调里能引用目标对象吗?——不能,闭包或参数里引用目标对象会让目标永不回收(回调先于对象死亡而被持有),这是 finalize 使用的头号陷阱。2) finalize 比 __del__ 好在哪?——独立回调对象持弱引用不阻止回收、保证恰好执行一次、可手动调用/detach 提前注销;__del__ 时机不定、异常被忽略打印、还要面对解释器退出时半拆除的模块状态。3) finalize 的底层结构?——注册表持有 (弱引用, callback, args, state),靠弱引用回调感知目标死亡,解释器退出时对存活的 finalize 再统一触发一次兜底。4) 生产陷阱?——给本应长存的对象(全局缓存)注册清理,回调永不触发或时机错乱;fork 后子进程继承注册表,对已不存在的资源重复清理。
