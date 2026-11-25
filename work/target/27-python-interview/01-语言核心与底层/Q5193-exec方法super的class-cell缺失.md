---
title: "[Q5193] exec 出来的方法调用 super() 报 __class__ cell 缺失"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5193 · exec 出来的方法调用 super() 报 __class__ cell 缺失

难度：P7 ｜ 标签：super、__class__ cell、exec、编译期符号表、插件热加载

**问**：插件系统用 `exec` 编译一段函数源码，再 `setattr` 挂到类上，调用时零参 `super()` 抛 `RuntimeError: super(): __class__ cell not found`。而同样的代码写成完整 `class` 语句就没问题。`super()` 的无参形式凭什么找到当前类？为什么"函数级"和"类体级"的编译结果不同？运行时能不能补救？

**答**：
结论：零参 `super()` 需要两个隐式上下文——`__class__` 闭包单元和第一个位置参数（`self`/`cls`）。编译器只有在**函数词法上位于 class 体内部**时，才会给该函数加一个 `__class__` cell，并在类命名空间里塞入 `__classcell__`，由 `type.__new__` 在创建类时把 cell 填成新类。函数若单独编译（`exec` 一个 `def`）再挂上去，符号表里没有 class 作用域，不会产生 cell，调用时就找不到当前类；在模块级直接写 `def f(): return super()` 则是另一种错——`super(): no arguments`。

取舍：运行时补救有三条：a) 改为显式两参 `super(Child, self)`，把类当普通对象传入，不依赖 cell，代价是类改名/被包装时要同步改；b) 让 `exec` 执行的是**整段 class 语句**，编译器自然生成 cell，代价是动态生成的粒度从"方法"变成"类"；c) 用 `functools.partial` 或闭包捕获基类方法，不走 `super`。插件热加载场景推荐 b，因为方法级注入还会遇到描述符绑定、`__set_name__` 不触发等一连串问题。

实战：事故形态是"插件加载器支持热替换单个方法，A 插件的方法里用了 `super()` 调基类校验，热加载后第一次请求 500"。下面演示三种失败/成功路径，并验证异常文案。

```python
class Base:
    name = "base"

    def greet(self):
        return f"base:{self.name}"


class Child(Base):
    pass


# 1) 单独编译函数再挂到类上：没有 __class__ cell
ns = {}
exec("def greet(self):\n    return super().greet() + '|child'\n", ns)
Child.greet = ns["greet"]
try:
    print(Child().greet())
except RuntimeError as e:
    print("[1] 挂上去的方法:", type(e).__name__, "|", e)


# 2) 模块级函数里写零参 super：连 self 都没有
def loose():
    return super()


try:
    loose()
except RuntimeError as e:
    print("[2] 模块级函数:", e)


# 3) exec 整段 class 语句：编译器生成 cell，type.__new__ 负责填充
ns2 = {}
exec(
    "class Child2(Base):\n"
    "    def greet(self):\n"
    "        return super().greet() + '|child2'\n",
    {"Base": Base},
    ns2,
)
print("[3] 整段 class 语句:", ns2["Child2"]().greet())
print("[4] cell 已被填充:", ns2["Child2"].greet.__closure__ is not None,
      ns2["Child2"].greet.__closure__[0].cell_contents is ns2["Child2"])


# 5) 显式两参：不依赖 cell
class Child3(Base):
    def greet(self):
        return super(Child3, self).greet() + "|child3"


print("[5] 显式 super(类, self):", Child3().greet())
```

**追问一**：`__classcell__` 是谁消费的？—— 类体执行结束时，编译器会把 `__classcell__` 作为类命名空间的一个特殊键留下，`type.__new__` 看到它就把 cell 内容设为正在创建的类；如果类体里引用了 `__class__` 却没有把它传给 `type.__new__`（例如手工 `type(name, bases, ns)` 前把 `__classcell__` 过滤掉），会得到 `RuntimeError: __class__ not set defining ...`。这也是很多"自定义元类 + 手工建类"框架踩的坑。

**追问二**：为什么 `super()` 在 `staticmethod` 里也不能用零参？—— 零参形式要靠第一个位置参数推断"从哪个类开始查找"，`staticmethod` 不绑定 `self`/`cls`，编译器虽然仍会给 cell（词法在类体内），但运行时拿不到实例，抛 `RuntimeError: super(): no arguments`。`classmethod` 可以，因为第一个参数是 `cls`；这就是"工厂方法里用 `super()` 要声明成 classmethod"的原因。

## 背诵要点
- 零参 `super()` 依赖编译期生成的 `__class__` cell，cell 只在函数词法位于 class 体内时产生。
- `exec` 单函数再 `setattr` 没有 cell → `super(): __class__ cell not found`；补救是显式 `super(Cls, self)` 或 exec 整段 class。
- `staticmethod` 里零参 `super()` 必然失败（无 `self`/`cls`），`classmethod` 可以。

## 复盘追问
- 插件热加载单个方法后 `super()` 报 cell 缺失，如何从符号表和 `type.__new__` 解释？（cell 生成时机、`__classcell__` 消费）
- 为什么"把方法挂到类上"还会连带破坏 `__set_name__` 和描述符？（类创建期钩子已过）
