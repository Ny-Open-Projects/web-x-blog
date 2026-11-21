---
title: [Q5023] match 语句深水区：PEP 634 的模式语义边界
date: 2026-11-20
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5023 · match 语句深水区：PEP 634 的模式语义边界

> 难度:★★★★☆ | 标签:PEP 634, match, 3.10+

**问**：`match/case` 不是 switch。九种模式（字面量、捕获、通配、值、序列、映射、类、或、守卫）的匹配语义各是什么？最容易踩的两个坑——"裸名值模式变成捕获"与"不可反驳模式遮蔽后续分支"——怎么防？

**答**：核心语义三条。1) **捕获模式**：`case x:` 是"绑定新变量"，任何值都匹配（不可反驳）；想要"等于某常量"必须用**值模式**——点号路径（`Cmd.RUN`、`Color.RED`）或 `case str() as s:` 这类类模式。裸名拼错（`case Run:`）不报错，只会悄悄新建变量并吞掉该分支。2) **序列/映射模式**：序列按形状匹配（`[a, *mid, z]`），映射是**子集匹配**——只要求列出的键存在，多余键无视（`**rest` 收集），与 `dict ==` 全等语义不同。3) **类模式**：`Job(name, size)` 按位置属性解构，位置参数由 `__match_args__` 决定（dataclass 自动生成，普通类要手写），关键字模式 `Job(name="x")` 直接按属性名取。守卫 `if size > 100` 不匹配会继续尝试下一分支；**不可反驳模式必须放最后**，否则后面分支永远不可达（静态检查器会警告 unreachable）。

```python
# file: code/01_语言核心与底层/q5023_match_semantics.py
from dataclasses import dataclass

class Cmd:
    RUN = "run"
    STOP = "stop"

@dataclass
class Job:                       # dataclass 自动生成 __match_args__ = ("name", "size")
    name: str
    size: int

def dispatch(msg):
    match msg:
        case {"op": Cmd.RUN, "job": Job(name, size), **rest}:
            return f"run {name} size={size} extra={sorted(rest)}"
        case {"op": Cmd.STOP, "job": str() as jid} if jid.startswith("job-"):
            return f"stop {jid}"
        case ["stop", *targets]:              # 序列模式 + 星号收集中段
            return f"batch-stop {targets}"
        case _:
            return "unknown"

print(dispatch({"op": "run", "job": Job("build", 8), "by": "ci"}))
print(dispatch({"op": "run", "job": {"name": "x", "size": 1}}))   # dict 不是 Job -> 落空
print(dispatch({"op": "stop", "job": "job-7"}))
print(dispatch({"op": "stop", "job": "other"}))                   # 守卫不匹配 -> unknown
print(dispatch(["stop", "a", "b", "c"]))

def pitfall(msg):
    match msg:
        case cmd:                 # 捕获模式:不可反驳,任何值都进来!
            return f"captured {cmd!r}"
print("裸名模式把 'run' 当变量捕获:", pitfall("run"))            # 不是值比较!

def value_pattern(msg):
    match msg:
        case Cmd.RUN:             # 点号路径 -> 值模式,真正做相等比较
            return "hit RUN"
    return "miss"
print("值模式比较:", value_pattern("run"), "/", value_pattern("other"))
```

**追问**：1) 映射模式的键必须是字面量吗？——必须是字面量或点号值模式（要保证 hash 与先求值），不能是运行时变量名；要动态键就得先转成序列或用守卫。2) 普通类怎么用位置类模式？——类属性 `__match_args__ = ("x", "y")` 声明位置序，或只用关键字模式 `Point(x=1)`；`__match_args__` 缺位还用位置参数会抛 TypeError。3) 穷尽性检查和 match 什么关系？——mypy/pyright 对 match 枚举/Literal 联合可推不可达，配合 `assert_never`（Q1274）能把漏分支变成静态错误；运行时仍要 `_` 兜底。

## 背诵要点
1. 裸名 `case x:` = 捕获（任何值都匹配）；比常量要用点号值模式 `case Cmd.RUN:`。
2. 映射模式是子集匹配（`**rest` 收尾）；序列模式支持 `*mid` 中段收集。
3. 类模式位置解构看 `__match_args__`（dataclass 自动生成）；守卫失败继续下一分支，不可反驳模式必须最后。

## 复盘追问
1. 把一坨 if/elif 分派重构为 match，怎么保证没改变行为？（提示：先锁特征测试（Q2647），逐分支对照语义差——尤其原 `==` 全等与映射子集匹配的差异）
2. `case {"op": op, "job": job}:` 里 op/job 是捕获还是比较？线上怎么防这类误写？（提示：捕获；靠 review + 类型检查器的 unreachable/绑定告警 + 值模式用枚举常量）
