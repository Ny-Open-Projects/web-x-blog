---
title: [Q1803] keyword-only 与 positional-only:API 演进的安全阀
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1803 · keyword-only 与 positional-only:API 演进的安全阀

> 难度:★★★☆☆ | 标签:参数设计, API, 兼容性

**问**:`/` 和 `*` 把参数分成三段,各解决什么问题?怎么用于 API 演进?

**答**:`def f(a, /, b, *, c)` 三段:斜杠前只能按位置、星号后只能按关键字,中间两可。工程价值在演进的「安全阀」:① 新参数一律放 `*` 之后(keyword-only),已有位置调用零破坏——若 role 是普通参数,上游 f(name, role) 写死后,再想插一个参数就得全局改调用点;② 会被重命名的参数加 `/`(positional-only),调用方无法按名耦合,内部改名不破坏兼容,也避免参数名与常见关键字撞车(如 open 早期的 file/buffer);③ inspect.signature 能完整读出两类标记,校验器与绑定逻辑不丢信息(Q498)。PEP 570(3.8)与 PEP 3102 各管一头,Q1273 讲 dataclass 的 kw_only 版本,本题是函数签名层的基础设施。

```python
# file: code/01_语言核心与底层/q1803_kw_only_params.py
"""keyword-only 与 positional-only:API 演进的安全阀。"""
import inspect


def create_user(name, /, *, role="member", active=True):
    # / 之前只能按位置;* 之后只能按关键字
    return {"name": name, "role": role, "active": active}


def legacy(name, role="member"):
    return {"name": name, "role": role}


if __name__ == "__main__":
    print("正常调用:", create_user("alice", role="admin"))
    try:
        create_user(name="bob")          # name 是 positional-only
    except TypeError as e:
        print("按关键字传 name:", str(e)[:48])
    try:
        create_user("carol", "admin")    # role 是 keyword-only
    except TypeError as e:
        print("按位置传 role:", str(e)[:48])
    print("签名自省:", str(inspect.signature(create_user)))
    print("旧接口兼容:", legacy("dave"))
```

**追问**:1) positional-only 还能防什么?——防调用方依赖参数名做关键字展开,从而锁死重命名与 kwargs 二次转发的自由度。2) 两个安全阀的分工?——/ 锁死位置(参数名是实现细节,内置 len(len(obj) 不能写 obj=)的姿势);* 锁死关键字(布尔/开关参数命名传,防位置错位);两者可同用:len(obj, /, *, key=None) 风格。3) API 演进策略?——新参数一律 keyword-only + 默认值,旧参数不动;把已发布参数改 pos-only 是破坏性变更,要走版本化。4) 生产陷阱?——布尔位置参数两值对调没人发现;**kwargs 转发链被 pos-only 中断;默认值参数插入位置改变位置实参含义。
