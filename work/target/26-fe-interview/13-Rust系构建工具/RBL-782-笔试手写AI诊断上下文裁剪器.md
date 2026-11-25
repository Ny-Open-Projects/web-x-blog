---
title: [RBL-782] 笔试：手写 AI 诊断上下文裁剪器（预算约束 + 优先级保留）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-782：笔试：手写 AI 诊断上下文裁剪器（预算 + 优先级）

**答**：实现 `trimForAI(items, { budgetTokens, estimate, minPerItem })`。items: AI 诊断对象数组（含 location.snippet 可能很长）。estimate: `(obj) => number`（token 估算注入）。规则：1) error 项优先于 warn；2) 同级按原始序；3) 总预算 budgetTokens：按序装入，装不下时**保底裁剪**（每项至少 minPerItem token：只保留 code+message 前 N 字符，去 snippet/hints）；4) 全部塞不下时至少保留第一个 error 的保底版；5) 返回 `{ kept: Array<{ item, trimmed: boolean }>, used }`。边界：budget 为 0 → 只返回第一个 error 的最小骨架（若存在）；空数组。

```javascript
function trimForAI(items = [], { budgetTokens = 4000, estimate, minPerItem = 60 } = {}) {
  const est = estimate ?? ((o) => JSON.stringify(o).length / 4);
  const skeleton = (item) => ({
    code: item.code, severity: item.severity,
    message: (item.message || '').slice(0, minPerItem),
  });
  const sorted = [...items].sort((a, b) =>
    (a.severity === 'error' ? 0 : 1) - (b.severity === 'error' ? 0 : 1));

  const kept = []; let used = 0;
  for (const item of sorted) {
    const full = est(item);
    if (used + full <= budgetTokens) {
      kept.push({ item, trimmed: false }); used += full;
      continue;
    }
    const sk = skeleton(item);
    const skCost = est(sk);
    if (used + skCost <= budgetTokens) {
      kept.push({ item: sk, trimmed: true }); used += skCost;
    }
    // 连保底都放不下：跳过
  }
  if (!kept.length && sorted.length) {                   // 保底：第一个 error 最小骨架
    const first = sorted.find(i => i.severity === 'error') ?? sorted[0];
    const sk = skeleton(first);
    return { kept: [{ item: sk, trimmed: true }], used: est(sk) };
  }
  return { kept, used };
}

// 自测
const est = (o) => JSON.stringify(o).length / 4;
let r = trimForAI([
  { code: 'W1', severity: 'warn', message: 'm1', hints: ['h'] },
  { code: 'E1', severity: 'error', message: 'e1', location: { snippet: 'x'.repeat(4000) } },
], { budgetTokens: 4000, estimate: est });
console.log(r.kept[0].item.code === 'E1' && r.kept[0].trimmed === false);   // error 优先
console.log(r.kept.length >= 1);

// 装不下 -> 保底裁剪
r = trimForAI([
  { code: 'E1', severity: 'error', message: 'big'.repeat(1000), location: { snippet: 'y'.repeat(5000) } },
  { code: 'E2', severity: 'error', message: 'e2' },
], { budgetTokens: 300, estimate: est, minPerItem: 20 });
console.log(r.kept[0].trimmed === true);
console.log(r.used <= 300);

// budget 0
r = trimForAI([{ code: 'E9', severity: 'error', message: 'hello world' }],
  { budgetTokens: 0, estimate: est });
console.log(r.kept.length === 1 && r.kept[0].trimmed === true);
console.log(trimForAI([], {}).kept.length === 0);
```

**评分点**：
- 优先级排序正确（error 先于 warn、同级保序——稳定排序）；预算装入顺序
- 保底裁剪语义（skeleton 保留 code/message 前缀，丢 snippet/hints）；全装不下时的最小保证
- budget 0 仍有最小骨架（AI 至少知道错误码）；空数组安全
- 能说清「结构化诊断是 AI 排查的最小充分上下文，日志直喂信噪比差」属于加分
