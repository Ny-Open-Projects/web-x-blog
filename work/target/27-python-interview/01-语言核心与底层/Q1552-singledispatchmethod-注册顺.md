---
title: [Q1552] singledispatchmethod:注册顺序与继承扩展
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1552 · singledispatchmethod:注册顺序与继承扩展

> 难度:★★★★☆ | 标签:functools, 分派, 多态

**问**:类里按参数类型分派,singledispatchmethod 的注册顺序会互相覆盖吗?与继承怎么配合?3.9 用它有什么限制?

**答**:singledispatchmethod(3.8+)把「按第一个非 self 参数的运行时类型分派」装进类:基方法作 object 兜底,@render.register(int) 逐型注册;派发沿参数类型 MRO 找最近注册,给基类注册的实现可被子类实例命中,未命中走兜底(Q427 讲函数版注册顺序,Q1276 讲与多态的关系,本题聚焦方法版的注册与扩展)。注册发生在类体执行(类创建)时:同型重复注册后者静默覆盖,运行期条件注册与 import 顺序耦合是常见坑。子类扩展分派表:@父类.render.register(新类型) 把实现登记进同一 dispatcher,实例共享。3.9 限制:不能与 classmethod/staticmethod/abstractmethod 叠放(3.11 支持),分派只看运行时类型不看泛型参数——list[int] 与 list[str] 同命。

```python
# file: code/01_语言核心与底层/q1552_singledispatchmethod.py
from functools import singledispatchmethod


class Renderer:
    @singledispatchmethod
    def render(self, value):
        return "fallback<" + type(value).__name__ + ">"     # object 兜底

    @render.register(int)
    def _(self, value):
        return "int:%+d" % value

    @render.register(list)
    def _(self, value):
        return "list[" + ", ".join(self.render(v) for v in value) + "]"


class FancyRenderer(Renderer):
    @Renderer.render.register(float)
    def _(self, value):              # 子类扩展:登记进父类的 dispatcher
        return "float:%.2f" % value


if __name__ == "__main__":
    r = Renderer()
    print(r.render(42))
    print(r.render(3.14159))
    print(r.render([1, -2, "hi"]))
    print(r.render({"plain": "dict"}))

    f = FancyRenderer()
    print("fancy float        :", f.render(2.71828))
    print("fancy int inherits :", f.render(7))
```

**追问**:1) 分派支持抽象基类注册吗?——支持,register(Sequence) 后传 list 能命中,靠虚拟子类判定;但泛型参数不参与,list[int] 与 list[str] 同命。2) 注册与解析的规则?——按类型层级查 MRO 最近实现;子类自动命中父类注册;运行期 register 即插即用,注册顺序无关;协议/ABC 注册走虚拟子类判定。3) 与 isinstance 分派的差异?——singledispatch 按精确类型层级解析,更快也更明确;isinstance 链要手写顺序;混合使用时口径要统一。4) 生产陷阱?——新类型漏注册 NotImplementedError,边界要兜底;以为泛型参数参与分派;ABC 注册后忘了虚拟子类「不继承实现」——分派命中但你方法不存在的假象。
