---
title: [ENG-296] 笔试题——实现灰度分流器（稳定哈希 + 分层正交 + 白名单）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## ENG-296：手写灰度分流器

**需求与边界**：
- 需求：按用户 ID 稳定分流（同用户永远同桶）；百分比灰度；白名单直进灰度；分层正交（不同实验层独立哈希）；支持紧急全量/回退开关。
- 边界：① 哈希分布均匀性（用 murmur/fnv 避免简单 hash 聚簇）；② 白名单优先于百分比；③ 开关状态（off/partial/on）语义清晰；④ 分流决策缓存（同会话同决策）。

**答**：
```javascript
function createSplitter(rules, { salt = '' } = {}) {
  const cache = new Map();                           // 会话决策缓存
  function assign(userId, layer) {
    const key = `${userId}:${layer}`;
    if (cache.has(key)) return cache.get(key);
    let result;
    const rule = rules[layer];
    if (!rule || rule.state === 'off') result = 'control';
    else if (rule.whitelist?.includes(userId)) result = 'treatment';    // 白名单优先
    else if (rule.state === 'on') result = 'treatment';
    else {
      const bucket = fnv1a(`${userId}:${layer}:${salt}`) % 10000;     // 分层盐正交
      result = bucket < rule.pct * 100 ? 'treatment' : 'control';
    }
    cache.set(key, result);
    return result;
  }
  return { assign };
}
function fnv1a(str) {
  let h = 0x811c9dc5;
  for (let i = 0; i < str.length; i++) {
    h ^= str.charCodeAt(i);
    h = Math.imul(h, 0x01000193) >>> 0;
  }
  return h;
}
// 分布自检
const dist = Array(100).fill(0);
for (let i = 0; i < 100000; i++) dist[fnv1a(String(i)) % 100]++;
console.assert(Math.max(...dist) < 1200, '分布不均');
```

**评分点**:
- 稳定哈希（fnv1a）+ 分层盐正交（SCN-ENG-253 同源）。
- 白名单 > 开关 > 百分比的优先级。
- 会话缓存（同会话同决策防抖）。
- 分布均匀性自检（简单 hash 聚簇的防御）。
