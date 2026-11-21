---
title: [Q1813] classmethod/staticmethod 的描述符本质:绑定时机
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1813 · classmethod/staticmethod 的描述符本质:绑定时机

> 难度:★★★★☆ | 标签:描述符, 绑定, 方法

**问**:普通函数、classmethod、staticmethod 挂在类体里,属性访问时分别发生了什么?

**答**:三者都是非数据描述符,差异全在 __get__ 的绑定行为(Q026 讲描述符分级,本题专讲方法绑定):① 普通函数 __get__(instance, owner) 返回绑定方法,把 instance 预填为第一参数——更准确的说法是「函数是描述符,方法是被绑定后的产物」;② classmethod.__get__ 忽略 instance,永远绑到类,连经由实例访问 m.klass() 拿到的 cls 也是类;③ staticmethod.__get__ 什么都不绑,原样返回底层函数。demo 里 Meta.__dict__ 取出的对象类型分别为 function/classmethod/staticmethod,手动 __get__(None, Meta) 后变成 method/method/function。应用分工:classmethod 适合「需要 cls 的替代构造器与注册点」,staticmethod 适合「命名空间归属下的纯函数」;想绕开绑定拿原始函数,从 __dict__ 取再手动 __get__,或经 __func__。

```python
# file: code/01_语言核心与底层/q1813_binding_descriptors.py
"""classmethod/staticmethod 的描述符本质:绑定时机。"""
import types


class Meta:
    version = "1.0"

    def instance_method(self):
        return "bound to " + type(self).__name__

    @classmethod
    def klass(cls):
        return "bound to class " + cls.__name__

    @staticmethod
    def plain():
        return "no binding"


def descriptor_view():
    rows = []
    for name in ("instance_method", "klass", "plain"):
        attr = Meta.__dict__[name]
        rows.append((name, type(attr).__name__))
    return rows


if __name__ == "__main__":
    print("类体内是描述符对象:", descriptor_view())
    m = Meta()
    print("实例调用:", m.instance_method(), "|", m.klass(), "|", m.plain())
    print("__get__ 绑定结果:",
          type(Meta.__dict__["instance_method"].__get__(m, Meta)).__name__,
          type(Meta.__dict__["klass"].__get__(None, Meta)).__name__,
          type(Meta.__dict__["plain"].__get__(None, Meta)).__name__)
    print("普通函数也是描述符:",
          isinstance(Meta.__dict__["instance_method"], types.FunctionType))
```

**追问**:1) 为什么 super().method() 不用手动传 cls?——super 代理在 __get__ 时把当前类作为 owner 绑定,cls 自动是 MRO 下一个类,这也是协作式初始化能工作的机制之一。2) 绑定时机的本质?——classmethod/staticmethod 是描述符:属性访问时 __get__ 决定返回绑定方法还是裸函数;描述符协议是「函数绑定行为」的统一实现(Q451 的数据/非数据之分同源)。3) 与实例方法的对比?——function 类型的 __get__ 绑定 instance,classmethod 绑定 class,staticmethod 不绑定;绑定发生在每次属性访问,不是类定义时。4) 生产陷阱?——staticmethod 里试图用 cls/self;classmethod 链式调用时误传 self;把绑定后的方法对象长期缓存(绑定目标生命周期变化)。
