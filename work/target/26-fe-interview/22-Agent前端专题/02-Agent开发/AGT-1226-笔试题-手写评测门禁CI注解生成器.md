---
title: [1226] 笔试手写：实现评测门禁结果的 PR 注释生成
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, 评测]
type: 笔试题
---

## 1226：笔试手写：实现评测门禁结果的 PR 注释生成

**答**：实现 gateComment(report, baseline)：report/baseline 为 { intent: { acc, cost } }。生成 markdown 注释：每意图一行（acc 变化箭头 +/-、cost 变化百分比），全局结论行（全意图 acc 无下降且 cost 增幅 <20% 为 '✅ pass'，否则 '❌ fail' 列出失败意图）。acc 变化保留 3 位。

```js
function gateComment(report, baseline) {
  const lines = [];
  const failed = [];
  for (const [intent, r] of Object.entries(report)) {
    const b = baseline[intent];
    const d = b ? +(r.acc - b.acc).toFixed(3) : null;
    const costUp = b ? (r.cost - b.cost) / b.cost : 0;
    const ok = b ? d >= 0 && costUp < 0.2 : true;
    if (!ok) failed.push(intent);
    const arrow = d === null ? 'new' : d > 0 ? `📈 +${d}` : d < 0 ? `📉 ${d}` : '=' ;
    lines.push(`| ${intent} | acc ${arrow} | cost ${costUp >= 0 ? '+' : ''}${(costUp * 100).toFixed(1)}% | ${ok ? '✅' : '❌'} |`);
  }
  const verdict = failed.length
    ? `❌ fail: ${failed.join(', ')}` : '✅ pass';
  return [`**评测门禁 ${verdict}**`, '| intent | acc | cost | gate |', '|---|---|---|---|',
    ...lines].join('\n');
}
console.log(gateComment(
  { qa: { acc: 0.85, cost: 110 }, code: { acc: 0.9, cost: 100 } },
  { qa: { acc: 0.86, cost: 100 }, code: { acc: 0.88, cost: 100 } }));
// qa acc -0.01 & cost +10% -> 通过（acc 降但 cost 增 <20% 需业务规则——本实现 acc 降即 fail）
// 实现里 ok = d >= 0 && costUp < 0.2 —— qa d=-0.01 -> fail
```

**评分点**：
- 双条件门禁（acc 不降 + cost 增幅 <20%）
- markdown 表格格式（PR 注释可直接渲染）
- 失败意图清单（CI fail 原因可读）
- 能讨论：门禁规则的分级（acc 小幅波动容忍带）、new intent 的基线缺失处理

