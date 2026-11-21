---
title: [Q5011] PEP 657 精细 traceback 与 add_note
date: 2026-11-18
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5011 · PEP 657 精细 traceback 与 add_note

> 难度:★★★☆☆ | 标签:traceback, PEP 657, 异常诊断

**问**:3.11 的 traceback 输出和 3.10 以前比多了什么?线上日志里 `add_note` 能解决什么定位难题?它的代价是什么?

**答**:PEP 657 让 traceback 的每一帧都带精确列号(`^` 不再指向整行,而是指向出错的那个表达式),多调用链(如 `f(g(x))` 嵌套)会显示两行注释分别标注;3.11 同时引入 `BaseException.add_note()`,把「第几行数据、哪个请求」这类上下文直接挂在异常上,随 traceback 一起输出,而不用在各层 catch 里拼日志字符串。代价有两点:异常对象的 `__notes__` 会被 pickle/序列化忽略(不保证跨进程保留);note 是「只增不减」的列表,同一异常被反复上抛、多层补 note 时会越滚越长,需要约定在「离现场最近的一层」补一次。

```python
import traceback


def parse(row):
    return int(row["amount"])


def run(rows):
    for i, r in enumerate(rows):
        try:
            parse(r)
        except ValueError as e:
            e.add_note(f"rows[{i}] = {r!r}")  # 3.11+: 给异常附加上下文笔记
            raise


rows = [{"amount": "12"}, {"amount": "x"}]
try:
    run(rows)
except ValueError:
    tb = traceback.format_exc()
    print(tb)
    # 3.11+ 的 traceback 文本带精确列号(^ 指向具体表达式)
    print("含列号指示:", "^^^" in tb or "^" in tb)
```

**追问**:1) `add_note` 和把上下文放进异常 message 有什么本质区别?——message 会改变异常类型判断(日志里 `str(e)` 变长、上游 `except` 匹配不受影响但报错聚合/告警按类型归并时会拿到拼接后的文本);note 存在 `__notes__`,不污染 `str(e)`,适合机器归并 + 人读两层分工。2) 3.13/3.14 在这条线上还有哪些演进?——`traceback.TracebackException` 支持从 note 生成结构化输出;配合 PEP 678 的 ExceptionGroup,可以对组内每个子异常分别附 note,故障聚合场景(一次批量操作 100 个子任务)能逐项标注。

