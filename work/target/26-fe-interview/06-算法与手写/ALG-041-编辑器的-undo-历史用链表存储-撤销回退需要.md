---
title: [ALG-041] 编辑器的 undo 历史用链表存储，撤销回退需要把历史链整条反转（最新变最旧）。如何原地反转单链表？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-041：编辑器的 undo 历史用链表存储，撤销回退需要把历史链整条反转（最新变最旧）。如何原地反转单链表？
**答**：三指针迭代：`prev / cur / next`，每次把 `cur.next` 指向 prev 后整体右移一位。迭代法空间 O(1) 优于递归法（递归栈 O(n)）。时间 O(n)，空间 O(1)。

```javascript
class ListNode {
  constructor(val, next = null) { this.val = val; this.next = next; }
}
function reverseList(head) {
  let prev = null, cur = head;
  while (cur) {
    const next = cur.next; // 先存后继
    cur.next = prev;       // 反指
    prev = cur;            // prev 前进
    cur = next;            // cur 前进
  }
  return prev; // 新头结点
}
```
