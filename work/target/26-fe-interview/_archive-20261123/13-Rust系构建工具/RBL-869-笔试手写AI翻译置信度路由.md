---
title: [RBL-869] 笔试：手写 AI 翻译置信度路由器（规则先行 + LLM 兜底 + 人工闸门）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-869：笔试：手写 AI 翻译置信度路由器（规则 + LLM + 人工）

**需求**：实现 `routeTranslate(items, { rules, llm, verifier, cache })`。items: 迁移项数组；rules: `Array<{ match(item), apply(item) -> { result, confidence: 1 } }>`；llm: `translate(item, ctx) -> Promise<{ result, confidence }>`；verifier: `verify(result) -> Promise<{ ok, confidence, reason? }>`。规则：1) 规则命中（match）→ 直接采纳（确定性，confidence 1）；2) 未命中 → LLM 翻译（缓存：同 item key 只调一次）→ verifier 验证；3) 综合置信 = llm.confidence × verifier.confidence：> 0.85 采纳（llm 组）、> 0.5 转人工（manual 组附候选）、≤ 0.5 丢弃（manual 组 reason 'low-confidence'）；4) verifier.ok = false 直接 manual。返回 `{ adopted: Array, manual: Array }`（各含来源标签 rule/llm）。边界：items 空；llm 抛错按 manual 处理。

```javascript
async function routeTranslate(items = [], { rules = [], llm, verifier, cache } = {}) {
  const adopted = [], manual = [];
  for (const item of items) {
    const rule = rules.find(r => r.match(item));
    if (rule) {
      const r = rule.apply(item);
      adopted.push({ item, result: r.result, source: 'rule', confidence: 1 });
      continue;
    }
    if (!llm) { manual.push({ item, reason: 'no-llm' }); continue; }
    let cand;
    try {
      const key = JSON.stringify(item);
      cand = cache?.has?.(key) ? cache.get(key) : await llm.translate(item);
      cache?.set?.(key, cand);
    } catch (e) {
      manual.push({ item, reason: 'llm-error', detail: e.message });
      continue;
    }
    const v = await verifier.verify(cand.result);
    const conf = (cand.confidence ?? 1) * (v.confidence ?? 1);
    if (!v.ok || conf <= 0.5)
      manual.push({ item, candidate: cand.result, reason: !v.ok ? v.reason : 'low-confidence' });
    else if (conf > 0.85)
      adopted.push({ item, result: cand.result, source: 'llm', confidence: +conf.toFixed(2) });
    else
      manual.push({ item, candidate: cand.result, reason: 'needs-review' });
  }
  return { adopted, manual };
}

// 自测
const rules = [{ match: (i) => i.type === 'alias', apply: (i) => ({ result: `alias:${i.value}`, confidence: 1 }) }];
const llmCache = new Map();
const llm = { translate: async (item) => {
  if (item.type === 'hard') return { result: null, confidence: 0.4 };
  return { result: `llm:${item.type}`, confidence: 0.95 };
} };
const verifier = { verify: async (result) =>
  result === null ? { ok: false, confidence: 0, reason: 'invalid' }
  : { ok: true, confidence: 0.95 } };

let r = await routeTranslate([
  { type: 'alias', value: '@' },                        // 规则
  { type: 'plugin', name: 'x' },                        // LLM 高置信
  { type: 'hard' },                                     // LLM 低置信 -> manual
  { type: 'plugin', name: 'x' },                        // 缓存命中同结果
], { rules, llm, verifier, cache: llmCache });
console.log(r.adopted.length === 3);
console.log(r.adopted[0].source === 'rule' && r.adopted[1].source === 'llm');
console.log(r.manual.length === 1 && r.manual[0].reason === 'invalid');
console.log(llmCache.size === 2);                       // hard 也缓存了

// 无 llm
r = await routeTranslate([{ type: 'unknown' }], { rules });
console.log(r.manual[0].reason === 'no-llm');
console.log((await routeTranslate([], { rules, llm, verifier })).adopted.length === 0);
```

**评分点**：
- 三层路由正确：规则确定性优先（confidence 1）、LLM 兜底缓存、置信分档（>0.85 采纳 / >0.5 人工 / ≤0.5 丢弃）
- verifier 失败直接 manual（验证闸门优先于置信数值）；LLM 抛错按 manual 不中断
- 边界：空 items、无 llm、缓存命中同结果
- 能说清「确定性优先 + AI 兜底 + 验证闸门三层防线让 AI 参与不降可靠性」属于加分
