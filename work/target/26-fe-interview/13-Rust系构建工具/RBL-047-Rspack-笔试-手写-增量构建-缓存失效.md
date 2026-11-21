---
title: [RBL-047] 笔试：手写增量构建的模块缓存失效器（脏标记扩散）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-047：笔试：手写增量构建的模块缓存失效器（脏标记扩散）
**题目**：给定模块图 { id, deps, parents }，实现 invalidate(changedId)：1) 把变更模块标记 dirty；2) 沿 parents 反向传播 dirty（依赖它的模块都要重编）；3) 遇到已 dirty 的模块剪枝（避免指数扩散）；4) 返回本次需要重编的模块 id 列表；5) 支持 contenthash 相同则剪枝（同内容变更可优化传播）。

```javascript
class InvalidationTracker {
  constructor(graph) { // graph: Map<id, {deps:Set, parents:Set, contentHash}>
    this.graph = graph;
    this.dirty = new Set();
  }
  invalidate(changedId, newHash) {
    const node = this.graph.get(changedId);
    // hash 相同（如仅格式化、导出未变）→ 内容等价，不扩散
    if (node.contentHash === newHash) return [];
    node.contentHash = newHash;
    this.dirty.add(changedId);
    // 沿 parents BFS 反向传播，visited 剪枝
    const queue = [changedId];
    while (queue.length) {
      const cur = queue.shift();
      for (const p of this.graph.get(cur).parents) {
        if (this.dirty.has(p)) continue;   // 已脏 → 剪枝
        this.dirty.add(p);
        queue.push(p);
      }
    }
    return [...this.dirty];
  }
  getDirty() { return [...this.dirty]; }
  clear() { this.dirty.clear(); }
}
module.exports = InvalidationTracker;

// 用法：改 leaf → parents 全脏；再改中间节点 → 已脏的根不重复入队
```
**评分点**：
- 反向沿 parents 传播（不是沿 deps 向下，方向错是主要扣分点）。
- visited/dirty 剪枝保证复杂度 O(V+E)（防止重复入队）。
- 内容 hash 相同提前返回（等价变更优化）。
- dirty 集合与重编列表分离（状态可查询）。
- 能联系 Rspack/webpack 的失效机制：hash 快照 + parents 反查。
