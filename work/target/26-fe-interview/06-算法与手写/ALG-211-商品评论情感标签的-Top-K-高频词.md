---
title: [ALG-211] 商品详情页：从 10 万条评论里取出现次数 Top-10 情感标签（计数 + 小顶堆 O(n log k)）
date: 2026-11-19
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

**场景**：详情页要展示"用户评价高频关键词 Top 10"。10 万条评论分词后统计频次，取 Top 10。全排序 O(n log n) 浪费，标准解：计数 Map + 容量为 k 的小顶堆，O(n log k)。

**思路**：Map 计数 → 遍历频次维护 size=10 小顶堆（新频次 > 堆顶则替换）→ 堆里即 Top-k。或简化用排序取前 10（n 小时完全够）——面试要点是能给出 O(n log k) 及其适用规模。

```javascript
function topK(words, k = 10) {
  const freq = new Map();
  for (const w of words) freq.set(w, (freq.get(w) || 0) + 1);      // O(n) 计数

  const heap = [];                                                  // [count, word] 小顶堆
  const push = (e) => { heap.push(e); heap.sort((a, b) => a[0] - b[0]); };
  for (const [word, count] of freq) {                               // O(m log k)
    if (heap.length < k) push([count, word]);
    else if (count > heap[0][0]) { heap.shift(); push([count, word]); }
  }
  return heap.sort((a, b) => b[0] - a[0]).map(([c, w]) => ({ word: w, count: c }));
}
// topK(['good','bad','good','great','good','bad'], 2) => [{good,3},{bad,2}]
// 复杂度：O(n + m log k)，m=去重词数；演示用 sort 模拟堆（m log k，k=10 实际很快）
// 变体：需要"分词"则先用分词器产出词数组；中文可用 Intl.Segmenter
const seg = new Intl.Segmenter('zh', { granularity: 'word' });
[...seg.segment('很好用的手机值得推荐')].map((s) => s.segment);
```

**评分点**：
- Map 计数 + Top-k 堆的复杂度 O(n + m log k) 说清（对比全排序 O(m log m)）。
- 小顶堆替换逻辑正确（count > 堆顶才换）。
- 能按场景选择实现：10 万条评论用 Map+排序也够，百万级才必须堆/桶。
- Intl.Segmenter 中文分词的意识是加分项。
