---
title: [Q542] 只有 __getitem__ 的旧式迭代协议
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q542 · 只有 __getitem__ 的旧式迭代协议

> 难度:★★★★ | 标签:迭代器, 兼容

**问**:一个类只有 __getitem__ 没有 __iter__,为什么 for 和 list 都能用它?这个协议何时该淘汰?

**答**:这是 Python 2 之前的「序列协议」遗留:iter(obj) 发现对象没有 __iter__ 时,回退到 seq_iterator——从 obj[0] 开始按下标递增读取,直到 IndexError 判定结束。所以旧式类不写任何迭代方法就能被 for/list/解包消费。但它有三个缺点:不支持无穷序列(IndexError 才停)、无法用 yield 简化、isinstance(x, Iterable) 为 False(协议检查只看 __iter__),类型系统与运行时行为脱节。现代代码一律实现 __iter__ 返回迭代器;__getitem__ 仅作下标访问语义保留。

```python
# file: code/01_语言核心与底层/q542_legacy_iteration.py
from collections.abc import Iterable

class OldStyle:
    """只有 __getitem__:旧式序列协议,依然可迭代"""
    def __getitem__(self, i):
        if i > 2:
            raise IndexError
        return i * i

if __name__ == "__main__":
    o = OldStyle()
    print("for works:", list(o), [x for x in o])
    print("iter + next:", next(iter(o)))

    print("isinstance Iterable:", isinstance(o, Iterable))   # False:协议按 __iter__ 判定
    print("yet iteration works — legacy protocol in action")
```

**追问**:1) 判定「能不能迭代」的正确方法?——不看 isinstance,直接 try iter(obj) except TypeError;或用迭代器协议逐层 Duck typing,这也解释了 Protocol/结构化检查为何更贴近真实行为。2) 旧协议怎么工作?——iter() 找不到 __iter__ 时,对只有 __getitem__ 的对象返回一个「从 0 开始逐个下标、直到 IndexError」的序列迭代器,兼容 2.2 之前的序列类。3) 底层回退路径?——PyObject_GetIter:先查 tp_iter,没有再查 sq_item 槽造旧式迭代器;IndexError 即终止,其他异常照常上抛——异常语义要区分清楚。4) 生产陷阱?——旧协议把业务里的 IndexError 当「迭代结束」吞掉;新代码一律实现 __iter__;判断「可迭代」写 isinstance(obj, Iterable) 对虚拟注册/结构检查的偏差要心里有数。
