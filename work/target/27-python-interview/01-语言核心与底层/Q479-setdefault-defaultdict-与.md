---
title: [Q479] setdefault、defaultdict 与 Counter 的默认值模式
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q479 · setdefault、defaultdict 与 Counter 的默认值模式

> 难度:★★☆☆ | 标签:字典, collections

**问**:统计与分组场景下,setdefault、defaultdict、Counter 各适合什么时机?defaultdict 有什么隐蔽副作用?

**答**:Counter 是计数的终极答案,most_common 直接给出 Top-N;分组用 defaultdict(list) 最简洁——缺键时自动建列表;setdefault 适合「一次取回可能已存在的值」的场景,它总是先构造默认值再判断,热路径略亏且只能用于「取回已有容器」这一种模式。defaultdict 的隐蔽副作用是**读取也会长键**:随便 `d["ghost"]` 就把 ghost 写进去,污染遍历和序列化;还有 pickle 往返会丢失工厂函数。需要「读不建键」时用 d.get 或普通 dict + setdefault。

```python
# file: code/01_语言核心与底层/q479_default_dict_patterns.py
from collections import defaultdict, Counter

text = "the quick brown fox jumps over the lazy dog the fox"

if __name__ == "__main__":
    # 1. 计数:Counter 最短
    print(Counter(text.split()).most_common(2))

    # 2. 分组:defaultdict 的标准姿势
    by_len = defaultdict(list)
    for w in text.split():
        by_len[len(w)].append(w)
    print(dict(by_len))

    # 3. setdefault:返回「已存在的或新建的」容器
    pairs = [("a", 1), ("b", 2), ("a", 3)]
    grouped = {}
    for k, v in pairs:
        grouped.setdefault(k, []).append(v)
    print(grouped)

    # 4. 副作用:defaultdict 读取也会长出键
    d = defaultdict(int)
    _ = d["ghost"]
    print("ghost in d:", "ghost" in d)
```

**追问**:1) defaultdict 与 setdefault 的性能差异来自哪?——defaultdict 缺键时走 C 实现的 __missing__ 钩子一次哈希完成创建;setdefault 无条件构造默认值对象再判断,多余一次分配。2) __missing__ 的通用玩法?——dict 子类实现 __missing__(key) 即可自定义缺键行为,defaultdict 只是「工厂函数」特例;可用于惰性加载、前缀树等;注意它只在下标访问路径触发,get()/in 不会。3) 读长键副作用的边界?——只有 d[key] 下标路径触发 __missing__ 写回;d.get(k)、`k in d`、遍历都不长键;副作用集中在「探测式访问」,而不是所有读操作。4) 生产陷阱?——defaultdict 经 json.dumps 变普通 dict,工厂行为在反序列化后丢失,协议边界要显式转换;`if d[k]:` 探测把缺键写进字典污染统计,判断存在性用 `k in d`。
