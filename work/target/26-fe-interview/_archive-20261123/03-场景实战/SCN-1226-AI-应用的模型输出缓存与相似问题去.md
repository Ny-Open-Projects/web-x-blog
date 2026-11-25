---
title: [SCN-1226] AI 应用的模型输出缓存与相似问题去重
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1226：AI 应用的模型输出缓存与相似问题去重

**答**：
- 缓存：相同 prompt（规范化后 hash）命中缓存直接返回（秒回），命中标注。
- 失效：缓存版本随模型/参数失效（换模型不命中）。
- 控制：用户可关闭缓存（需要最新回答场景）。

```javascript
// 输出缓存
function cacheKey(prompt, model, params) {
  return hash(normalize(prompt) + model + JSON.stringify(params));
}
function normalize(p) { return p.trim().replace(/\s+/g, ' '); }
async function askWithCache(prompt, model) {
  const key = cacheKey(prompt, model);
  const cached = await cache.get(key);
  if (cached && cacheEnabled) return { ...cached, fromCache: true };
  const r = await generate(prompt, model);
  await cache.set(key, r, { ttl: 3600_000 });
  return { ...r, fromCache: false };
}
```
