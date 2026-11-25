---
title: [ALG-207] IM 多设备同步：k 条会话各自按时间有序，合并最近 N 条消息（小顶堆多路归并）
date: 2026-11-19
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---
## ALG-207：IM 多设备同步：k 条会话各自按时间有序，合并最近 N 条消息（小顶堆多路归并）
**答**：IM 客户端同步 k 个设备/会话的增量消息，每条会话内消息按时间升序。要取**全局最近 N 条**渲染时间线。k 路归并：小顶堆放每路"当前最旧/最新"指针，弹堆顶取下一条。若求"最近 N 条"（最新优先）：每路倒序 + 大顶堆，或正序小顶堆全归并后取尾部。

**思路**：正序小顶堆（值=消息时间），归并出全量有序流，同时维护长度 N 的队列取尾部更省——直接反向：堆存"最新消息"，取最大者输出，N 次循环。

```javascript
function latestMessages(streams, n) {
  // streams: 每路按时间升序的数组
  const heap = [];                                   // 小顶堆存 [ts, streamIdx, msgIdx]
  const push = (t) => { heap.push(t); heap.sort((a, b) => a[0] - b[0]); }; // 简化版堆（演示用）
  for (let s = 0; s < streams.length; s++) {
    if (streams[s].length) push([streams[s][0].ts, s, 0]);
  }
  const out = [];
  while (heap.length && out.length < streams.reduce((a, s) => a + s.length, 0)) {
    const [, s, i] = heap.shift();                   // 取全局最旧
    out.push(streams[s][i]);
    if (i + 1 < streams[s].length) push([streams[s][i + 1].ts, s, i + 1]);
  }
  return out.slice(-n);                              // 全量有序流的最后 N 条 = 最近 N 条
}
// 进阶：只要最近 N 条时不需全量归并——反向大顶堆取 N 个，O(N log k)
// streams[[{ts:1},{ts:5}], [{ts:3},{ts:9}]], n=2 => 全序 [1,3,5,9] => 最近 2 条 [5,9]
// 真实工程：用成熟的二叉堆实现（sort 的 O(n) 换成堆 O(log k)），本例演示逻辑
```

**评分点**：
- 多路归并结构正确：堆里放 (ts, 路号, 指针)，弹顶推进对应路。
- "最近 N 条"用全量归并尾部（正确但非最优），能指出 O(N log k) 反向取法。
- 复杂度：演示版 O(M log M)（sort 版堆），标准堆 O(M log k)。
- 能对应场景：IM 多端消息时间线合并。
