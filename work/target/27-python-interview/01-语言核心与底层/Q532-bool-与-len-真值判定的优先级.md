---
title: [Q532] __bool__ 与 __len__:真值判定的优先级
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q532 · __bool__ 与 __len__:真值判定的优先级

> 难度:★★☆☆ | 标签:魔术方法, 布尔

**问**:if obj 的真值判定顺序是什么?自定义容器「空即假」怎么实现?

**答**:bool(obj) 的顺序:1) 类型定义了 __bool__ 就用它(必须返回 bool);2) 否则用 __len__(返回 0 为假);3) 都没有则一律真。两者都定义时 __bool__ 优先。这个机制支撑了 `if items:` 比 `if len(items) > 0:` 更 Pythonic 的写法。陷阱:__bool__ 里做昂贵计算(查询数据库判断「有没有」)会让每个 if 都付出代价;语义上「非空即真」用 __len__,语义上「状态开关」用 __bool__,不要混。

```python
# file: code/01_语言核心与底层/q532_bool_len.py
class Queue:
    def __init__(self, items):
        self._items = list(items)

    def __len__(self):
        print("  __len__ called")
        return len(self._items)

    def push(self, x):
        self._items.append(x)

    def pop(self):
        return self._items.pop(0)

class AlwaysTrue:
    def __len__(self):
        return 0

    def __bool__(self):
        return True                       # __bool__ 优先于 __len__

if __name__ == "__main__":
    q = Queue([])
    print("empty:", bool(q))              # 回退 __len__ → 0 → False
    q.push("job")
    print("nonempty:", bool(q))
    if q:
        print("if q: truthy branch")

    print("bool wins over len:", bool(AlwaysTrue()))
    print("default is truthy:", bool(object()))
```

**追问**:1) __bool__ 返回非 bool 值会怎样?——CPython 直接抛 TypeError("__bool__ should return bool, returned ..."),解释器不做静默转换;契约上必须返回 bool。2) 真值判定的完整优先级?——PyObject_IsTrue 先查 __bool__,缺省看 __len__(0 为假),两者都没有则恒真;bool(x)、if x、and/or、while 全走同一条路径。3) 底层槽位?——tp_as_number.nb_bool 与 tp_as_sequence.sq_length 两个槽;__bool__ 与 __len__ 同时定义时前者赢——语义要一致,否则 truthiness 不可预测。4) 生产陷阱?——空容器 len 为 0 但 __bool__ 返回 True 的自相矛盾实现;pandas 的 DataFrame 故意在 __bool__ 抛 ValueError 防歧义真值,提示「用 any/all」;自定义容器漏 __len__ 导致空对象为真。
