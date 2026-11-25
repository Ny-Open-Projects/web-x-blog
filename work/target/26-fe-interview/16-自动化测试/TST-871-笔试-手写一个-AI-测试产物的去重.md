---
title: [TST-871] 笔试：手写一个「AI 测试产物的去重/合并器」，避免重复用例
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-871：笔试：手写一个「AI 测试产物的去重/合并器」，避免重复用例
**答**：
- 需求：实现 dedupeTests(tests) —— 对 AI 生成的用例按「行为签名」去重，相似用例合并保留信息最全的一条。
- 规则：行为签名 = 被测函数 + 断言类型 + 关键输入（序列化）；同签名视为重复。
- 边界：合并时保留并集 tags 与更长的 description；非数组抛错；保持首次出现顺序。

```javascript
function behaviorSignature(t) {
  const input = JSON.stringify(t.input ?? null);
  return `${t.target}|${t.assertionType}|${input}`;
}
function dedupeTests(tests) {
  if (!Array.isArray(tests)) throw new TypeError('tests 必须是数组');
  const seen = new Map();
  for (const t of tests) {
    const sig = behaviorSignature(t);
    if (!seen.has(sig)) { seen.set(sig, { ...t }); continue; }
    const prev = seen.get(sig);
    // 合并：tags 取并集，描述保留更长的
    prev.tags = [...new Set([...(prev.tags || []), ...(t.tags || [])])];
    if ((t.description?.length || 0) > (prev.description?.length || 0))
      prev.description = t.description;
  }
  return [...seen.values()]; // Map 保持插入顺序
}
console.log(dedupeTests([
  { target: 'sum', assertionType: 'toBe', input: [1,2], tags: ['happy'] },
  { target: 'sum', assertionType: 'toBe', input: [1,2], tags: ['regression'], description: '更详细描述' },
]).length); // 1
```
**评分点**：
- 行为签名设计（目标+断言类型+关键输入）合理，能识别语义重复。
- 合并保留 tags 并集与更优 description，信息不丢失。
- 保持首次出现顺序，非数组抛错，边界健壮。
- 能点出 AI 批量生成易产生「换汤不换药」的重复用例，去重是入库必要环节。
