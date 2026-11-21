---
title: [ALG-017] 搜索日志有几百万条关键词，要实时算出出现次数 Top 10 的热词。为什么用"哈希计数 + 容量为 K 的小顶堆"而不是全量排序？请实现核心逻辑。
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-017：搜索日志有几百万条关键词，要实时算出出现次数 Top 10 的热词。为什么用"哈希计数 + 容量为 K 的小顶堆"而不是全量排序？请实现核心逻辑。
**答**：全量排序 O(n log n) 且要一次性装下所有数据；正确做法是先 `Map` 计数 O(n)，再维护一个容量为 K 的**小顶堆**：堆顶是当前第 K 大，新词频次若大于堆顶才替换并下沉。内存只需 O(K)，总时间 O(n log K)；海量数据下还可分片统计再归并。时间 O(n log K)，空间 O(K)（堆）+ O(n)（计数）。

```javascript
function topK(words, k) {
  const freq = new Map();
  for (const w of words) freq.set(w, (freq.get(w) || 0) + 1);
  const heap = []; // 小顶堆，元素为 [词, 次数]
  const up = i => {
    while (i > 0) {
      const p = (i - 1) >> 1;
      if (heap[p][1] <= heap[i][1]) break;
      [heap[p], heap[i]] = [heap[i], heap[p]]; i = p;
    }
  };
  const down = () => {
    let i = 0;
    for (;;) {
      const l = 2 * i + 1, r = l + 1; let m = i;
      if (l < heap.length && heap[l][1] < heap[m][1]) m = l;
      if (r < heap.length && heap[r][1] < heap[m][1]) m = r;
      if (m === i) break;
      [heap[m], heap[i]] = [heap[i], heap[m]]; i = m;
    }
  };
  for (const item of freq) {
    if (heap.length < k) { heap.push(item); up(heap.length - 1); }
    else if (item[1] > heap[0][1]) { heap[0] = item; down(); }
  }
  return heap.sort((a, b) => b[1] - a[1]).map(([w]) => w);
}
```
