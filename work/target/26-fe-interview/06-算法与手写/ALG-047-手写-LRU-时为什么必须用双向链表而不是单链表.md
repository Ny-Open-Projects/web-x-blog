---
title: [ALG-047] 手写 LRU 时为什么必须用双向链表而不是单链表？请给出双向链表节点与三个关键 O(1) 操作的实现。
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-047：手写 LRU 时为什么必须用双向链表而不是单链表？请给出双向链表节点与三个关键 O(1) 操作的实现。
**答**：LRU 淘汰"最久未使用"，需要：命中时把节点移到头部——单链表拿到节点后无法 O(1) 拿前驱，删不了自己；双向链表配合 hash 表（Map）即可全部 O(1)。节点必须同时存 key：淘汰尾部节点时要靠 `node.key` 反查并删除 Map 里的记录。get/put 均 O(1)，空间 O(capacity)。

```javascript
class DNode {
  constructor(key, val) { this.key = key; this.val = val; this.prev = null; this.next = null; }
}
// 三个关键操作（配哨兵头尾使用）：
function remove(node) {
  node.prev.next = node.next;
  node.next.prev = node.prev;
}
function addToHead(node, head) {
  node.next = head.next; node.prev = head;
  head.next.prev = node; head.next = node;
}
function moveToHead(node, head) { remove(node); addToHead(node, head); }
// get(key)：Map 取节点 => moveToHead => 返回 val
// put(key, val)：已存在则更新 + moveToHead；不存在则头插新节点，
// 超容量时取 tail.prev，remove + 按 node.key 从 Map 删除。
```

---

## 六、哈希与设计
