---
title: [1188] embedding 缓存什么时候会「答非所问」
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 缓存]
type: 面试题
---

## 1188：embedding 缓存什么时候会「答非所问」

**答**：
- 三个陷阱：模型版本未入 key（升级模型后命中旧向量——空间不兼容，检索全乱）、文本规范化不一致（写入时 trim 了查询时没 trim，同文本不同 key 缓存永不命中）、预处理注入缓存（改写后的 query 进缓存——改写策略一变全串）。
- 正确姿势：key = hash(规范化文本 + 模型版本 + 预处理版本)；命中也要「抽检」（按比例验证向量与当前模型输出的一致性，防供应商静默升级）。
- 清理策略：模型升级触发按版本前缀批量清理（旧版本向量无用），别让死缓存占内存。
- 追问钩子：为什么「预处理版本」也要进 key？——预处理（分词/清洗）是向量的前置函数，预处理变了同文本向量就不同；不进 key 会得到「看起来命中实则错位」的缓存。

```ts
async function embedCached(text) {
  const norm = normalize(text);                    // 规范化固定
  const key = hash([norm, MODEL_VER, PREPROCESS_VER].join('|')); // 三要素入 key
  const hit = await vecCache.get(key);
  if (hit && sampleCheck(hit)) return hit;         // 抽检一致性
  const vec = await embed(norm);
  await vecCache.set(key, vec);
  return vec;
}
// 模型升级：按版本前缀清理
onModelUpgrade(() => vecCache.deleteByPrefix(':' + OLD_VER));
```
