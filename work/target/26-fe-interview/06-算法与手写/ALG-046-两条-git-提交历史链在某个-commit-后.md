---
title: [ALG-046] 两条 git 提交历史链在某个 commit 后共享同一段历史（rebase 导致），要找到两条链表的相交节点。如何 O(1) 空间求交点？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-046：两条 git 提交历史链在某个 commit 后共享同一段历史（rebase 导致），要找到两条链表的相交节点。如何 O(1) 空间求交点？
**答**：双指针 p、q 分别从 a、b 出发，走到尾就"换轨"到另一条链。两指针走过的总步数都是 a+b+c（a 为独有段+共享段交叉抵消），必然在交点相遇；不相交则同时到达 null。时间 O(m + n)，空间 O(1)。

```javascript
function getIntersection(a, b) {
  if (!a || !b) return null;
  let p = a, q = b;
  while (p !== q) {
    p = p ? p.next : b; // 走到尾就切到另一条链，抵消长度差
    q = q ? q.next : a;
  }
  return p; // 交点，或 null（不相交）
}
```
