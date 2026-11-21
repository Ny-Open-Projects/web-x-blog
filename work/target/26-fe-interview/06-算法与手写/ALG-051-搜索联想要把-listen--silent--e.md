---
title: [ALG-051] 搜索联想要把 `['listen', 'silent', 'enlist', 'google']` 中互为字母异位词的词聚成一簇展示。如何分组？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-051：搜索联想要把 `['listen', 'silent', 'enlist', 'google']` 中互为字母异位词的词聚成一簇展示。如何分组？
**答**：异位词排序后相同——把每个词的字符排序结果作为 Map 的 key，原词归入对应桶。也可用 26 位字母计数字符串作 key（O(L) 而非 O(L log L)）。时间 O(n × L log L)，空间 O(n × L)。

```javascript
function groupAnagrams(words) {
  const map = new Map();
  for (const w of words) {
    const key = [...w].sort().join(''); // 异位词排序后同 key
    if (!map.has(key)) map.set(key, []);
    map.get(key).push(w);
  }
  return [...map.values()];
}
// => [['listen','silent','enlist'], ['google']]
```
