---
title: [R19-038] Fiber 架构的双缓存与可中断渲染是怎么回事？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-038：Fiber 架构的双缓存与可中断渲染是怎么回事？
**答**：
- 每个组件对应一个 Fiber 节点，Fiber 树以链表结构组织，支持暂停后从任意节点恢复。
- 双缓存：current 树对应当前屏幕，workInProgress 树在内存中构建，构建完一次性替换。
- render 阶段可中断、可丢弃，因此必须无副作用；commit 阶段同步不可中断。
- createRoot 是启用并发能力的前提，ReactDOM.render 的旧模式不支持可中断渲染。

```jsx
import { createRoot } from 'react-dom/client';

// createRoot 开启并发渲染能力
const root = createRoot(document.getElementById('root'));
root.render(<App />);

// Fiber 双缓存要点：
// current 树对应当前屏幕，workInProgress 树在内存中构建
// render 阶段按优先级分片执行，可中断可重来
// commit 阶段同步提交 DOM，保证界面不出现半成品
```
