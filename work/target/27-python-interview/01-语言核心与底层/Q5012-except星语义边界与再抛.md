---
title: [Q5012] except* 语义边界:嵌套、再抛与未匹配子组去向
date: 2026-11-18
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5012 · except* 语义边界:嵌套、再抛与未匹配子组去向

> 难度:★★★★☆ | 标签:PEP 654, ExceptionGroup, 异常处理

**问**:`except*` 和 `except` 的根本区别是什么?在 `except*` 分支里裸 `raise` 会抛出什么?未匹配的子异常会不会丢失?

**答**:三个硬区别。第一,`except*` 是按「子异常类型」分组匹配:组内每个子异常独立判断,同一组可以被多个 `except*` 分支各摘走一部分,而 `except` 只命中第一个匹配的类型。第二,匹配是「拷贝语义」:分支拿到的 `eg.exceptions` 是匹配子集,分支结束后未匹配的部分继续按组传播——不会丢失。第三,最反直觉的是裸 `raise`:在 `except*` 分支里裸 `raise` 重新抛出的是**整个原始组(含已被本分支处理过的子异常)**,而不是剩余部分;想只抛剩余部分就不要再抛,想让上层看到全部就裸 raise。另外同一 try 块禁止 `except` 与 `except*` 混用,`except*` 分支里也不允许 `continue/break/return` 半途吞掉组。

```python
def main():
    try:
        raise ExceptionGroup("g", [TypeError("t1"), ValueError("v2")])
    except* ValueError as eg:
        print("分支捕获:", [type(e).__name__ for e in eg.exceptions])
        raise  # 裸 raise:把未匹配部分(TypeError)继续按组上抛


try:
    main()
except ExceptionGroup as eg:
    print("顶层剩余:", [type(e).__name__ for e in eg.exceptions])

# 嵌套 except*:内层 raise eg 把整组(含已处理的 ValueError)再抛给外层
try:
    try:
        raise ExceptionGroup("inner", [ValueError("v"), OSError("o")])
    except* ValueError as eg:
        print("内层:", [type(e).__name__ for e in eg.exceptions])
        raise eg
except* OSError as eg:
    print("外层 OSError:", [type(e).__name__ for e in eg.exceptions])
except* Exception as eg:
    print("外层剩余(重复出现的 ValueError 也在这):", [type(e).__name__ for e in eg.exceptions])
```

**追问**:1) 实测里裸 raise 后顶层为什么还能看到 ValueError?——PEP 654 规定裸 `raise` 重抛完整原始组;对照实验是分支里不再抛,顶层只会收到 `[TypeError]`。所以「分支处理完还想让上层感知失败」必须显式重新组包(`raise ExceptionGroup(...)`)而不是裸 raise。2) TaskGroup 里怎么和 `except*` 配合?——`async with asyncio.TaskGroup()` 收集所有子任务异常后抛出 `ExceptionGroup`(TaskGroup 的实现保证无并发异常时直接抛单个异常,不组包);调用端用 `except* ValueError` 摘出业务失败、`except* asyncio.CancelledError` 单独处理取消,比在 except 里遍历 `eg.exceptions` 手写过滤更清晰。3) 为什么 except* 里不能 `return`?——组语义要求「所有子异常都被明确处置或传播」,半途 return 等于吞掉未匹配分支,语言层直接禁止。

