---
title: [SCN-646] 笔试题——实现审批表单 schema 版本迁移器（字段映射 + 冲突标记）？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-646：手写表单 schema 迁移器

**需求与边界**：
- 输入：v1 数据、v1→v2 映射表（rename/transform/drop/add）、v2 schema。
- 输出：迁移后数据 + 迁移报告 `{ mapped, dropped, conflicts, missing }`；冲突 = 映射目标已有值且源值不同。

**答**：
```javascript
function migrateForm(v1Data, mapping, v2Schema) {
  const out = {}, report = { mapped: [], dropped: [], conflicts: [], missing: [] };
  for (const [src, rule] of Object.entries(mapping)) {
    const srcVal = v1Data[src];
    if (rule.type === 'drop') { report.dropped.push(src); continue; }
    const dst = rule.to;
    if (rule.type === 'rename') out[dst] = srcVal;
    else if (rule.type === 'transform') out[dst] = rule.fn(srcVal);   // 类型转换/单位换算
    if (rule.type !== 'rename' && rule.type !== 'transform') continue;
    // 冲突检测：v2 已有值（如迁移目标被另一个映射写过）
    if (out[dst] !== undefined && report.mapped.some(m => m.to === dst))
      report.conflicts.push({ to: dst, first: out[dst], second: srcVal });
    else report.mapped.push({ from: src, to: dst });
    delete v1Data[src];
  }
  // 未映射的 v1 字段：丢弃并报告（不静默丢）
  for (const k of Object.keys(v1Data)) report.dropped.push(k);
  // v2 必填缺失
  for (const f of v2Schema.required)
    if (out[f] === undefined || out[f] === '') report.missing.push(f);
  return { data: out, report };
}
// 映射示例：
// { amount_fen: { type: 'transform', to: 'amount', fn: v => v / 100 },  // 分→元
//   old_remark: { type: 'rename', to: 'comment' },
//   legacy_flag: { type: 'drop' } }
```

**评分点**:
- 三种迁移类型（rename/transform/drop）+ add 语义由 missing 体现。
- 冲突检测（映射目标重写）。
- 未映射字段显式 dropped 报告（不静默丢数据）。
- 必填缺失进 missing 供补填提示。
