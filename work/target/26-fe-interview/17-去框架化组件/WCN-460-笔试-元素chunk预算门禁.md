---
title: [WCN-460] 笔试：实现元素 chunk 的体积预算门禁（构建产物检查）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-460：笔试：实现元素 chunk 的体积预算门禁（构建产物检查）。
**答**：输入 `[{file, gzip}]` 与预算表。门禁：超预算列出；共享 chunk（被 > 3 元素引用）单独预算。输出 `{violations, total}` 与构建退出码。

```javascript
function chunkGate(arts, budgets, { exempt = [] } = {}) {
  const violations = arts
    .filter(a => !exempt.includes(a.file) && a.gzip > (budgets[a.file] ?? budgets.default))
    .map(a => ({ file: a.file, gzip: a.gzip, limit: budgets[a.file] ?? budgets.default }));
  return { violations, exitCode: violations.length ? 1 : 0,
    total: arts.reduce((s, a) => s + a.gzip, 0) };
}
console.log(chunkGate([
  { file: 'ds-button.js', gzip: 3 }, { file: 'ds-table.js', gzip: 14 },
], { default: 8, 'ds-table.js': 12 })); // violations: [ds-table 14 > 12]，exitCode 1

```

**评分点**：
- per-element 预算表驱动。
- 共享 chunk 识别与单独预算。
- 退出码语义（CI 集成）。
- 豁免清单（带说明的特批）。
