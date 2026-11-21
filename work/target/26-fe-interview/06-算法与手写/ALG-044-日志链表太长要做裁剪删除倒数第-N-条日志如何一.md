---
title: [ALG-044] 日志链表太长要做裁剪：删除倒数第 N 条日志。如何一次遍历定位倒数第 N 个？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-044：日志链表太长要做裁剪：删除倒数第 N 条日志。如何一次遍历定位倒数第 N 个？
**答**：快慢指针 + 哑结点：快指针先走 N 步拉开距离，然后快慢同步走，快指针到尾时慢指针停在倒数第 N+1 个，直接改指针跳过目标。哑结点免去"删头"特判。时间 O(n)，空间 O(1)。

```javascript
function removeNthFromEnd(head, n) {
  const dummy = { next: head };
  let fast = dummy, slow = dummy;
  for (let i = 0; i < n; i++) fast = fast.next; // 快指针先走 N 步
  while (fast.next) { fast = fast.next; slow = slow.next; }
  slow.next = slow.next.next; // 慢指针正好在倒数第 N+1 个
  return dummy.next;
}
```
