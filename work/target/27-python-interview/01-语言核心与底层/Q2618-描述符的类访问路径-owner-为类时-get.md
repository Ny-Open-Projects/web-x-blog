---
title: [Q2618] 描述符的类访问路径:owner 为类时 __get__ 拿到什么
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2618 · 描述符的类访问路径:owner 为类时 __get__ 拿到什么

> 难度:★★★☆☆ | 标签:描述符, __get__, 绑定

**问**:`MyClass.attr` 访问一个描述符时会发生什么?`instance` 参数为什么是 None?

**答**:描述符 `__get__(self, instance, owner)` 的两个参数只在实例访问时才「双满」:`obj.attr` 时 instance 是 obj、owner 是 type(obj);而 `MyClass.attr` 时 instance 是 None、owner 是 MyClass 本身。`property` 在类访问时直接返回 property 对象自身(这就是 `@property` 装饰的方法在类上看到的是 property 而不是值的原因);函数描述符在类访问时返回普通函数(未绑定)。自定义描述符要利用这一点:类访问常用来返回描述符自身(便于内省)或做类级配置,实例访问才做真正的取值。写描述符库时必须把 instance is None 这个分支处理清楚,否则类访问会莫名崩溃。

```python
# file: code/01_语言核心与底层/q2618_descriptor_class_get.py
"""类访问描述符:instance 为 None、owner 为类时分派的两种姿势。"""


class Versioned:
    """实例访问返回值,类访问返回描述符自身便于内省。"""

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner=None):
        if instance is None:
            print(f"    [类访问] owner={owner.__name__}, 返回自身")
            return self
        print(f"    [实例访问] owner={owner.__name__}, 返回存储值")
        return instance.__dict__.get(self.name, "未设置")

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Service:
    version = Versioned()


if __name__ == "__main__":
    print("类访问:")
    desc = Service.version                # instance=None 分支
    print("    拿到:", type(desc).__name__)

    print("实例访问:")
    svc = Service()
    svc.version = "2.1"
    print("    拿到:", svc.version)

    print("property 的类访问返回 property 对象本身:")
    print("    ", type(Service.__dict__.get("version", None)) is Versioned)
```

**追问**:1) 函数在类访问时返回什么?——普通函数(未绑定),Python 3 没有未绑定方法概念;实例访问时才经描述符协议绑定成 method 对象。2) owner 为类的语义?——__get__(None, owner) 返回描述符自身(或裸函数),框架借此做「类级配置读取」(Q451 的 Typed 返回自身);classmethod/staticmethod 在类访问时同样解包(Q1813)。3) 与元编程的配合?——类访问拿描述符可调 invalidate(Q452 的缓存失效);__set_name__ 后名字已知;装饰器在类体完成装配。4) 生产陷阱?——以为类访问拿到「绑定方法」;文档里 Cls.attr 语义没写清;静态工具(如 mypy)对类访问类型的推断与运行时不一致。
