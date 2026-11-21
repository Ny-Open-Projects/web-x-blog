---
title: [DP-209] 源码识别：TanStack Query 源码中的观察者与缓存策略？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-209：源码识别：TanStack Query 源码中的观察者与缓存策略？
**答**：
- 观察者（核心）：QueryCache 持 query 池，每个 query 持 observers 列表；组件 useQuery = 创建 observer 订阅，状态变化 notify 观察者——多组件共享同一 query 的机制就在这里。
- 备忘录+策略：缓存即备忘录（key 指纹），staleTime/gcTime 是过期策略（ARC-059 数据失效同款思想）；refetchOnWindowFocus 是事件驱动的策略触发。
- 状态机：query 状态 idle/fetching/error/success + fetchStatus，重试与乐观更新挂在状态转移上。
- 识别要点：能说清"一个 query 多个 observer 时，数量归零触发 gcTime 回收"——观察者计数与缓存的联动。

```javascript
// TanStack Query 简化模型
class Query {
  observers = new Set();          // 观察者
  state = { data: undefined, status: 'idle', fetchStatus: 'idle' };
  subscribe(o) { this.observers.add(o); return () => this.observers.delete(o); }
  notify() { this.observers.forEach(o => o.onUpdate(this.state)); }
  async fetch() {
    this.state = { ...this.state, fetchStatus: 'fetching' }; this.notify();
    try { const data = await this.options.queryFn();
      this.state = { data, status: 'success', fetchStatus: 'idle', dataUpdatedAt: Date.now() };
    } catch (e) { this.state = { ...this.state, status: 'error', fetchStatus: 'idle' }; }
    this.notify();
  }
}
class QueryCache {
  map = new Map();                // 备忘录池：hashKey → Query
  getOrCreate(options) { const k = hashKey(options.queryKey);
    this.map.get(k) ?? this.map.set(k, new Query(options)); return this.map.get(k); }
  removeExpired(now) {            // gcTime：observer 数为 0 且过期 → 删除
    for (const [k, q] of this.map)
      if (!q.observers.size && now - q.state.dataUpdatedAt > q.options.gcTime) this.map.delete(k);
  }
}
```
