---
title: [XP-413] 手写一个层级 Token 管理器（弹层/悬浮层）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## XP-413：手写一个层级 Token 管理器（弹层/悬浮层）

**答**：
- 需求：implement ZToken(layers 为 modal/toast/dropdown)。alloc(layer) 按 layer 基础值 + 序号分配；层间保证 toast > modal > dropdown；release 回收（序号重用）；输出 { z, layer }。
- 边界：layer 未知抛错；同层并发分配递增；release 后序号可复用（回收池）；上限 100 防溢出。
- 评分点：分层基础值；回收复用；未知层；溢出

```javascript
class ZToken {
  constructor(layers = ['dropdown', 'modal', 'toast']) {
    this.layers = layers;
    this.base = new Map(layers.map((l, i) => [l, 1000 + i * 100]));
    this.counter = new Map(layers.map(l => [l, 0]));
    this.free = new Map(layers.map(l => [l, []]));
  }
  alloc(layer) {
    if (!this.base.has(layer)) throw new Error('未知层 ' + layer);
    const recycled = this.free.get(layer).pop();
    if (recycled) return { z: recycled, layer };
    const n = this.counter.get(layer);
    if (n >= 100) throw new Error('层级溢出');
    this.counter.set(layer, n + 1);
    return { z: this.base.get(layer) + n, layer };
  }
  release(z, layer) {
    this.free.get(layer).push(z);                      // 回收复用
  }
}
```
