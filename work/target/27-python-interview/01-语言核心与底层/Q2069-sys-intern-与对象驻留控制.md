---
title: [Q2069] sys.intern 与对象驻留控制
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2069 · sys.intern 与对象驻留控制

> 难度:★★★☆☆ | 标签:intern, 对象池, 内存

**问**:小整数有缓存、短字符串会自动驻留(Q006),那手动控制驻留怎么做?什么时候值得做?

**答**:sys.intern(s) 把字符串放进解释器全局驻留表,返回表内的唯一实例:值相等的字符串经过 intern 后 is 成立、id 唯一。收益场景是「重复字符串海量存在且被长期持有」——比如解析日志、HTTP 方法名、状态机 token,intern 后几万份副本坍缩成几份,省内存顺带加速 == 与 dict 查找(身份相同可短路值比较)。对象池则是同一思想对任意类型的推广:用 __new__ 按参数做规范化,同参数永远返回同一实例,demo 里 Color 就是一个最小可用的规范化池。两个代价要清楚:池对象的可变状态被所有持有者共享;池本身持强引用,不设上限就是泄漏,生产上常配 weakref 值容器(Q2068)做自动淘汰。

```python
# file: code/01_语言核心与底层/q2069_intern_pool.py
"""sys.intern 驻留控制与 __new__ 规范化对象池。"""
import sys

TOKEN_BYTES = [b"GET", b"POST", b"PUT", b"DELETE"]


def make_tokens(n):
    """bytes.decode 每次都产生值相等但身份不同的新字符串。"""
    return [TOKEN_BYTES[i % 4].decode("ascii") for i in range(n)]


class Color:
    """规范化对象池:同参数永远返回同一实例。"""
    _pool = {}

    def __new__(cls, name):
        obj = cls._pool.get(name)
        if obj is None:
            obj = super().__new__(cls)
            obj.name = name
            cls._pool[name] = obj
        return obj


if __name__ == "__main__":
    tokens = make_tokens(20000)
    unique_ids = len({id(t) for t in tokens})
    interned = [sys.intern(t) for t in tokens]
    unique_after = len({id(t) for t in interned})
    print("驻留前不同对象数:", unique_ids, "| 驻留后:", unique_after)
    print("intern 不改值只改身份:", tokens[0] == interned[0], tokens[0] is not interned[0])

    a, b = Color("red"), Color("red")
    print("对象池同参同实例:", a is b, "| 不同参数不同实例:", Color("blue") is not a)
    print("池的代价:状态被共享,且池持强引用,要有上限与淘汰策略")
```

**追问**:1) sys.intern 对任意字符串都安全吗?——语法上都可以,但驻留表随解释器生命周期存活,对不可信的海量用户输入驻留反而扩大驻留表,只对高频固定词汇用;对象池比 intern 强在哪?——不限字符串,且能把规范化逻辑写成业务语义,代价是池化管理要自己负责。2) 自动驻留的边界?——标识符样字符串编译期自动 intern,运行时拼接/切片不自动,需要显式 sys.intern——所以「is 比较拼接结果」不可靠(Q1798)。3) 驻留的收益?——重复字符串共享对象省内存、比较退化为指针相等;协议字段名、状态名等高频词汇收益最大。4) 生产陷阱?——对用户输入 intern 撑大驻留表;依赖「intern 后 is 相等」跨实现;对象池无淘汰策略变泄漏池。
