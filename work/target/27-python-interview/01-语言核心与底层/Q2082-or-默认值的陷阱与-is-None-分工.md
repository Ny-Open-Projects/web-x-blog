---
title: [Q2082] or 默认值的陷阱与 is None 分工
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2082 · or 默认值的陷阱与 is None 分工

> 难度:★★★☆☆ | 标签:or, falsy, 默认值

**问**:`config.get("timeout") or 30` 有什么问题?正确的缺省写法是什么?

**答**:or 的语义是「左侧为 falsy 就取右侧」,而 falsy 家族不止 None——0、0.0、空串、空容器、False 全部命中(Q532 的真值规则)。timeout=0 是合法业务值却被悄悄换成 30,这就是经典事故。精确表达「缺失才用默认」必须用 is None:先取值,值为 None(键不存在且没给默认)才落默认值。or 写法只在一种情况下成立:falsy 值与缺失语义本来就一致,比如 name or "guest" 把空串当未填名。记住分工:is None 表达「缺失」,or 表达「空值无所谓」,两者不可互相替代。

```python
# file: code/01_语言核心与底层/q2082_or_default.py
"""or 默认值的陷阱:falsy 值会被误替换,is None 才是精确判断。"""


def timeout_or(config):
    return config.get("timeout") or 30         # 0 也会被换成 30


def timeout_none(config):
    value = config.get("timeout")
    return 30 if value is None else value      # 只有缺失才用默认


if __name__ == "__main__":
    for cfg in ({}, {"timeout": 0}, {"timeout": ""}, {"timeout": 5}):
        print(cfg, "-> or 写法:", timeout_or(cfg), "| is None 写法:", timeout_none(cfg))
    print("falsy 家族:", [bool(v) for v in (0, 0.0, "", [], {}, set(), None)])
    print("结论:缺失语义用 is None;or 只用于空值与缺失本就等价的场景")
```

**追问**:1) 什么时候 or 默认值可接受?——falsy 值与缺失语义一致时,如空串本就该当缺省名;与哨兵设计什么关系?——同一思想的两级实现,公开 API 用 None 够用,内部有歧义才上专用哨兵单例,见 Q1282。2) or 的陷阱清单?——0、""、[]、False 全被当「缺失」覆盖:name or "anon" 会把空名覆盖、count or default 把 0 覆盖;需要区分「0 合法」就必须 is None。3) 分工模型?——or:业务上 falsy 即缺失;is None:None 即缺失、0/空串合法;专用哨兵:None 本身也是合法值(Q1282 三级语义)。4) 生产陷阱?——金额/计数用 or 默认被 0 吞;布尔参数 or 默认;链式 or 默认值表达式带副作用重复执行。
