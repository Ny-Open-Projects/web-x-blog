---
title: [ALG-042] 两个埋点 SDK 各自按时间升序产出日志链表，要合并成一条全局有序日志流。如何合并两个有序链表？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-042：两个埋点 SDK 各自按时间升序产出日志链表，要合并成一条全局有序日志流。如何合并两个有序链表？
**答**：经典归并：哑结点 dummy 简化头处理，双指针比较 `time`，小者接上并前进；任一为空后把剩余整段接上。时间 O(m + n)，空间 O(1)。

```javascript
function mergeLogs(a, b) {
  const dummy = { time: 0, next: null };
  let cur = dummy;
  while (a && b) {
    if (a.time <= b.time) { cur.next = a; a = a.next; }
    else { cur.next = b; b = b.next; }
    cur = cur.next;
  }
  cur.next = a || b; // 拼接剩余段
  return dummy.next;
}
```
