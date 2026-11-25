---
title: "[Q5199] type() 动态建类后 pickle 报 not the same object"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5199 · type() 动态建类后 pickle 报 not the same object

难度：P7 ｜ 标签：type()、pickle、__qualname__、按引用序列化、插件注册表

**问**：ORM/插件框架用 `type(name, bases, attrs)` 动态生成模型类，本地测试正常，一进多进程任务（`multiprocessing` 或 Celery）就抛 `PicklingError: Can't pickle <class 'app.models.User'>: it's not the same object as app.models.User`。`pickle` 怎么序列化一个类？为什么"名字对得上"还不够？动态类到底该怎么注册才能被反序列化？

**答**：
结论：`pickle` 序列化类/函数时**不打包代码**，只记录 `module` + `qualname` 的引用，反序列化时 `import` 该模块并按 `getattr` 逐级取值，然后断言取到的对象与序列化时是同一个（`obj is not the same` 就抛 `PicklingError`）。`type()` 造出来的类如果没绑定到模块全局，`getattr(module, "User")` 拿到的是 `None` 或另一个对象，于是失败。换句话说：pickle 认的是"可重新导入的路径"，不是"长得一样的 typedef"。

取舍：a) 动态类创建后立刻 `setattr(sys.modules[cls.__module__], cls.__qualname__, cls)`，并保证 `__qualname__` 不含 `<locals>`、`__module__` 指向真实模块——这是框架（Django 的 model、SQLAlchemy 的 declarative）能跨进程的前提；b) 传"类名 + 参数"而不是传类，接收端重建，代价是多一次解析但更稳；c) 用 `copyreg`/`__reduce__` 自定义序列化为工厂函数，适合无法绑定全局的场景。注意多进程 `spawn` 会重新 import 主模块，`if __name__ == "__main__"` 保护缺失时动态类会被创建两次，仍可能不是同一个对象。

实战：事故形态是"任务队列 worker 反序列化任务参数时报 not the same object，主进程里明明有这个类"。下面演示未绑定全局的失败、绑定后的成功、`<locals>` 造成的不可达，以及用工厂函数绕过。

```python
import pickle
import sys
import types

module = sys.modules[__name__]

# 1) 动态建类，但模块里没有同名全局
LooseRef = type("Loose", (), {"__module__": __name__})
try:
    pickle.dumps(LooseRef)
except pickle.PicklingError as e:
    print("[1] 未绑定全局:", type(e).__name__, "|", e)

# 2) 绑定到模块命名空间后可被按引用找到
Bound = type("Bound", (), {"__module__": __name__})
setattr(module, "Bound", Bound)
blob = pickle.dumps(Bound)
print("[2] 绑定后可序列化:", pickle.loads(blob) is Bound)

# 3) 定义在函数内部：qualname 带 <locals>，永远不可达
def factory():
    class Inner:
        pass

    return Inner


Inner = factory()
setattr(module, "Inner", Inner)
print("[3] 局部类的 qualname:", Inner.__qualname__)
try:
    pickle.dumps(Inner)
except (pickle.PicklingError, AttributeError) as e:
    print("[3] <locals> 类:", type(e).__name__, "|", e)

# 4) 不能绑定全局时：自定义 reduce 走工厂函数
def rebuild(spec):
    return type(spec["name"], (), {"__module__": __name__})


class Wrapper:
    def __init__(self):
        self.cls = type("Hidden", (), {"__module__": __name__})

    def __reduce__(self):
        return (rebuild, ({"name": "Hidden"},))


obj = pickle.loads(pickle.dumps(Wrapper()))
print("[4] reduce 工厂重建:", type(obj).__name__)

# 5) 模块名写错：pickle 会去 import 一个不存在的模块
Bad = type("Bad", (), {"__module__": "app.not_exists"})
setattr(module, "Bad", Bad)
try:
    pickle.dumps(Bad)
except (pickle.PicklingError, ModuleNotFoundError) as e:
    print("[5] __module__ 不真实:", type(e).__name__, "|", e)
```

**追问一**：为什么 `copy.deepcopy` 不会报这个错？—— `deepcopy` 对有 `__deepcopy__`/`__reduce_ex__` 的对象走内存重建，对普通对象复制 `__dict__`，不需要"按名字找回来"。pickle 的核心约束是**跨进程序列化必须能重建引用**，所以它需要稳定的导入路径；`deepcopy` 只在同一进程内复制值，没这个要求。这也是"本地 deepcopy 正常、多进程一跑就炸"的根因。

**追问二**：`spawn` 与 `fork` 下动态类的表现为什么不同？—— `fork` 直接复制父进程内存，类对象地址相同，`is` 判断成立，能正常工作；`spawn` 起全新解释器，重新 import 主模块，模块顶层的 `type()` 会再执行一次生成**新对象**。若这个类被放在 `if __name__ == "__main__"` 之外，还会在子进程 import 时产生副作用（重复建表、重复注册）。所以"fork 能跑、spawn 挂"不是 pickle 的 bug，而是"按引用重建"暴露了动态类没有稳定导入路径。

## 背诵要点
- pickle 序列化类只记 `module + qualname`，反序列化按路径 import/getattr 并要求 `is` 同一对象。
- 动态类必须绑定到模块全局，`__qualname__` 不能含 `<locals>`，`__module__` 必须是真实可导入模块。
- 无法绑定时用 `__reduce__`/`copyreg` 走工厂重建；`fork` 能掩盖问题，`spawn` 会暴露。

## 复盘追问
- 多进程任务报 `not the same object`，如何从 pickle 的按引用机制定位？（模块全局缺失 / `<locals>` / 重复创建）
- 为什么 `fork` 正常、`spawn` 失败？（内存复制 vs 重新 import 生成新类对象）
