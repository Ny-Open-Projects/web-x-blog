---
title: [FRP-044] key 在 diff 中的源码级作用是什么？为什么用 index 当 key 会出问题？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-044：key 在 diff 中的源码级作用是什么？为什么用 index 当 key 会出问题？

**答**：
- reconcileChildren 中，新旧 children 都有 key 时会构建 **`key -> 旧 fiber` 的 Map**（existingChildren），新列表逐项用 `key + type` 查旧 fiber：查到就复用更新，查不到就新建，Map 里剩余的在最后统一删除。
- key 相同 + type 相同 → 复用 fiber（保住 DOM 节点与 state）；key 相同 type 不同 → 复用 key 但重建节点；key 不同 → 销毁重建。
- 用 index 当 key：列表头部插入一项后，所有项的 key 位置对不上，**全部按错位复用**——input 等非受控状态串行、组件 state 错乱、动画错位；更新本身还触发全量 patch。
- 结论：key 只要求"**同层级列表内唯一且稳定**"，用业务 id；无状态纯展示的短列表用 index 退化可行，但一旦涉及输入/动画就是 bug 温床。

```javascript
// 简化实现，帮助理解 keyed diff 的 Map 复用
function reconcileKeyedChildren(oldChildren, newChildren, container) {
  // 1. 建立 key -> 旧 fiber 的映射（源码 existingChildren: Map）
  const existingChildren = new Map();
  oldChildren.forEach((child) => existingChildren.set(child.key, child));

  // 2. 遍历新列表，按 key 复用
  newChildren.forEach((newChild, i) => {
    const oldChild = existingChildren.get(newChild.key);
    if (oldChild) {
      existingChildren.delete(newChild.key);   // 匹配上：从待删除集合移除
      if (oldChild.type === newChild.type) {
        patch(oldChild, newChild, container);  // key + type 相同：复用 fiber 与 DOM
        // DOM 不重建，组件 state 保留 —— 这就是 key 保状态的意义
      } else {
        unmount(oldChild);
        mount(newChild, container);
      }
    } else {
      mount(newChild, container);              // 没有匹配 key：全新创建
    }
  });

  // 3. 剩下的旧节点 = 新列表中已不存在的，统一卸载
  existingChildren.forEach((leftover) => unmount(leftover));
}

// index 当 key 的错位演示：
// 旧：[{key:0,A},{key:1,B},{key:2,C}]  新头部插入 D：
// 新：[{key:0,D},{key:1,A},{key:2,B},{key:3,C}]
// key=0 上 A 被当 D 复用 —— A 的 input 值显示给了 D，全部串位
```
