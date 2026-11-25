---
title: [AIC-503] 笔试：手写 AI 上下文裁剪器
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-503：笔试：手写 AI 上下文裁剪器

**答**：实现 `trimContext(items, budget)`。items: `{ type, content, tokens, priority }[]`；budget: `{ maxTokens }`。规则：1) 按 priority 升序排序（priority 0 = 最高）；2) 贪心装入：逐个加入直到超预算——超预算的 item **跳过**（不截断单条——保持语义完整）；3) 返回 `{ included: ContextItem[], skipped: number, usedTokens: number }`。边界：items 空；单 item 超预算（跳过——不截断）；全部超预算（included 空）；budget=0。

```javascript
function trimContext(items = [], budget = { maxTokens: 4000 }) {
  const sorted = [...items].sort((a, b) => (a.priority ?? 5) - (b.priority ?? 5));
  const included = []; let usedTokens = 0; let skipped = 0;
  for (const item of sorted) {
    const tokens = item.tokens ?? estimateTokens(item.content);
    if (usedTokens + tokens > budget.maxTokens) { skipped++; continue; }  // 跳过不截断
    included.push(item); usedTokens += tokens;
  }
  return { included, skipped, usedTokens };
}
function estimateTokens(text = '') {
  // 粗估：英文 4 字符/token，中文 1.5 字符/token
  const chinese = (text.match(/[\u4e00-\u9fff]/g) ?? []).length;
  const other = text.length - chinese;
  return Math.ceil(chinese / 1.5 + other / 4);
}

// 自测
const items = [
  { type: 'rule', content: 'Use strict TypeScript', tokens: 20, priority: 0 },
  { type: 'file', content: 'const x = 1;'.repeat(100), tokens: 200, priority: 1 },
  { type: 'symbol', content: 'interface User { id: number }', tokens: 50, priority: 2 },
  { type: 'semantic', content: 'similar code...', tokens: 3000, priority: 3 },
  { type: 'file', content: 'unrelated file', tokens: 500, priority: 4 },
];
let r = trimContext(items, { maxTokens: 1000 });
console.log(r.included.length === 3);                    // rule + file + symbol = 270
console.log(r.usedTokens === 270);                       // semantic 3000 超预算跳过
console.log(r.skipped === 2);
console.log(r.included[0].type === 'rule');              // 优先级排序

// 全部超预算
r = trimContext(items, { maxTokens: 10 });
console.log(r.included.length === 0 && r.skipped === 5); // rule 20 > 10 也超

// 空
console.log(trimContext([], { maxTokens: 1000 }).included.length === 0);
```

**评分点**：
- 贪心装入（优先级排序 + 不截断单条——语义完整性优先于填满预算）
- 跳过不截断（截断的 item = 半截代码 = AI 理解错误——完整性优先）；estimateTokens 的中英文区分
- 边界（全超/空/budget=0）；优先级排序
- 能说清「上下文裁剪的核心：不截断单条（半截代码比没有更糟）——按优先级贪心装入完整条目」属于加分
