---
title: [Q2365] finally 里的 break 与 continue
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2365 · finally 里的 break 与 continue

> 难度:★★★☆☆ | 标签:finally, 控制流, 陷阱

**问**:finally 里写 return 或 break 会发生什么?为什么规范禁止这么写?

**答**:finally 的定位是「无论 try 怎么收场都执行」,但它在 3.8 之前允许改写控制流:finally 里的 return 会覆盖 try 的返回值,finally 里的 break/continue 会改变所在循环的走向——try 里本来要返回的值、要传播的异常都被静默丢弃,结果与读代码的人的直觉完全相反。CPython 3.8 起,finally 中的 return/break/continue 会产生 SyntaxWarning,等于官方宣布这是反模式。规范的写法:finally 只做清理(关文件、释放锁、恢复状态),绝不放 return、break、continue,也不该抛新异常——清理代码抛异常会吞掉正在传播的原异常。需要「清理并替换结果」时,显式在 finally 之后写 return;需要清理失败可感知,用 contextlib 或显式 try/except 包清理段。

```python
# file: code/01_语言核心与底层/q2365_finally_flow.py
"""finally 里的 return/break/continue:会覆盖 try 的既定走向。"""


def with_break_in_finally():
    for i in range(3):
        try:
            if i == 1:
                continue
            print("  body:", i)
        finally:
            if i == 2:
                print("  finally 决定 break")
                break
    return "循环结束"


def with_return_in_finally():
    try:
        return "try 的返回"
    finally:
        return "finally 的返回"       # 覆盖前者


if __name__ == "__main__":
    print(with_break_in_finally())
    print(with_return_in_finally())

    log = []

    def clean_version():
        try:
            log.append("工作")
            return "结果"
        finally:
            log.append("清理")        # 只清理,不改控制流

    print(clean_version(), log)
```

**追问**:1) finally 里抛异常会怎样?——新异常替换正在传播的原异常,原异常作为 __context__ 挂在新异常上,但如果没有上层捕获,原始故障现场就丢了;所以清理代码要自己 try。2) break/continue 进 finally 的语义?——从 finally 跳出到循环同样会「覆盖」正在进行的行为(与 return 同级,3.8+ SyntaxWarning);finally 里的控制流语句是 Python 明令劝退的模式(Q526)。3) 嵌套 finally 的展开序?——多层 try 向外展开,每层 finally 依次执行;任何一层的 break/return/新异常都会终止后续展开。4) 生产陷阱?——finally 里做「聪明」控制流让 bug 凭空消失;清理抛错顶掉业务异常;嵌套 finally 层层 return(题干场景)。
