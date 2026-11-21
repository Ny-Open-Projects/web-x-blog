---
title: [DP-037] React/Vue 组件树和组合模式是什么关系？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-037：React/Vue 组件树和组合模式是什么关系？
**答**：
- React/Vue 的 UI 本质是组件树：组件里嵌套组件，与组合模式"部分-整体层次结构"完全同构。
- React 里每个组件的返回值是元素树，renderer 递归处理（叶子=宿主组件如 div，容器=函数/类组件）——"统一接口"就是组件这个抽象本身。
- Vue 的 slot、React 的 children 都是"把子结构当参数传入容器"，是组合模式的 API 化。
- 面试延伸：diff 算法对树做统一遍历（同层比较），正是因为结构统一才可行。

```jsx
// React：容器组件与叶子组件同构，递归渲染树形数据（组合模式思想）
const Tree = ({ node }) => (
  <div className="node">
    <span>{node.type === 'folder' ? '📁' : '📄'} {node.name}</span>
    {node.children && (
      <div className="children" style={{ paddingLeft: 16 }}>
        {node.children.map((child) => (
          <Tree key={child.name} node={child} />  // 递归：容器统一委托子节点
        ))}
      </div>
    )}
  </div>
);
const data = {
  type: 'folder', name: 'src',
  children: [
    { type: 'file', name: 'index.js' },
    { type: 'folder', name: 'components', children: [{ type: 'file', name: 'Button.vue' }] },
  ],
};
// <Tree node={data} /> —— 渲染逻辑不区分树的深度与形态

// Vue 等价形态：递归组件
// const TreeItem = {
//   props: ['node'],
//   template: `<div><span>{{ node.name }}</span>
//     <TreeItem v-for="c in node.children || []" :key="c.name" :node="c" /></div>`,
// };
```
