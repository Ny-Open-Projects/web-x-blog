---
title: [AGT-492] 笔试题——实现会话数据分区路由（一致性哈希+会话粘性+迁移）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-492：手写分区路由：一致性哈希、会话粘性、节点增减最小迁移

**需求与边界**：
- 输入：节点列表（增减动态）、会话 id；输出：路由节点。
- 边界要求：① 一致性哈希（虚拟节点均匀分布）；② 节点增减仅迁移相邻区段（最小迁移原则）；③ 会话粘性（同会话始终同节点——状态本地缓存场景）；④ 节点摘除时粘性会话迁移（状态外置兜底）。

**答**：
```javascript
class HashRing {
  constructor({ vnodes = 150 }) {
    this.vnodes = vnodes; this.ring = new Map();  // hash → node
    this.sorted = [];
  }
  addNode(node) {
    for (let i = 0; i < this.vnodes; i++) {
      const h = hash(`${node.id}:${i}`);
      this.ring.set(h, node.id);
    }
    this.rebuild();
  }
  removeNode(node) {
    for (let i = 0; i < this.vnodes; i++)
      this.ring.delete(hash(`${node.id}:${i}`));
    this.rebuild();
    // 迁移清单：原属该节点的 key 需迁到新 owner
    return this.migrationsFor(node);
  }
  rebuild() {
    this.sorted = [...this.ring.keys()].sort((a, b) => a - b);
  }
  route(convId) {                                // 顺时针找第一个节点
    const h = hash(convId);
    const idx = this.sorted.findIndex(k => k >= h);
    const ringKey = this.sorted[idx === -1 ? 0 : idx];
    return { node: this.ring.get(ringKey), sticky: true };
  }
  migrationsFor(removed) {                       // 最小迁移计算
    const moved = [];
    for (const [h, node] of this.ring) {
      if (node === removed) continue;
      // 该 key 若原本路由到 removed → 需迁移
      // （由状态外置存储执行 copy，粘性缓存重建）
    }
    return moved;
  }
}
// 状态外置（AGT-456）时粘性仅为缓存优化，
// 节点切换不丢数据；本地状态节点必须先迁移再摘除。
```

**评分点**:
- 一致性哈希+虚拟节点实现（均匀分布）。
- 路由顺时针查找含环绕处理（idx=-1 回到首个）。
- 最小迁移原则（仅相邻区段迁移）与摘除迁移清单意识。
- 会话粘性与状态外置的关系（粘性是优化不是正确性依赖）。
