---
title: [Q2374] 返回契约三选一:None、raise 与空对象
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2374 · 返回契约三选一:None、raise 与空对象

> 难度:★★★★☆ | 标签:API 设计, 错误处理, 空对象模式

**问**:查询函数找不到结果,该返回 None、抛异常还是返回空对象?

**答**:三种契约对应三种「缺失」语义。返回 None:缺失是常态且调用方必然要检查时用(如 dict.get),风险是 None 会向远处传播,AttributeError 在几十行外爆炸;约定俗成的补救是调用方立即 `or 默认值` 或显式 is None 判断。抛特定异常(LookupError 子类):缺失意味着违反前置条件、继续执行就是错误时用,异常携带上下文、调用栈清晰,代价是控制流变重。空对象(Null Object):缺失时也要「继续跑」的场景用,返回与真实对象同接口的空实现(访客用户、空列表),调用方零判断,代价是多一个类且「什么都没查到」被静默化,可观测性下降。选型口诀:调用方必然处理缺失用 None;缺失即异常用 raise;调用方不该关心缺失用空对象。同一模块内三种风格混用是最伤 API 一致性的错误。

```python
# file: code/01_语言核心与底层/q2374_return_contract.py
"""返回契约三选一:None、raise 与空对象各自的适用场景。"""


class _User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"你好,{self.name}"


_USERS = {"u1": _User("张三")}


def find_user_none(uid):
    """缺失是常态:返回 None。"""
    return _USERS.get(uid)


class _Guest:
    """空对象:与真用户同接口,行为安全默认。"""
    name = "访客"

    def greet(self):
        return f"你好,{self.name}"


def find_user_null(uid):
    return _USERS.get(uid, _Guest())


class NotFoundError(LookupError):
    pass


def find_user_strict(uid):
    user = _USERS.get(uid)
    if user is None:
        raise NotFoundError(f"user {uid!r} 不存在")
    return user


if __name__ == "__main__":
    print("None 式:", find_user_none("u9"))

    guest = find_user_null("u9")
    print("空对象式:", guest.greet())
    print("命中真实用户:", find_user_null("u1").greet())

    try:
        find_user_strict("u9")
    except NotFoundError as exc:
        print("raise 式:", exc)

    try:
        find_user_none("u9").name
    except AttributeError as exc:
        print("None 式延迟爆炸:", exc)
```

**追问**:1) 空对象和 default 参数怎么配合?——`get(key, _Guest())` 一步到位,但注意默认参数求值时机:每次调用都新建空对象没问题,可变默认对象则会被共享修改。2) 三种契约的选型?——None:缺席是常态;raise:缺席是错误(强契约);空对象(Nil Object):缺席有「默认行为」——按调用方需求定;混合时文档写清(Q2374 呼应)。3) 空对象的设计要点?——实现与真对象相同的接口、行为无副作用;与哨兵区别:哨兵用于「内部判别」,空对象用于「返回给调用方直接用」。4) 生产陷阱?——可变默认参数共享(Q2085);None 穿透到深层调用链(层层判空);空对象行为不完整被当真对象用。
