---
title: [TST-865] 笔试：手写一个「测试用例的 self-healing 定位器」（AI 修复失效 selector）
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-865：笔试：手写一个「测试用例的 self-healing 定位器」（AI 修复失效 selector）
**答**：
- 需求：实现 selfHealLocator(original, candidates, dom) —— 原选择器失效时，从候选选择器中选出一个在 dom 中唯一匹配的元素。
- 规则：按候选相似度/优先级排序；选出匹配数 === 1 的候选作为修复结果；都失败返回 null 并记录原因。
- 边界：dom 用 querySelectorAll 模拟；原选择器仍有效则直接返回原值（无需修复）。

```javascript
function selfHealLocator(original, candidates, dom) {
  const query = (sel) => {
    try { return dom.querySelectorAll(sel).length; } catch { return -1; }
  };
  if (query(original) === 1) return { locator: original, healed: false };
  const tried = [];
  for (const sel of candidates) {
    const count = query(sel);
    tried.push({ sel, count });
    if (count === 1) return { locator: sel, healed: true, from: original };
  }
  return { locator: null, healed: false, reason: '无唯一匹配候选', tried };
}
// 模拟 DOM（真实用 jsdom / Playwright）
const dom = { querySelectorAll: sel => sel === '.btn-new' ? [{}] : [] };
console.log(selfHealLocator('.btn-old', ['#submit', '.btn-new'], dom));
// { locator:'.btn-new', healed:true } —— AI 可据此自动修复用例并记录

// 候选都失败时返回 null，转人工而非盲目修复
console.log(selfHealLocator('.btn-old', ['#missing'], dom));
// { locator:null, healed:false, tried:[...] } —— 需人工确认
// 原选择器仍有效时不触发自愈，避免无谓改动
```
**评分点**：
- 原选择器有效则无需修复，逻辑正确。
- 候选选择器选「唯一匹配（count===1）」者，避免误修复到多个元素。
- 失败返回 null 并记录 tried 便于审计与重新训练。
- 能点出 self-healing 需「记录修复原因 + 人工抽检」防止错误自愈。
