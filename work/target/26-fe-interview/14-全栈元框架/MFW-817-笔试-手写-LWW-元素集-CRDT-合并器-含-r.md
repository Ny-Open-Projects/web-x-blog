---
title: [MFW-817] 笔试：手写 LWW 元素集 CRDT 合并器（含 remove 优先与节点 tie-break）
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-817：笔试：手写 LWW 元素集 CRDT 合并器（含 remove 优先与节点 tie-break）

**答**：
- 结论：合并是幂等/交换/结合的（CRDT 三性质），add 与 remove 各自取时间戳较大者；平局时 remove 优先，避免「幽灵元素」。
- 关键：节点 id 做 tie-break，避免不同节点同时间戳的合并结果不确定；元素可见当且仅当 add.ts > remove.ts。
- 追问钩子：tombstone 无限增长怎么压缩？——需要向量时钟/版本下限，确认所有副本已同步后才能 GC。

```javascript
function merge(a, b) {
  const pick = (ma, mb, preferRemove) => {
    const out = new Map(ma);
    for (const [id, v] of mb) {
      const cur = out.get(id);
      const win = cur === undefined || v.ts > cur.ts ||
                  (v.ts === cur.ts && preferRemove) ||
                  (v.ts === cur.ts && v.node > (cur.node || ''));
      if (win) out.set(id, v);
    }
    return out;
  };
  const adds = pick(a.adds, b.adds, false);
  const removes = pick(a.removes, b.removes, true);   // 平局 remove 优先
  const visible = new Set();
  for (const [id, add] of adds) {
    const rem = removes.get(id);
    if (!rem || add.ts > rem.ts) visible.add(id);
  }
  return { adds, removes, visible: [...visible] };
}

// 自测：A 加 x，B 加 y → 合并后 x、y 都在
const A = { adds: new Map([['x', { ts: 1, node: 'a' }]]), removes: new Map() };
const B = { adds: new Map([['y', { ts: 1, node: 'b' }]]), removes: new Map() };
console.log(merge(A, B).visible.sort().join(','));    // x,y
// 幂等性：merge(A,B) 再与 A 合并结果不变
console.log(merge(merge(A, B), A).visible.sort().join(',')); // x,y
```

**评分点**：
- 合并满足幂等/交换/结合三性质（CRDT 正确性基础，需在自测或点评中体现）
- add/remove 分别取时间戳较大者，平局 bias remove 防幽灵元素
- 节点 id 做 tie-break，消除同 ts 的不确定性
- 元素可见性判定 add.ts > remove.ts 正确；能讨论 tombstone 压缩（加分）
