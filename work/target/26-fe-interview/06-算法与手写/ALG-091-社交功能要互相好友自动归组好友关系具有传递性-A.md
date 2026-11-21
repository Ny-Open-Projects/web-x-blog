---
title: [ALG-091] 社交功能要"互相好友"自动归组：好友关系具有传递性（A-B、B-C 则 A、B、C 同组）。如何用并查集（Union-Find）分组并统计组数？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-091：社交功能要"互相好友"自动归组：好友关系具有传递性（A-B、B-C 则 A、B、C 同组）。如何用并查集（Union-Find）分组并统计组数？
**答**：每个元素初始自成一组，`union` 把两个组的根相连，`find` 沿父指针找根，路径压缩让树几乎扁平（配合按秩合并近 O(α)）。最后根不同的即为不同组，统计根数即分组数。时间近 O(n × α(n))，空间 O(n)。

```javascript
class UnionFind {
  constructor() { this.parent = new Map(); }
  find(x) {
    if (!this.parent.has(x)) this.parent.set(x, x);
    while (this.parent.get(x) !== x) {
      // 路径压缩：直接挂到爷爷节点
      this.parent.set(x, this.parent.get(this.parent.get(x)));
      x = this.parent.get(x);
    }
    return x;
  }
  union(a, b) {
    const ra = this.find(a), rb = this.find(b);
    if (ra !== rb) this.parent.set(ra, rb);
  }
  groups() {
    const roots = new Set();
    for (const k of this.parent.keys()) roots.add(this.find(k));
    return roots.size;
  }
}
```
