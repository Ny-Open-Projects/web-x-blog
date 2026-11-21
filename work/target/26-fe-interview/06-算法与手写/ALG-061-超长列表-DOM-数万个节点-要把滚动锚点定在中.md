---
title: [ALG-061] 超长列表（DOM 数万个节点）要把"滚动锚点"定在中间元素上以平衡上下白屏。如何 O(n) 时间 O(1) 空间找链表/数组中间元素（快慢指针）？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-061：超长列表（DOM 数万个节点）要把"滚动锚点"定在中间元素上以平衡上下白屏。如何 O(n) 时间 O(1) 空间找链表/数组中间元素（快慢指针）？
**答**：快指针每次走 2 步、慢指针走 1 步，快指针到尾时慢指针恰在中间（偶数长度时为中点偏后）。数组可直接下标取，但链表结构（如虚拟列表的块链）只能快慢指针。时间 O(n)，空间 O(1)。

```javascript
function middleNode(head) {
  let slow = head, fast = head;
  while (fast && fast.next) {
    slow = slow.next;      // 1 步
    fast = fast.next.next; // 2 步
  }
  return slow; // 偶数长度返回中间偏后那个
}
```
