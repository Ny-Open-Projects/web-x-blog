---
title: [JS-155] 链表结构在 JS 中如何实现与应用？LRU 的底层思想是什么？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-155：链表结构在 JS 中如何实现与应用？LRU 的底层思想是什么？

**答**：
- 单向链表：节点存 value 与 next，插入删除 O(1)，但查找必须从头遍历 O(n)——JS 数组反而随机访问快。
- 反转链表三指针法：prev/cur/next 逐个翻转指向，是最高频链表手写题。
- LRU 的 O(1) 秘密：哈希表负责 O(1) 定位，双向链表负责 O(1) 摘除与头插，二者配合。
- 双向链表的优势：拿到任意节点引用即可 O(1) 摘除（无需找前驱），这正是 LRU 需要的。

```javascript
class Node {
  constructor(value) { this.value = value; this.next = null; }
}
class LinkedList {
  constructor() { this.head = null; this.size = 0; }
  append(value) {
    const node = new Node(value);
    if (!this.head) this.head = node;
    else {
      let cur = this.head;
      while (cur.next) cur = cur.next;   // 尾插需遍历 O(n)
      cur.next = node;
    }
    this.size++;
  }
  reverse() {                            // 三指针原地反转
    let prev = null, cur = this.head;
    while (cur) {
      const next = cur.next;             // 先存后继
      cur.next = prev;                   // 翻转指向
      prev = cur;                        // prev 前进
      cur = next;                        // cur 前进
    }
    this.head = prev;                    // 新头是原尾
  }
  toArray() {
    const out = []; let cur = this.head;
    while (cur) { out.push(cur.value); cur = cur.next; }
    return out;
  }
}
const list = new LinkedList();
list.append(1); list.append(2); list.append(3);
list.reverse();
console.log(list.toArray());   // [3, 2, 1]

// 双向链表节点：LRU O(1) 的底层支撑
class DNode {
  constructor(key, value) { this.key = key; this.value = value; this.prev = null; this.next = null; }
}
function moveToHead(head, node) {   // LRU 命中时的核心动作
  node.prev.next = node.next;       // O(1) 摘除：无需遍历找前驱
  node.next.prev = node.prev;
  node.next = head.next;            // 头插：最近使用的放头部
  node.prev = head;
  head.next.prev = node;
  head.next = node;
}
// 配合 Map<key, DNode>，get/put 都是 O(1)；链表尾部的节点即「最久未使用」，容量满时淘汰
```
