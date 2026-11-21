---
title: [R19-120] React 与微前端集成的要点？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-120：React 与微前端集成的要点？
**答**：
- 四大隔离：JS 沙箱（Proxy 快照）、样式隔离（scoped/Shadow DOM）、路由同步、公共依赖共享。
- React 双实例是头号坑：主子应用必须共享同一个 React/ReactDOM（external 化），否则 Hook 报 Invalid hook call。
- 子应用生命周期对齐：mount 用 createRoot，unmount 必须 root.unmount()，否则内存泄漏与事件残留。
- 通信收敛到一个 props/全局事件总线，禁止子应用直接操作主应用 DOM。

```jsx
// 微前端集成：qiankun 主应用 + React 子应用
import { registerMicroApps, start } from 'qiankun';
import { createRoot } from 'react-dom/client';

registerMicroApps([
  {
    name: 'order-app',
    entry: '//localhost:7101',
    container: '#sub-container',
    activeRule: '/order',
    props: { token: getSharedToken() },   // 下发共享上下文
  },
]);
start({ experimentalStyleIsolation: true });   // 样式 scoped 隔离

// 子应用生命周期，React 挂载/卸载对齐
let root = null;

export async function mount(props) {
  root = createRoot(props.container.querySelector('#root'));
  root.render(<App />);
}

export async function unmount() {
  root.unmount();   // 必须真正卸载，否则内存泄漏与事件残留
  root = null;
}
// 关键决策：React/ReactDOM 配 external 由主应用提供，避免子应用各自打包引发多实例
```
