---
title: [FRP-088] completeWork 里的单链表 diff 具体怎么处理四种情况？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-088：completeWork 里的单链表 diff 具体怎么处理四种情况？

**答**：
- reconcile 子节点是**新 children（JSX 数组）与旧 fiber 单链表**的双指针问题，React 归结为四步：①**从头部开始**，新既单点比较（同 type 复用）直到遇到不可复用的节点；②**从尾部开始**同理，确定共同前缀/后缀。
- ③若旧链表遍历完而新 children 还有剩余 → **尾部新增**（剩余的标记 Placement 插入）；若新遍历完旧还有剩余 → **尾部删除**（旧链表剩余的标记 Deletion）。
- ④**中间乱序**：把剩余旧 fiber 按 `key` 建 Map，遍历剩余新 children——key 命中则复用并标记移动（Placement，记录 oldIndex 算 LIS 决定是否真移动），未命中则新建，Map 里没被消耗的旧 fiber 标记 Deletion。
- 与 Vue 的对比：React 用 Map 复用 + `lastPlacedIndex` 贪心判定是否移动（无 LIS）；Vue3 同为"同步头尾 + 乱序 keyToNewIndexMap"，再用**最长递增子序列**决定最少移动，思想同源（都是同层 diff）。

```javascript
// 简化实现，帮助理解单链表 diff 的四种情况
function diffChildren(parentFiber, newChildren) {
  const oldFirst = parentFiber.child;
  // 情况 1：同步头部——旧的复用直到不匹配
  let i = 0, oldFiber = oldFirst, lastPlaced = null;
  while (i < newChildren.length && oldFiber && newChildren[i].key === oldFiber.key) {
    newChildren[i].fiber = oldFiber; oldFiber.flags = 'Update';
    lastPlaced = newChildren[i].fiber;
    oldFiber = oldFiber.sibling; i++;
  }
  // 情况 2：同步尾部——从后往前复用
  let j = newChildren.length - 1;
  let oldLast = oldFiber; while (oldLast?.sibling) oldLast = oldLast.sibling;
  while (j >= i && oldLast && newChildren[j].key === oldLast.key) {
    newChildren[j].fiber = oldLast; oldLast.flags = 'Update';
    oldLast = prevSibling(oldFirst, oldLast); j--;
  }
  if (i <= j && !oldFiber) {
    // 情况 3a：旧链表已耗尽，新 children 剩余 -> 全部新增
    newChildren.slice(i, j + 1).forEach((c) => (c.fiber = { key: c.key, flags: 'Placement' }));
    return 'append tail';
  }
  if (i > j && oldFiber) {
    // 情况 3b：新 children 耗尽，旧剩余 -> 全部删除
    for (let f = oldFiber; f; f = f.sibling) f.flags = 'Deletion';
    return 'delete tail';
  }
  // 情况 4：中间乱序——key -> 新下标 Map
  const keyMap = new Map();
  for (let k = i; k <= j; k++) keyMap.set(newChildren[k].key, k);
  for (let f = oldFiber; f; f = f.sibling) {
    if (keyMap.has(f.key)) { f.flags = 'Move'; keyMap.delete(f.key); } // 复用+移动判定
    else f.flags = 'Deletion';                                          // 未被消耗
  }
  newChildren.slice(i, j + 1).forEach((c) => {
    if (!c.fiber) c.fiber = keyMap.size >= 0 ? { key: c.key, flags: 'Placement' } : null;
  });
  // 真实实现：React 用 lastPlacedIndex 贪心判定移动；Vue3 计算最长递增子序列，LIS 内的节点不动、之外的标记移动
  return 'reorder middle';
}
const prevSibling = (head, node) => { let p = head; while (p && p.sibling !== node) p = p.sibling; return p; };

// 验证四种情况
console.log(diffChildren({ child: { key: 'a', sibling: { key: 'b', flags: 'Update', sibling: null } } },
  [{ key: 'a' }])); // delete tail：旧 b 被删
```
