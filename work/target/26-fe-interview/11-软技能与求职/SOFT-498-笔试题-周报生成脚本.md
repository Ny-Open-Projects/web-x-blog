---
title: [SOFT-498] 笔试题——手写周报生成脚本（三段式+价值翻译）？
date: 2026-11-20
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-498：手写一个周报生成脚本——原始工作项自动整理为三段式周报？

**需求与边界**：
- 输入：本周工作项数组（含动作与原始描述）；输出：≤10 行三段式周报（结果/风险/下周）。
- 边界要求：① 工作项必须完成"价值翻译"（动作→业务收益）；② 风险为空也要输出"无"（显式声明）；③ 下周计划 ≤3 项且可验证。

**答**（周报生成脚本）:
```javascript
/**
 * @param {Array<{raw:string, value?:string, risk?:{desc:string,plan:string}, next?:string}>} items
 */
function buildWeekly(items) {
  // 1. 结果段：优先取有"价值翻译"的项，动作→收益
  const results = items
    .filter(i => !i.risk)
    .map((i, idx) => `${idx + 1}. ${i.value || i.raw}`); // 无翻译则保底原文
  // 2. 风险段：空也要显式输出"无"（预期管理）
  const risks = items.filter(i => i.risk)
    .map(i => `- ${i.risk.desc}（方案：${i.risk.plan}）`); // 风险永远带方案
  if (!risks.length) risks.push('- 无');
  // 3. 下周段：≤3 项，必须可验证（有交付物或指标）
  const nexts = items.filter(i => i.next).slice(0, 3)
    .map((i, idx) => `${idx + 1}. ${i.next}`);
  return ['【结果】', ...results, '【风险】', ...risks,
          '【下周】', ...nexts].join('\n');
}
// 示例输入：
// [{ raw: '重构列表组件', value: '重构列表组件，新需求开发 5 天→2 天' },
//  { raw: '修了 3 个 bug', value: '修复 __ 等 3 个 bug，回归通过' },
//  { risk: { desc: 'X 接口可能延 1 天', plan: '先 mock 联调，影响可控' },
//    next: 'X 页面上线（灰度 5%）' }]
// 自检：≤10 行；风险空输出"无"；下周带可验证交付物。
```

**评分点**:
- 三段式结构正确（结果/风险/下周），结果先行、≤10 行的长度纪律落实。
- 价值翻译逻辑存在（value 优先于 raw），区分"动作描述"与"业务收益"。
- 风险为空仍显式输出"无"，且每条风险强制带方案（plan 字段必填逻辑）。
- 下周计划限 3 项且要求可验证，符合"预期管理"与"可考核"两个设计目标。
