---
title: [MFW-019] 笔试：实现内存版 tag 失效缓存（get/set/revalidateTag）
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-019：笔试：实现内存版 tag 失效缓存（get/set/revalidateTag）
**题目**：实现 `createTagCache()`：`get(key, fn, tags)` 读缓存（命中返回值，未命中执行 fn 并按 tags 记录）；`revalidateTag(tag)` 使所有含该 tag 的条目立即失效（下一次 get 重算）；`revalidateTag` 后**正在进行的 get 不得回写旧值**。要求 O(1) 失效，支持时间过期兜底。

```javascript
function createTagCache({ defaultTTL = 60_000 } = {}) {
  const entries = new Map();     // key -> { value, expireAt, tags, epoch }
  const tagIndex = new Map();    // tag -> Set(key)，O(1) 找到失效目标
  let globalEpoch = 0;           // 失效代次：失效即 +1

  function indexTags(key, tags) {
    for (const t of tags) {
      if (!tagIndex.has(t)) tagIndex.set(t, new Set());
      tagIndex.get(t).add(key);
    }
  }

  async function get(key, fn, tags = [], ttl = defaultTTL) {
    const myEpoch = globalEpoch;              // 记住调用时的代次
    const hit = entries.get(key);
    if (hit && hit.expireAt > Date.now()) return hit.value;
    const value = await fn();                 // 重新计算
    if (myEpoch !== globalEpoch) return value; // 计算期间发生失效：只返回，不回写旧值
    entries.set(key, { value, expireAt: Date.now() + ttl, tags, });
    indexTags(key, tags);
    return value;
  }

  function revalidateTag(tag) {
    globalEpoch += 1;                         // 让所有 in-flight 计算作废回写
    const keys = tagIndex.get(tag) ?? new Set();
    for (const k of keys) entries.delete(k);  // 精准删除该 tag 的条目
    tagIndex.delete(tag);
  }

  return { get, revalidateTag };
}

// ---- 用法 ----
const cache = createTagCache();
await cache.get('product:1', () => fetchProduct(1), ['product-1', 'products']);
cache.revalidateTag('product-1'); // 下一次 get 重算，in-flight 旧值不会污染缓存

// **评分点**
// 1. tag -> keys 倒排索引，失效 O(相关条目数) 而非全表扫描。
// 2. in-flight 防回写：用「代次/epoch」比对，读题中“正在进行的 get 不得回写旧值”是否处理——最大失分点。
// 3. 时间过期兜底 + 失效即删，语义区分清楚（过期可后台刷新，失效必须重算）。
// 4. 单例 epoch 自增的正确性：任何一次 revalidateTag 都要作废所有 in-flight，不只是目标 tag。
```
