---
title: [Q1830] dataclasses.replace:冻结对象的派生修改
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1830 · dataclasses.replace:冻结对象的派生修改

> 难度:★★☆☆☆ | 标签:dataclass, replace, 不可变

**问**:配置对象 frozen=True 之后想「改一个字段」,正确姿势是什么?

**答**:dataclasses.replace(obj, **changes) 调用生成的 __init__ 复制出改了指定字段的新实例,原对象不动——frozen 对象的「修改」全部走它,与 Q468 的冻结哈希语义配套。三条纪律:① replace 只接受真实字段名,传错字段当场 TypeError,比手写构造器安全;② 「相对修改」先读旧值:bump_port(cfg) 里 replace(cfg, port=cfg.port + delta);③ 派生链可组合:promote_debug(bump_port(base)) 每步产生新对象,管道式演进,审计与回滚都容易。与手写 copy+setattr 相比,replace 对 InitVar、default_factory 字段都按 __init__ 语义处理,不会绕过 __post_init__ 的派生与校验逻辑(Q466)。

```python
# file: code/01_语言核心与底层/q1830_dc_replace.py
"""dataclasses.replace:冻结对象的派生修改。"""
from dataclasses import dataclass, replace


@dataclass(frozen=True)
class Config:
    host: str = "localhost"
    port: int = 8000
    debug: bool = False


def promote_debug(cfg):
    return replace(cfg, debug=True)          # 返回新实例,原对象不动


def bump_port(cfg, delta=1):
    return replace(cfg, port=cfg.port + delta)


def unknown_field_check(cfg):
    try:
        replace(cfg, nope=1)
    except TypeError as e:
        return str(e)[:44]
    return "没有报错?"


if __name__ == "__main__":
    base = Config()
    prod = bump_port(promote_debug(base), delta=1000)
    print("原对象:", base)
    print("派生对象:", prod)
    print("frozen 不可写:", end=" ")
    try:
        base.port = 1
    except Exception as e:
        print(type(e).__name__)
    print("未知字段报错:", unknown_field_check(base))
```

**追问**:1) replace 会触发 __post_init__ 吗?——会,它走 __init__,派生字段与校验逻辑照常执行,这正是它优于手工拷贝的原因。2) replace 的字段语义?——只传要改的字段,其余从原实例带过;类型检查在静态层收窄(字段名拼错 mypy 报);InitVar 字段也要重新传,漏传报错。3) 与冻结语义的配合?——frozen 实例的「修改」全部表达为 replace 派生(Q468);值语义对象可安全共享、可做 dict key;嵌套派生逐层 replace。4) 生产陷阱?——手工 copy + setattr 绕过 frozen 与校验;replace 漏传 InitVar;嵌套结构的深层 replace 直接给共享内层对象赋引用(浅层派生)。
