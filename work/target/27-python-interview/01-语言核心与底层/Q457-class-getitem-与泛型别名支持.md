---
title: [Q457] __class_getitem__ 与泛型别名支持
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q457 · __class_getitem__ 与泛型别名支持

> 难度:★★★☆ | 标签:元编程, typing

**问**:为什么 `list[int]` 在运行时是合法表达式?自定义类如何支持同样的 `[]` 语法?

**答**:类方查找 `Cls[item]` 时解释器调用的是元类上的 `__getitem__`,而实例级没有对应操作;PEP 560 引入 `__class_getitem__` 作为「类上的 __getitem__」,让任何类都能响应下标。内置容器用它返回 types.GenericAlias(几乎零成本),配合静态检查器表达泛型;自定义类同样可以实现它来构建「参数化类」的 API,比如 `Repository[User]` 返回绑定实体类的子类。注意它定义在类上、通过类访问时触发,与元类 __getitem__ 的触发路径不同。

```python
# file: code/01_语言核心与底层/q457_class_getitem.py
class Repository:
    """支持 Repository[Entity] 的参数化语法"""
    _bound = {}

    def __class_getitem__(cls, entity):
        key = (cls, entity)
        if key not in Repository._bound:
            name = f"{cls.__name__}[{entity.__name__}]"
            Repository._bound[key] = type(name, (cls,), {"entity": entity})
        return Repository._bound[key]

class User:
    pass

class Order:
    pass

if __name__ == "__main__":
    UserRepo = Repository[User]
    OrderRepo = Repository[Order]
    print(type(UserRepo).__name__, UserRepo.entity)
    print(issubclass(UserRepo, Repository))
    print(UserRepo is Repository[User])   # 同参数返回同一子类
    print(UserRepo is OrderRepo)
```

**追问**:1) list[int] 返回的 GenericAlias 能实例化吗?——能,`list[int]()` 就是普通 list;运行时它不做事,只是给 mypy 看的「带参数的别名」。2) 与元类 __getitem__ 的区别?——__class_getitem__ 定义在普通类上、由解释器在类下标时调用,PEP 560 让不写元类也能支持 [];元类方案会卷入元类继承冲突,能不用就不用。3) GenericAlias 的运行时反射?——__origin__/__args__ 记录来源与参数,3.10+ 支持 isinstance(x, list[int]) 这类检查;实例化与运算委托给 origin,本质是轻量元数据壳。4) 生产陷阱?——__class_getitem__ 里每次请求动态建子类又不缓存,类对象无限增长;以及把 GenericAlias 传给需要真实类型的 C 扩展 API(某些 ORM)报错,要取 __origin__ 再传。
