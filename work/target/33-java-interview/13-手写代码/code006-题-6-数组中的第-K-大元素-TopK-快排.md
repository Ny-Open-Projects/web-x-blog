---
title: "题 6：数组中的第 K 大元素（TopK，快排 partition / 小顶堆）"
date: 2026-11-18
categories: [Java面试, 手写代码]
tags: [Java面试, 手写题, 33]
type: 手写题
disableNunjucks: true
---

## 题 6：数组中的第 K 大元素（TopK，快排 partition / 小顶堆）

**堆版（背这个，10 行）**：

```java
public int findKthLargest(int[] nums, int k) {
    PriorityQueue<Integer> minHeap = new PriorityQueue<>(k);   // 小顶堆
    for (int n : nums) {
        if (minHeap.size() < k) minHeap.offer(n);
        else if (n > minHeap.peek()) { minHeap.poll(); minHeap.offer(n); }
    }
    return minHeap.peek();
}
// 时间 O(n log k)，空间 O(k) —— 适合 n 大 k 小（TopK 热点词场景）
```

**快排 partition 版（追问时口述思路即可）**：随机选 pivot，partition 后若 pivot 位置正好是 n-k 就命中；偏左递归右、偏右递归左。平均 O(n)（每轮只走一半），最坏 O(n²)（随机化避免）。**追问"数据流实时 TopK"** → 堆 + 固定内存；"海量分片数据 TopK" → 各分片本地 TopK 再归并（map-reduce 思想）。

---
