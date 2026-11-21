---
title: [Q1807] __init_subclass__ 的声明式 kwargs:配置上浮与约束校验
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1807 · __init_subclass__ 的声明式 kwargs:配置上浮与约束校验

> 难度:★★★★☆ | 标签:元编程, __init_subclass__, 声明式

**问**:Q455 讲了注册与约束,子类关键字参数的「消化链」你梳理过吗?多个 mixin 各自定义 __init_subclass__ 时 kwargs 怎么流动?

**答**:类体里 `class User(Table, table="users", strict=False)` 的 kwargs 由 MRO 上各基类的 __init_subclass__ 逐层「认领」:每层签名里显式声明的参数留下自用,其余通过 super().__init_subclass__(**kwargs) 继续上传,最终 object.__init_subclass__() 不收任何参数——有人留了没人认领的键就 TypeError,这是天然的拼写检查。三个工程要点:① 每层 mixin 只声明自己关心的 kwargs,组合时互不感知;② 约束校验查 cls.__dict__ 而不是 hasattr,避免把继承来的成员误当自己的声明(Q455 同款纪律);③ 注册表在这层维护,类定义即完成,导入顺序决定注册顺序——与 Q442 装饰器注册器同源的问题,解法都是「注册时只记录、使用时再解析」。

```python
# file: code/01_语言核心与底层/q1807_init_subclass_kwargs.py
"""__init_subclass__ 的声明式 kwargs:配置上浮与约束校验。"""


class Table:
    registry = {}

    def __init_subclass__(cls, table=None, strict=True, **kwargs):
        super().__init_subclass__(**kwargs)      # 其余 kwargs 沿 MRO 继续上传
        cls.table = table or cls.__name__.lower()
        cls.strict = strict
        if strict and "columns" not in cls.__dict__:
            raise TypeError(cls.__name__ + " 缺少 columns 声明")
        Table.registry[cls.table] = cls


class User(Table, table="users", strict=False):
    columns = ["id", "name"]


class Order(Table):
    columns = ["id", "amount"]


if __name__ == "__main__":
    print("注册表:", sorted(Table.registry))
    print("User 表名:", User.table, "| strict:", User.strict)
    print("Order 表名(默认推导):", Order.table)
    try:
        type("Bad", (Table,), {"table": "bad"})  # strict 且缺 columns
    except TypeError as e:
        print("约束生效:", str(e)[:44])
```

**追问**:1) __init_subclass__ 里抛 TypeError 在什么时机炸?——子类定义/import 时刻,而非实例化时刻,错误左移到 CI 阶段。2) kwargs 的来源与链式约束?——类体括号参数由 metaclass 透传给 __init_subclass__;必须显式 super().__init_subclass__(**kwargs) 把不认识的传下去,否则基类钩子被跳过;未知关键字直接报错是特性不是 bug。3) 配置上浮的收益?——类声明即配置(如 class Csv(Backend, codec="utf8")),注册/校验/参数都在类创建期完成;与 __set_name__/__class_getitem__ 同属声明式工具箱。4) 生产陷阱?——吞掉 kwargs 不传 super 导致多级钩子断链;在钩子里做重初始化(import 锁期);kwargs 语义未文档化。
