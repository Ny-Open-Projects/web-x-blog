---
title: [ENG-317] 笔试题——实现 ADR 状态一致性校验（superseded 链与引用完整性）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## ENG-317：手写 ADR 校验器

**需求与边界**：
- 需求：校验 ADR 目录——① superseded 链合法（supersede 目标存在且状态为 accepted/superseded）；② 无环（A supersede B 且 B supersede A）；③ accepted 且被引用为「当前实践」的 ADR 必须无未关闭的 superseded 标记；④ 孤儿 ADR（无状态头）检测。
- 边界：① 状态解析容错（大小写/中英文）；② supersede 目标缺失时建议「标记 archived」；③ 输出修复建议。

**答**：
```javascript
function adrAudit(docs) {
  const byId = new Map(docs.map(d => [d.id, d]));
  const issues = [];
  for (const d of docs) {
    if (!d.status) { issues.push({ id: d.id, type: 'NO_STATUS', fix: '补状态头' }); continue; }
    for (const target of d.supersedes ?? []) {
      const t = byId.get(target);
      if (!t) { issues.push({ id: d.id, type: 'SUPERSEDE_MISSING', target,
        fix: `目标 ${target} 不存在，建议标记 ${d.id} 为 archived` }); continue; }
      if (t.status === 'rejected')
        issues.push({ id: d.id, type: 'SUPERSEDE_REJECTED', target,
          fix: `被否决的 ${target} 不应被 supersede，改为 related` });
    }
  }
  // supersede 链环检测
  const color = {};
  const dfs = (id, path) => {
    if (color[id] === 1) { issues.push({ type: 'SUPERSEDE_CYCLE', cycle: [...path, id] }); return; }
    if (color[id] === 2) return;
    const d = byId.get(id);
    color[id] = 1;
    for (const t of d?.supersedes ?? []) dfs(t, [...path, id]);
    color[id] = 2;
  };
  for (const d of docs) dfs(d.id, []);
  return issues;
}
```

**评分点**:
- supersede 目标三态校验（缺失/被否决/成环）。
- 被否决 ADR 的语义纠正（rejected 不可被 supersede，ENG-272 生命周期）。
- 链环检测（染色法复用）。
- 每个问题带修复建议（可行动）。
