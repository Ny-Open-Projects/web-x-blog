---
title: [Q1819] contextlib.suppress:精确吞异常的语义与边界
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1819 · contextlib.suppress:精确吞异常的语义与边界

> 难度:★★☆☆☆ | 标签:suppress, 异常, EAFP

**问**:except KeyError: pass 与 with suppress(KeyError) 等价吗?什么时候用哪个?

**答**:语义等价,表达力不同:suppress 声明了「这里预期会吞哪些异常」的意图,一行搞定,成功路径自然外移;适合 EAFP 风格的小动作——删可能不存在的文件、读可能缺的键。边界两条:① 只吞声明的具体类型,suppress(Exception) 是坏味道,程序 bug(ZeroDivisionError、AttributeError)会被静默吞掉;② 它不改变异常的成本语义——异常构建与栈展开仍然昂贵,热路径高频「预期失败」该用 .get/.exists 查询(Q1839 实测),suppress 是控制流表达工具、不是性能工具。与 Q471 的 warnings 治理同方向:静默必须显式、可枚举、可审查。

```python
# file: code/01_语言核心与底层/q1819_suppress.py
"""contextlib.suppress:精确吞异常的语义与边界。"""
import os
from contextlib import suppress


def remove_quiet(path):
    with suppress(FileNotFoundError):
        os.remove(path)
        return "已删除"
    return "文件本来就不存在"


def too_broad():
    # 反例:suppress(Exception) 连程序 bug 一起吞掉
    with suppress(Exception):
        1 / 0
        return "不会到这里"
    return "ZeroDivisionError 也被吞了"


def narrow_only():
    with suppress(KeyError):
        {}["missing"]
        return "不会到这里"
    return "只吞声明的类型"


if __name__ == "__main__":
    print(remove_quiet("/tmp/q1819_definitely_missing.bin"))
    print(too_broad())
    print(narrow_only())
```

**追问**:1) suppress 里代码执行一半后吞了异常,状态怎么办?——吞异常不回滚副作用;要「要么全成功要么别跑」得靠事务设计(Q1818),suppress 只管异常不打扰外层。2) suppress 的语义边界?——精确类型元组(可多类型),等价「__exit__ 判类型返回 True」;可重入;与裸 except 的差别是「明确声明的例外清单」。3) 与 try/except 的取舍?——「缺失是正常的」(os.remove 清理、键不存在)用 suppress 表达意图;需要分支处理(记日志/降级)用 except。4) 生产陷阱?——suppress(Exception) 吞一切掩盖 bug;吞掉的副作用残留(文件已建一半);在长事务里 suppress 让部分失败不可见。
