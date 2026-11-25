---
title: [AGT-477] 笔试题——实现答案增量更新（数据变化时只更新受影响段落）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-477：手写增量更新：段落级依赖追踪、变更影响面计算、局部重生成

**需求与边界**：
- 输入：原答案（分段）、数据变更集；输出：更新后的答案（仅重生成受影响段）。
- 边界要求：① 段落依赖追踪（每段引用了哪些数据点）；② 变更影响面（变更的数据点→受影响段落集合）；③ 仅重生成受影响段（成本最小化），未变段原样保留；④ 全局一致性检查（更新后数字前后不矛盾）。

**答**：
```javascript
async function incrementalUpdate(prev, changes, { regenerate, depsOf }) {
  // 1. 影响面：变更数据点 → 依赖它的段落
  const changedKeys = new Set(changes.map(c => c.key));
  const affected = new Set();
  for (const seg of prev.segments)
    for (const dep of seg.deps)          // 段落生成时记录的依赖
      if (changedKeys.has(dep.key)) affected.add(seg.id);
  // 2. 局部重生成
  const segments = await Promise.all(prev.segments.map(async seg => {
    if (!affected.has(seg.id)) return seg;           // 未受影响原样保留
    const fresh = changes.filter(c =>
      seg.deps.some(d => d.key === c.key));
    const updated = await regenerate(seg, fresh, {
      rule: `只更新与变更数据相关的表述；
        未变更的数据保持原值：${seg.deps
          .filter(d => !changedKeys.has(d.key))
          .map(d => `${d.key}=${d.value}`).join(', ')}` });
    return { ...seg, text: updated, rev: seg.rev + 1 };
  }));
  // 3. 全局一致性：更新后数字集合自洽检查
  const nums = extractAll(segments);
  const inconsistent = nums.filter(n => n.key &&
    changedKeys.has(n.key) &&
    n.value !== changes.find(c => c.key === n.key).value);
  if (inconsistent.length)
    return { error: '更新后数字不一致',
      segments, inconsistent };                     // 供修复或人工
  return { segments, updated: affected.size,
    saved: prev.segments.length - affected.size };  // 节省统计
}
```

**评分点**:
- 段落依赖追踪（生成时记录 deps）→ 变更影响面计算正确。
- 仅重生成受影响段+节省统计（成本优化可量化）。
- 重生成 prompt 纪律：未变更数据显式保持（防连带改写）。
- 全局一致性检查（更新后数字自洽），不一致不静默。
