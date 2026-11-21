---
title: [Q465] NewType、TypeAlias 与 cast
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q465 · NewType、TypeAlias 与 cast

> 难度:★★★☆ | 标签:typing, NewType

**问**:NewType("UserId", int) 和直接用 int 注解相比,防住了什么?cast 的适用边界在哪?

**答**:NewType 创建「零成本的独立类型」:UserId(42) 才是 UserId,裸 int 不能直接传给要 UserId 的函数,防止把语义不同的整数混用(用户 id 当订单号传);运行时它就是个恒等函数,没有子类化开销。类型别名(X = list[int])纯粹是缩短长注解,两边完全等价可互换。cast(T, v) 是「我比你懂」的显式断言:静态检查器信你,运行时原样返回第二参;只应用于确实无法证明的场景(如来自外部 JSON 的数据),滥用等于关掉类型检查。

```python
# file: code/01_语言核心与底层/q465_newtype_cast.py
from typing import NewType, cast

UserId = NewType("UserId", int)
OrderNo = NewType("OrderNo", int)
IdList = list[int]                        # 类型别名

def get_name(uid: UserId) -> str:
    return f"user-{uid}"

def first(items: IdList) -> int:
    return items[0]

if __name__ == "__main__":
    raw = 42
    print(get_name(UserId(raw)))          # 显式构造:语义转换点清晰
    print(get_name(OrderNo(raw)))         # mypy 报错:OrderNo 不是 UserId
    print(first([1, 2, 3]))

    payload = {"id": 7}
    uid = UserId(cast(int, payload["id"]))   # 外部数据:cast 声明假设
    print(get_name(uid))
```

**追问**:1) NewType 与继承 int 定义子类的区别?——NewType 不创建类、零运行时开销、不能加方法;子类是真实类型可扩展行为但参与 issubclass,按需选择。2) cast 的适用边界?——只用于「确实无法静态证明」的场景:外部 JSON 字段、测试桩、第三方无注解 API;滥用等于关掉类型检查,review 里 cast 出现处必须注释理由。3) NewType 的运行时形态?——3.10 起 NewType 是类,调用 UserId(42) 原样返回参数(恒等函数),不创建对象不做检查;对它做 isinstance 直接 TypeError,因为它不在真实类层次里。4) 生产陷阱?——用 NewType 划分语义后忘了在系统边界做构造(UserId(raw) 调用点),裸 int 仍然四处流;边界转换点要集中,否则 NewType 只是心理安慰。
