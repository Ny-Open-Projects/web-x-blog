---
title: [Q1274] 穷尽性检查:Literal 联合与 assert_never
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1274 · 穷尽性检查:Literal 联合与 assert_never

> 难度:★★★☆☆ | 标签:typing, Literal, 防御式

**问**:状态机加了一个新枚举值,怎么让「忘了处理的分支」在静态检查期就报错,而不是上线后静默 fallthrough?

**答**:把取值收窄为 `Literal["fast", "safe", "off"]` 联合,处理函数写成 if/elif 链,最后 else 分支调用 `typing.assert_never(value)`(3.11+):当所有成员都被处理,value 已收窄为 Never,这条语句是死代码;漏了一个成员时 value 不是 Never,静态检查器直接报错——重构加枚举值变成了编译期错误。3.10- 的等价做法是 else 分支 `raise AssertionError` 并在测试里覆盖未知值,配合 mypy 的 exhaustive 检查插件。运行时 assert_never 会真的抛异常,所以它同时是静态哨兵与运行时兜底;注意别与 Q470 的「-O 下 assert 消失」混淆——typing.assert_never 是函数调用,不受 -O 影响。

```python
# file: code/01_语言核心与底层/q1274_exhaustiveness.py
from __future__ import annotations

import sys

Mode = str        # 实际应为 Literal["fast", "safe", "off"]


def handle(mode: Mode) -> str:
    if mode == "fast":
        return "F"
    elif mode == "safe":
        return "S"
    elif mode == "off":
        return "O"
    else:
        # 3.11+: assert_never(mode);这里用运行时兜底保持 3.9 可运行
        raise AssertionError("unhandled mode: %r" % (mode,))


if __name__ == "__main__":
    print("python:", sys.version.split()[0])
    for m in ("fast", "safe", "off"):
        print(m, "->", handle(m))
    try:
        handle("turbo")
    except AssertionError as e:
        print("unhandled:", e)
    if sys.version_info >= (3, 11):
        print("3.11+: typing.assert_never 让漏分支变成静态错误")
```

**追问**:1) match 语句下怎么写?——3.10+ `case _:` 分支放 assert_never(value),配合 Literal/Enum 同样实现穷尽性,且分支顺序无关。2) 穷尽性检查的原理?——mypy 把 if/elif/match 各分支收窄成 Literal 残集,全部覆盖后残集是 Never;assert_never(value) 的参数应为 Never,漏分支时报「Argument has type X」——类型系统替你数分支。3) Never 的地位?——Never(3.11+ typing.Never,旧名 NoReturn)是底类型,任何值都不能赋给它;assert_never 在 3.11+ 进入 typing,3.10- 自写 helper(参数标 NoReturn)。4) 生产陷阱?——新增枚举值没走完 CI 就上线(这正是检查的价值);运行期兜底用 assert_never 在 -O 下消失,要 raise 版本;Literal 与 Enum 混用导致收窄对不上。
