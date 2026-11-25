---
title: [ARC-791] 笔试：手写 ADR 模板与完整性校验器
date: 2026-11-21
categories: [前端架构]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## ARC-791：笔试：手写 ADR 模板与校验器

**答**：实现 ADR（架构决策记录）的模板与校验器：① ADR 数据模型：id/title/status(proposed|accepted|superseded)/context/decision/consequences/alternatives(被否方案含理由)/decidedBy/date/reviewDate；② 校验器 `validateADR(adr)`：完整性检查（必填字段/alternatives ≥1 条含理由/被否方案不能为空）、格式检查（reviewDate > date）；③ 状态机校验：superseded 必须引用替代决策的 id；④ 输出校验报告（error/warning 分级——warning 如无 reviewDate）；⑤ 提供 markdown 渲染器（ADR → 文档）。写出实现与一个 ADR 样例。

```javascript
const REQUIRED = ['id', 'title', 'status', 'context', 'decision', 'consequences', 'decidedBy', 'date'];

function validateADR(adr) {
  const errors = [], warnings = [];
  for (const f of REQUIRED) if (!adr[f]) errors.push(`missing field: ${f}`);
  if (!Array.isArray(adr.alternatives) || adr.alternatives.length === 0)
    errors.push('alternatives required (被否方案必须记录)');
  else adr.alternatives.forEach((a, i) => {
    if (!a.option || !a.reason) errors.push(`alternative[${i}] needs option & reason`);
  });
  if (adr.reviewDate && new Date(adr.reviewDate) <= new Date(adr.date))
    errors.push('reviewDate must be after date');
  else if (!adr.reviewDate) warnings.push('no reviewDate — 决策需复审日');
  if (adr.status === 'superseded' && !adr.supersededBy)
    errors.push('superseded must reference supersededBy id');
  if (adr.status === 'proposed' && !adr.reviewers?.length)
    warnings.push('proposed without reviewers');
  return { errors, warnings, ok: errors.length === 0 };
}

function renderADR(adr) {
  return `# ADR-${adr.id}: ${adr.title}\n\n**状态**: ${adr.status} | **决策**: ${adr.decidedBy} | **日期**: ${adr.date}\n\n## 背景\n${adr.context}\n\n## 决策\n${adr.decision}\n\n## 备选方案\n${adr.alternatives.map(a => `- ~~${a.option}~~: ${a.reason}`).join('\n')}\n\n## 后果\n${adr.consequences}\n\n## 复审\n${adr.reviewDate ?? '未设置'}`;
}

// 样例
const sample = {
  id: 17, title: '状态管理迁移到 zustand', status: 'accepted',
  context: 'redux 样板代码占比 40%, 新人上手慢', decision: '迁移到 zustand',
  alternatives: [{ option: '保留 redux + rtk', reason: '迁移成本 3 人月, 收益不足以覆盖' }],
  consequences: '存量 12 模块需迁移, 双跑 1 个月',
  decidedBy: 'arch-team', date: '2026-11-01', reviewDate: '2027-05-01',
  reviewers: ['a', 'b'],
};
console.log(validateADR(sample).ok); // true
```

**评分点**：
- alternatives 必须含被否理由（ADR 的核心价值是取舍记录）
- superseded 状态机校验（决策演进链完整）
- error/warning 分级（阻断 vs 提示）
- markdown 渲染器的取舍表达（被否方案删除线）
