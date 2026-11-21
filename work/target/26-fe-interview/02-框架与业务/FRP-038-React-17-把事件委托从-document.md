---
title: [FRP-038] React 17 把事件委托从 document 改到 root，为什么？事件池为什么被移除？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-038：React 17 把事件委托从 document 改到 root，为什么？事件池为什么被移除？

**答**：
- React 16 委托在 `document`：一个页面多个 React root 时，事件会跨 root 串台（一个 root 的 stopPropagation 挡不住另一个 root）；且与其它框架共存、与原生事件混用时层级不可控。
- React 17+ 委托到**每个 root 容器**：作用域隔离、与原生事件的关系更直观（`document` 上的原生监听能正常拦截 React 事件）。
- React 16 的事件池（SyntheticEvent 复用对象，回调结束后属性置 null）经常造成"异步读 e.target 变 null"的经典 bug；17 移除事件池后事件对象可随意异步使用，代价是 GC 压力略增（现代引擎可承受）。

```jsx
// 一一对应：两个易踩坑点的前后对比
import { useState } from 'react';

export default function EventDemo() {
  const [text, setText] = useState('');

  const handleChange = (e) => {
    // React 16 坑：异步读事件对象 —— 事件池回收后 e.target 为 null
    // setTimeout(() => setText(e.target.value), 0);  // 16 中报错
    setTimeout(() => setText(e.target.value), 0);    // 17+ 正常：无事件池
  };

  return (
    <div onClickCapture={() => console.log('capture 父')} onClick={() => console.log('bubble 父')}>
      <input onChange={handleChange} />
      {/* React 17 的停止传播只作用于本 root：
          若页面上还有另一个 root 挂在 document 上（16），这里的 stopPropagation 会被绕过 */}
      <button onClick={(e) => { e.stopPropagation(); console.log('子，不再冒泡'); }}>stop</button>
      <p>{text}</p>
    </div>
  );
}
// React 17+ 委托结构：
// root 容器 ──监听 click/focus/... ──> 分发到本 root 内的 fiber 链
// document ──不再有 React 的监听
```
