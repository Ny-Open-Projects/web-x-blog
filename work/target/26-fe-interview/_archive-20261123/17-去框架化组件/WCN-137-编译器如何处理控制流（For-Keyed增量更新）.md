---
title: [WCN-137] 编译器如何处理控制流？For 的 keyed 增量更新编译成什么代码？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 编译器方向]
type: 面试题
---

## WCN-137：编译器如何处理控制流？For 的 keyed 增量更新编译成什么代码？

**答**：
- 编译器把 `<For each={list} keyed>` 转成对 runtime helper 的调用，helper 内部做 keyed diff：新数组按 key 建索引，复用旧节点、只处理增删移。
- Solid 的 For：`createFor` 维护 key→节点映射；非 keyed（默认）按引用比对——item 对象不变则完全跳过更新（数据不可变模式下的最优路径）。
- Svelte 5 的 each：`each_block` 编译为 keyed 增量块，move 操作用 insertBefore 复位顺序（复用 DOM，不重建）。
- 与手写 diff 的差异：编译器知道循环体结构，可为每行生成精确的局部更新 effect（行内插值），而通用 diff 只能 patch。
- 展示：中间插入一个元素时，只创建新节点 + 一次 insertBefore；后续所有行不触碰。

```jsx
// Solid 源码与产物（示意）
<For each={items()} keyed>{(item) => <Row item={item} />}</For>

// 编译产物
createFor(items, (item) => Row({ item }), (item) => item.id, {
  // keyed: 插入/删除/移动走 helper 的增量算法
  // 非对象替换 → 跳过整行更新
});
```
