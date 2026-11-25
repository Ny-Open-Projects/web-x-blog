---
title: [RBL-955] 笔试：手写可调试性 review 清单校验器（诊断码/trace/失败信息覆盖）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-955：笔试：手写可调试性 review 校验器（四项清单）

**答**：实现 `debugReview(pr, diff)`。pr: `{ checklist?: string[] }`；diff: `{ newErrors: number, newAsync: boolean, newDynamicImport: boolean, newMinified: boolean }`. 规则：1) checklist 校验（新增错误须有诊断码声明等——pr.checklist 含对应项）；2) **diff 驱动的强制项**：newErrors > 0 → 要求 'diagnostic-codes' 项；newAsync → 'trace-spans'；newDynamicImport → 'chunk-failure-info'；newMinified → 'sourcemap-names'——diff 有变化但 checklist 缺对应项 → finding 'missing-check'；3) checklist 有但 diff 无对应变化 → info 'redundant-check'；4) 返回 `{ findings, ok }`（ok = 无 missing-check）。边界：diff 全 false；checklist 全量但无变化（全是 redundant）。

```javascript
const MAP = {
  diagnosticCodes: { trigger: (d) => d.newErrors > 0, label: '新增错误有诊断码' },
  traceSpans: { trigger: (d) => d.newAsync, label: '异步链路有 trace span' },
  chunkFailureInfo: { trigger: (d) => d.newDynamicImport, label: '动态导入失败信息' },
  sourcemapNames: { trigger: (d) => d.newMinified, label: 'sourcemap names 保留' },
};

function debugReview(pr = {}, diff = {}) {
  const findings = [];
  const checklist = new Set(pr.checklist ?? []);
  for (const [key, cfg] of Object.entries(MAP)) {
    const needed = cfg.trigger(diff);
    const has = checklist.has(key);
    if (needed && !has) findings.push({ type: 'missing-check', key, label: cfg.label });
    else if (!needed && has) findings.push({ type: 'redundant-check', key, level: 'info' });
  }
  return { findings, ok: !findings.some(f => f.type === 'missing-check') };
}

// 自测
const diff = { newErrors: 2, newAsync: true, newDynamicImport: false, newMinified: false };
let r = debugReview({ checklist: ['diagnosticCodes'] }, diff);
console.log(r.ok === false);
console.log(r.findings.some(f => f.type === 'missing-check' && f.key === 'traceSpans'));
console.log(!r.findings.some(f => f.key === 'chunkFailureInfo'));   // 无变化不要求

// 全备
r = debugReview({ checklist: ['diagnosticCodes', 'traceSpans'] }, diff);
console.log(r.ok === true);

// 冗余检查
r = debugReview({ checklist: ['diagnosticCodes', 'chunkFailureInfo', 'traceSpans', 'sourcemapNames'] },
  { newErrors: 0, newAsync: false, newDynamicImport: false, newMinified: false });
console.log(r.findings.every(f => f.type === 'redundant-check') && r.ok === true);
console.log(r.findings.length === 4);

console.log(debugReview({}, { newErrors: 0, newAsync: false, newDynamicImport: false, newMinified: false }).ok === true);
```

**评分点**：
- diff 驱动的强制项映射（变化类型 ↔ 可调试性义务）；missing 与 redundant 双向
- ok 仅由 missing-check 决定（redundant 是 info 不阻断）；边界（全 false/全量清单）
- 清单项与卡片体系的链接（诊断码/trace/失败信息/map names）
- 能说清「可调试性与功能同 review——每个 PR 回答『出了错怎么排查』」属于加分
