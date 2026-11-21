---
title: [SCN-487] 笔试题——实现 AI 生成 UI 的门禁（lint/类型/视觉 diff/可访问性）？
date: 2026-11-20
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-487：手写 AI 生成 UI 门禁：静态校验、视觉 diff、a11y 检查、合并判定

**需求与边界**：
- 输入：AI 生成代码、设计稿参照；输出：门禁结果（block/fix/pass）。
- 边界要求：① 静态三检（lint/类型/a11y——axe 规则）；② 视觉 diff（渲染截图 vs 设计稿像素对比）；③ 违规项分级（blocker 阻断/nit 建议）；④ 修复建议回流（给 AI 重新生成的反馈）。

**答**：
```javascript
async function uiGate({ code, design }) {
  const issues = [];
  // 1. 静态三检
  const lint = await lintCode(code);           // ESLint
  const types = await typeCheck(code);         // tsc
  const a11y = await axeCheck(render(code));   // 可访问性
  issues.push(...[
    ...lint.map(x => ({ ...x, level: 'blocker' })),
    ...types.map(x => ({ ...x, level: 'blocker' })),
    ...a11y.violations.map(x => ({ ...x, level: 'must' })),
  ]);
  // 2. 视觉 diff
  const shot = await screenshot(code);
  const visual = pixelDiff(shot, design);      // 像素对比
  if (visual.diffRatio > 0.05)
    issues.push({ level: 'must', type: 'visual',
      detail: `还原度 ${100 - visual.diffRatio * 100}%`,
      regions: visual.regions });              // 差异区域
  // 3. 判定
  const blockers = issues.filter(i => i.level === 'blocker');
  const fixPrompt = issues.length
    ? genFixPrompt(issues)                    // 修复建议→AI 重生成
    : null;
  return {
    decision: blockers.length ? 'block'
      : issues.length ? 'fix_required' : 'pass',
    issues, fixPrompt,
  };
}
// 修复回流：fixPrompt → AI 重新生成 → 再过门禁（≤2 次）。
```

**评分点**:
- 静态三检（lint/类型/a11y）+ 视觉像素 diff 四维门禁。
- 分级判定（blocker 阻断/must 修复/nit 建议）。
- 视觉差异区域定位（regions）可定位修复。
- 修复建议回流 AI 重生成的闭环（≤2 次防死循环）。
