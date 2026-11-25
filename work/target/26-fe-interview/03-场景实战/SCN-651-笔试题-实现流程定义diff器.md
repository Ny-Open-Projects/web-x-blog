---
title: [SCN-651] 笔试题——实现流程定义 diff 器（节点增删改 + 路径影响分析）？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-651：手写流程定义 diff 器

**需求与边界**：
- 需求：对比两版流程定义，输出节点增/删/改（审批人规则或条件变化）与受影响的在途实例类别（无需迁移/需补填/不可迁移）。
- 边界：① 节点匹配按 id；② 改动检测字段级（assignee/condition/timeout）；③ 影响分析依据「改动字段是否影响已提交内容」。

**答**：
```javascript
function diffFlow(oldDef, newDef) {
  const oldMap = new Map(oldDef.nodes.map(n => [n.id, n]));
  const newMap = new Map(newDef.nodes.map(n => [n.id, n]));
  const diff = { added: [], removed: [], changed: [] };
  for (const [id, n] of newMap)
    if (!oldMap.has(id)) diff.added.push(id);
    else {
      const o = oldMap.get(id);
      const changes = ['assignee', 'condition', 'timeout', 'formPerm']
        .filter(f => JSON.stringify(o[f]) !== JSON.stringify(n[f]));
      if (changes.length) diff.changed.push({ id, changes, from: o, to: n });
    }
  for (const id of oldMap.keys()) if (!newMap.has(id)) diff.removed.push(id);
  diff.edgeChanged = JSON.stringify(oldDef.edges) !== JSON.stringify(newDef.edges);
  return diff;
}
function impactAnalysis(diff, instances) {
  const impacts = { none: [], refill: [], frozen: [] };
  for (const inst of instances) {
    const touched = diff.changed.some(c =>
      inst.statusMap[c.id] !== undefined            // 节点已在途
      && c.changes.some(f => f === 'formPerm'));    // 改了表单权限
    if (touched) impacts.frozen.push(inst.id);      // 不可迁移：保持快照
    else if (diff.added.length && inst.status === 'DRAFT')
      impacts.refill.push(inst.id);                 // 草稿可补填新字段
    else impacts.none.push(inst.id);
  }
  return impacts;
}
```

**评分点**:
- id 匹配 + 字段级变更检测（JSON 序列化比较）。
- 边变化单独标记（连线影响路径）。
- 影响三级分类（none/refill/frozen）依据「在途节点+字段类型」。
- frozen 语义正确：在途实例保持提交时快照不可迁移。

## 变体与延伸（补充）

**变体与延伸**：

1. 节点没有稳定 id、只能按名称匹配怎么办 → 引入人工 mapping 表或结构哈希做对齐，无法匹配的单独归为 ambiguous，禁止猜匹配。
2. 流程支持子流程与并行网关，diff 粒度怎么调 → 用 `parentId + id` 复合键做树形 diff，网关分支只比 `condition` 与出边集合。
3. 要求 diff 可回放（撤销一次发布）怎么办 → 输出 patch 序列而非最终态，`removed` 保留完整节点定义，回放时按逆序应用。
