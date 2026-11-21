---
title: [Q2222] stale-while-revalidate: 用旧值窗口换回源毛刺
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2222 · stale-while-revalidate: 用旧值窗口换回源毛刺

> 难度:★★★★ | 标签:缓存, 可用性

**问**:SWR 是什么?它解决了什么问题,引入了什么新问题?

**答**:stale-while-revalidate 把过期分成两段:TTL 内返回新鲜值;TTL 后、硬过期前的"旧值窗口"内,先返回旧值,同时触发后台刷新——把原本同步回源的毛刺摊到异步。收益直接:回源延迟从读路径上消失,后端抖动被旧值吸收,可用性显著提升;代价是读到的可能不是最新值,所以窗口长度必须匹配业务的"允许旧多久",并且刷新必须配单飞(single-flight),否则旧值窗口内的并发读会打出并发回源,毛刺反而放大。硬过期仍然同步回源,这是最终兜底。适用边界:内容类、榜单类适合;余额、权限类要么禁用 SWR,要么在窗口内加版本校验。

```python
# file: code/04_数据库与缓存/q2222_stale_while_revalidate.py
"""stale-while-revalidate: 过期后先回旧值, 触发刷新"""

class SwrCache:
    def __init__(self, loader, ttl, stale_window):
        self.loader = loader
        self.ttl = ttl
        self.stale_window = stale_window
        self.value = None
        self.fetched_at = None
        self.refreshing = False

    def get(self, now):
        if self.value is None:
            self.value = self.loader()
            self.fetched_at = now
            return self.value, "miss 同步回源"
        age = now - self.fetched_at
        if age < self.ttl:
            return self.value, "fresh"
        if age < self.ttl + self.stale_window:
            if not self.refreshing:
                self.refreshing = True
                old = self.value
                self.value = self.loader()   # 同步调用模拟后台刷新完成
                self.fetched_at = now
                self.refreshing = False
                return old, "stale 先回旧值 刷新已触发"
            return self.value, "stale 刷新进行中 返回旧值"
        self.value = self.loader()
        self.fetched_at = now
        return self.value, "硬过期 同步回源"

calls = {"n": 0}
def loader():
    calls["n"] += 1
    return "data-v%d" % calls["n"]

cache = SwrCache(loader, ttl=10, stale_window=5)
for now in (0, 5, 11, 13, 26):
    v, why = cache.get(now)
    print("t=%-3d 返回 %-8s 状态=%s" % (now, v, why))
print("SWR 用允许旧值的窗口换掉回源毛刺, 刷新必须单飞, 硬过期是最终兜底")
```

**追问**:
- 与逻辑过期什么区别?—— 逻辑过期永不物理过期、由刷新线程维护,SWR 保留物理 TTL 作为兜底,两者可以叠加。
- 窗口内的旧值要打标吗?—— 要,响应头或字段带上 stale 标记与数据版本,方便监控归因和业务按需绕过。

---
