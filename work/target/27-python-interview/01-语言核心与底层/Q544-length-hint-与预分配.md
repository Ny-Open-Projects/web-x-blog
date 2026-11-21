---
title: [Q544] __length_hint__ 与预分配
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q544 · __length_hint__ 与预分配

> 难度:★★★☆ | 标签:容器, 优化

**问**:list(generator) 为什么有时候不反复扩容?__length_hint__ 起什么作用?

**答**:list()/tuple()/join 等构造函数在物化可迭代对象前,会先问 `operator.length_hint(it)`(依次查 __length_hint__、__len__):有可靠提示就按它预分配底层缓冲,无提示则从空表开始按 1.125 倍扩容摊还。自定义迭代器实现 __length_hint__(返回估计值,允许不准)能让物化少几次 realloc;生成器的 length_hint 恒为 0(无法预知),所以 list(gen) 通常比 list(已知长度的序列)多几次扩容——这也是「能传序列不传生成器」的微优化依据之一。提示错了不会报错,只影响性能。

```python
# file: code/01_语言核心与底层/q544_length_hint.py
import operator

class Countdown:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return iter(range(self.n, 0, -1))

    def __length_hint__(self):
        return self.n                     # 提示:大约 n 个,允许不准

if __name__ == "__main__":
    c = Countdown(5)
    print("length_hint:", operator.length_hint(c))
    print("materialized:", list(c))
    print("hint of plain generator:", operator.length_hint(x for x in range(3)))
```

**追问**:1) length_hint 返回错误值会怎样?——预分配偏小只多扩容几次,偏大浪费一点内存;协议明确「提示仅供参考」,实现不得依赖其正确性,这正是它敢叫 hint 的原因。2) 预分配的价值?——list(v) 等构造会先按 hint 估算容量,减少扩容 realloc 次数;生成器没有 hint,list(gen) 只能从默认容量逐步翻倍。3) 回退链?——PyObject_LengthHint:先 __length_hint__,再 __len__,最后默认值;返回负数或抛错时忽略用默认。4) 生产陷阱?——hint 严重虚高一次性分配大内存;依赖 hint 做精确判断的代码本身是错的;性能敏感场景先 `list = []; append` 与 list(gen) 的差异要 profile 而不是猜。
