---
title: [Q2292] Agent 记忆的分级存储:热 暖 冷三层
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2292 · Agent 记忆的分级存储:热 暖 冷三层

> 难度:★★☆☆ | 标签:Agent, 记忆, 存储分层

**问**:Agent 跑了几百轮对话,上下文记忆怎么存才能又快又省?全放内存或全落盘各有什么问题?

**答**:按访问热度分三层:L1 热层是进程内 OrderedDict,毫秒级读写但容量最小;L2 暖层落盘存 JSON 行,容量大但读一次有 IO 代价;L3 冷层归档老记录,只能显式取回。核心机制是双向流动:热层超容量按 LRU 逐出到暖层,暖层超容量按"非重要且最旧"优先归档;而读穿透会让暖层冷层记录自动晋升回热层——刚被翻过的记忆大概率还会被翻。重要标记让关键事实(用户偏好、已确认决策)在归档时豁免。收益是把内存预算花在最近活跃的记忆上,全量记忆不丢但都不占贵资源。

```python
# file: code/06_Agent与LLM及系统设计/q2292_memory_tiers.py
"""Agent 记忆分级存储:L1 进程内 LRU L2 磁盘档 L3 归档,带晋升 降级与容量核算。"""
from collections import OrderedDict


class TieredMemory:
    def __init__(self, hot_cap=3, warm_cap=5, clock=None):
        self.hot = OrderedDict()
        self.warm = {}
        self.cold = {}
        self.hot_cap, self.warm_cap = hot_cap, warm_cap
        self.clock = clock if clock is not None else (lambda: 0)
        self.moved = []

    def put(self, key, value, important=False):
        rec = {"v": value, "ts": self.clock(), "important": important}
        self.hot[key] = rec
        self.hot.move_to_end(key)
        self._evict_hot()

    def get(self, key):
        if key in self.hot:
            self.hot.move_to_end(key)
            return self.hot[key]["v"]
        if key in self.warm:
            rec = self.warm.pop(key)
            self.hot[key] = rec
            self.moved.append(("promote", key))
            self._evict_hot()
            return rec["v"]
        if key in self.cold:
            rec = self.cold.pop(key)
            self.hot[key] = rec
            self.moved.append(("restore", key))
            self._evict_hot()
            return rec["v"]
        return None

    def _evict_hot(self):
        while len(self.hot) > self.hot_cap:
            key, rec = self.hot.popitem(last=False)
            self.warm[key] = rec
            self.moved.append(("demote", key))
            if len(self.warm) > self.warm_cap:
                oldest = min(self.warm.items(),
                             key=lambda kv: (kv[1]["important"], kv[1]["ts"]))
                self.cold[oldest[0]] = self.warm.pop(oldest[0])
                self.moved.append(("archive", oldest[0]))

    def stats(self):
        return {"hot": len(self.hot), "warm": len(self.warm), "cold": len(self.cold)}


if __name__ == "__main__":
    counter = {"n": 0}

    def clock():
        counter["n"] += 1
        return counter["n"]

    m = TieredMemory(hot_cap=2, warm_cap=2, clock=clock)
    m.put("a", "alpha")
    m.put("b", "beta")
    m.put("c", "gamma", important=True)
    assert m.stats() == {"hot": 2, "warm": 1, "cold": 0}
    assert m.moved[-1] == ("demote", "a"), "最旧的热层记录降级到暖层"
    assert m.get("a") == "alpha" and ("promote", "a") in m.moved, "读穿透自动晋升"
    m.put("d", "delta")
    m.put("e", "epsilon")
    assert m.stats()["cold"] >= 1, "暖层溢出归档冷层"
    assert m.get("a") == "alpha" and ("restore", "a") in m.moved, "冷档可显式取回"
    assert m.get("c") == "gamma", "重要记录可从暖层取回"
    assert m.get("missing") is None
    print("分级记忆通过:热层逐出 暖层归档 读穿透晋升 冷档取回")
```

**追问**:
- 暖层应该存什么格式? 答:追加式 JSONL 加索引偏移,读时按偏移 seek,不要整个文件重写
- 会话结束冷层数据怎么处理? 答:按保留策略过期清理,重要记忆提取为事实卡进长期记忆库,而不是原样囤积
