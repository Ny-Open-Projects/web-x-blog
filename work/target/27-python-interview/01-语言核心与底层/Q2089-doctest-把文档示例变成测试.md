---
title: [Q2089] doctest:把文档示例变成测试
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2089 · doctest:把文档示例变成测试

> 难度:★★★☆☆ | 标签:doctest, 文档, 测试

**问**:docstring 里的 >>> 示例怎么能自动验证?doctest 有哪些匹配规则要知道?

**答**:doctest 把 docstring 中的 >>> 行当输入、后续行当期望输出,doctest.testmod() 扫描模块全部 docstring 逐条重放比对,demo 里三个用例(普通返回、空白归一、异常)零依赖跑完。三条匹配规则:期望输出必须与 repr 逐字一致,包括引号与空格;异常用 Traceback (most recent call last): 头 + 省略的栈体 + 最后一行「类型: 消息」逐字匹配,栈可以缩成 ...;输出顺序敏感,dict 虽有序但别依赖复杂容器打印。适用边界:纯函数的输入输出示例最适合 doctest,有副作用、随机性或环境依赖的场景交给单元测试,两者互补而非替代。

```python
# file: code/01_语言核心与底层/q2089_doctest_basics.py
"""doctest:把文档示例变成可执行测试。"""
import doctest


def slugify(text):
    """把标题转成 slug。

    >>> slugify("Hello World")
    'hello-world'
    >>> slugify("  A  B  ")
    'a-b'
    >>> slugify("")
    Traceback (most recent call last):
        ...
    ValueError: 空文本无法生成 slug
    """
    cleaned = "-".join(text.lower().split())
    if not cleaned:
        raise ValueError("空文本无法生成 slug")
    return cleaned


if __name__ == "__main__":
    fails, total = doctest.testmod(verbose=False)
    print(f"doctest 用例 {total} 个,失败 {fails} 个")
    print("文档即测试:示例与实现一起腐烂或一起存活")
```

**追问**:1) 异常示例怎么匹配?——栈体可省略为 ...,但异常类型与消息行必须逐字一致;什么不适合 doctest?——副作用、随机输出、依赖环境的用例,写进单元测试更稳。2) doctest 的工程位?——文档示例与测试合一,改文档即改测试;ELLIPSIS 标志放宽输出;全局 doctest 模块级示例可测 docstring。3) 与单元测试的分工?——doctest 管「展示契约」(示例必须真实),pytest 管「行为回归」;稳定输出、纯函数的示例适合 doctest。4) 生产陷阱?——示例随代码演化过时(没跑 CI 就失真);输出含字典/集合顺序(哈希序不稳,要 sorted);消息文本改一个字 doctest 就红。
