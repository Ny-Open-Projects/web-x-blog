---
title: [FRP-047] 虚拟 DOM 的价值与代价分别是什么？为什么不直接操作 DOM？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-047：虚拟 DOM 的价值与代价分别是什么？为什么不直接操作 DOM？

**答**：
- 价值一：**声明式**——开发者描述"UI 应该是什么样"，框架负责算出最小 DOM 操作，心智负担远低于手动增删改查。
- 价值二：**跨平台**——vnode 与具体渲染器解耦，同一套组件代码可渲染到 DOM、Native、Canvas、SSR 字符串。
- 价值三：**批量与最小化更新**——diff 后合并操作，避免高频手动 DOM 操作引发的重排风暴。
- 代价：创建 vnode 与 diff 的 JS 开销；"最优 diff 是 O(n)" 依赖启发式（同层比较、key），某些场景手写 DOM 操作更快；因此 Vue3 用编译期信息减少 diff 范围，Svelte 干脆编译期生成直接操作 DOM 的代码。

```javascript
// 一一对应：手动 DOM 操作 vs 虚拟 DOM diff
// —— 手动操作：每次都要自己算"改哪里"，容易过度操作 ——
function updateUserManually(user) {
  document.querySelector('#name').textContent = user.name;      // 总是写
  document.querySelector('#age').textContent = user.age;        // 总是写，即使没变
  // 忘记某处？UI 与数据不一致；写多了？多余的重排
}

// —— 虚拟 DOM：声明目标状态，框架 diff 出最小操作 ——
function render(user) {
  return h('div', null, [
    h('span', { id: 'name' }, user.name),
    h('span', { id: 'age' }, String(user.age)),
  ]);
}
// patch(prevVnode, nextVnode) 内部：
//   同层比较 type/key -> 复用 DOM 节点
//   文本没变 -> 什么都不做（比手动少一次 DOM 写入）
//   只有变化的属性才 setAttribute

// 代价演示：vnode 创建与 diff 本身有 JS 成本
console.time('vnode');
render({ name: 'x', age: 1 }); // 每次渲染都要新建整棵 vnode 树
console.timeEnd('vnode');      // 小树微秒级；万级节点列表就明显 -> 配合虚拟列表/编译优化
```
