---
title: [Q469] ExceptionGroup 与 except*
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q469 · ExceptionGroup 与 except*

> 难度:★★★★★ | 标签:异常, ExceptionGroup

**问**:并发任务同时抛多个异常时,ExceptionGroup 如何表达和拆分?except* 与 except 的语义差别?

**答**:ExceptionGroup(msg, [exc1, exc2, ...]) 把多个不相关的异常打包成一个可抛出对象,3.11 引入,配套语法 except* 按类型「拆包」:每个 except* 分支独立匹配组内的子异常,命中的子集构成新组交给分支,未命中的随原组继续传播;多个 except* 分支可以各自命中一次,这与普通 except「至多命中一个」根本不同。典型场景:asyncio.TaskGroup 聚合所有子任务异常、批量处理收集每个条目的失败。except* 分支内的 eg.exceptions 是命中的子异常元组。注意 ExceptionGroup 与 except* 均为 3.11+ 引入,且 except* 是新语法(低版本解释器连源码都无法解析),低版本运行演示文件时打印说明并跳过。

```python
# file: code/01_语言核心与底层/q469_exception_group.py
import sys

def batch_process(items):
    errors = []
    results = []
    for i, item in enumerate(items):
        try:
            if item < 0:
                raise ValueError(f"negative item {i}")
            results.append(item * 2)
        except ValueError as e:
            errors.append(e)
    if errors:
        raise ExceptionGroup("batch failed", errors)   # 3.11+
    return results

if __name__ == "__main__":
    if sys.version_info < (3, 11):
        print(f"该特性需要 Python 3.11+,当前 {sys.version_info.major}.{sys.version_info.minor},演示跳过")
        sys.exit(0)

    # except* 是 3.11 新语法,只能放在字符串里按需编译执行
    demo = """
try:
    batch_process([1, -2, 3, -4])
except* ValueError as eg:
    print("value errors:", [str(e) for e in eg.exceptions])
except* TypeError as eg:
    print("type errors:", [str(e) for e in eg.exceptions])
"""
    exec(demo, globals())

    eg = ExceptionGroup("mixed", [ValueError("v"), TypeError("t")])
    print(type(eg).__name__, len(eg.exceptions))
    print("group message:", eg.message)
```

**追问**:1) except* 分支里能不能重新抛出部分异常?——可以,raise 后未处理的子异常会被重新打包传播;另外 except* 不允许捕获 BaseException 整组,防止吞掉 KeyboardInterrupt 之类的取消信号。2) except* 与 except 的执行模型差异?——每个 except* 分支独立匹配一次,命中的子集打包成新组传入,分支结束后剩余子异常重新组合继续传播;except 至多命中一个。except* 分支里 break/continue/return 是语法错误,因为组必须走完重新组合流程。3) TaskGroup 怎么用它?——子任务异常被收集、兄弟任务被取消,退出时把全部异常打包成一个 ExceptionGroup(可嵌套)从 __aexit__ 抛出;gather(return_exceptions=True) 按完成序返回异常对象、不取消兄弟,语义完全不同。4) 生产陷阱?——低版本解释器遇到 except* 源码直接 SyntaxError,多版本部署要先做版本断言;except Exception 捕到 ExceptionGroup 后当单异常处理会丢失子异常上下文,要拆 eg.exceptions。
