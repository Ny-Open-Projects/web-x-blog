---
title: [HW-262] 手写一个树结构 CRDT：并发移动子节点的冲突处理
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-262：手写一个树结构 CRDT：并发移动子节点的冲突处理

**答**：
- 需求：实现 TreeCRDT：节点 {id, parent, ts, site, deleted}；move(nodeId, newParent) 是带 ts 的写；并发移动同一节点（A→X vs A→Y）按 LWW 定 parent；环检测（移动造成父子环）拒绝并回退到合法父节点；删除子树（递归 tombstone）。
- 边界：并发移动+删除交叉（删除优先于移动？按 ts LWW 统一判定）；环检测在 merge 后整体校验（不只单次 move）；孤儿节点（parent 被删）挂到根并标记。
- 评分点：LWW 移动；merge 后环检测；孤儿处理。

```javascript
class TreeCRDT {
  constructor(siteId) { this.site = siteId; this.nodes = new Map(); }
  add(id, parent) { this.nodes.set(id, { id, parent, ts: Date.now(), site: this.site, deleted: false }); }
  async move(id, newParent) {                               // LWW 移动
    const n = this.nodes.get(id);
    if (!n) return false;
    const ts = Date.now();
    const trial = new Map(this.nodes); trial.get(id).parent = newParent;
    if (hasCycle(trial, id)) return false;                  // 即时环检测
    Object.assign(n, { parent: newParent, ts, site: this.site });
    return true;
  }
  merge(remote) {
    for (const [id, r] of remote) {
      const cur = this.nodes.get(id);
      if (!cur) { this.nodes.set(id, { ...r }); continue; }
      if (r.ts > cur.ts || (r.ts === cur.ts && r.site > cur.site)) Object.assign(cur, r);   // LWW
    }
    this.fixCycles(); this.fixOrphans();                    // merge 后整体校验
  }
  fixCycles() {
    const seen = new Set();
    for (const id of this.nodes.keys()) {
      let p = id; seen.clear();
      while (p) { if (seen.has(p)) { this.nodes.get(p).parent = null; break; }   // 断环挂根
        seen.add(p); p = this.nodes.get(p)?.parent; }
    }
  }
  fixOrphans() { for (const n of this.nodes.values())
    if (n.parent && (!this.nodes.get(n.parent) || this.nodes.get(n.parent).deleted))
      { n.parent = null; n.orphan = true; } }
  removeSubtree(id) {                                       // 递归墓碑
    for (const n of this.nodes.values())
      if (n.id === id || isDescendant(this.nodes, n.id, id)) n.deleted = true;
  }
}
```
