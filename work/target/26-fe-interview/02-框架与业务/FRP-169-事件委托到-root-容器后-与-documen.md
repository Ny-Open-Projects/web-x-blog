---
title: [FRP-169] 事件委托到 root 容器后，与 document 委托时代有哪些行为差异？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-169：事件委托到 root 容器后，与 document 委托时代有哪些行为差异？

**答**：
- React17 前所有事件委托在 `document`，17+ 移到 **root 容器**——同一页面多个 React 应用不再通过 document 互相串扰，也为渐进迁移（新旧应用并存）铺路。
- 委托层级变化影响与**原生监听器的时序**：挂 window/document 的原生 listener 会在 React 合成事件**之前**（捕获/冒泡阶段不同）触发——迁移时常见"以前 stopPropagation 能挡住，现在挡不住"的问题。
- 合成事件的 `e.stopPropagation()` 只阻止**合成传播**（React 模拟的冒泡链），原生事件已到达 root——要阻止原生传播需 `e.nativeEvent.stopImmediatePropagation()` 或在 root 外层挂原生监听。
- 附加变化：onScroll 不再冒泡（对齐原生）、事件池在 17 移除（e 对象可异步持有）。

```javascript
// 简化实现，帮助理解委托层级与时序
// —— React16：document 委托 ——
document.addEventListener('click', dispatchSimulatedClick);      // 冒泡阶段
// 多个 React 应用 + 第三方库都在 document 上，listeners 顺序互相干扰

// —— React17+：root 委托 ——
function createRoot(container) {
  // 捕获与冒泡两套都挂，覆盖全部事件类型
  for (const type of allDelegatedEvents) {
    container.addEventListener(type, dispatchEvent, false);        // 冒泡
    container.addEventListener(type, dispatchCaptureEvent, true);  // 捕获
  }
}

// —— 时序差异验证 ——
document.addEventListener('click', () => console.log('document 原生'));
// <div onClick={() => console.log('react 合成')}>   （React17+）
// 点击输出：react 合成 先于 document 原生 —— 因为委托在 root，root 更深（先冒泡到）
// React16 时顺序相反：document 委托先触发

// —— stopPropagation 的影响 ——
function Inner() {
  return <button onClick={(e) => e.stopPropagation()}>stop</button>;
}
// 合成层面：外层 React onClick 不会触发（模拟冒泡被截断）✓
// 原生层面：click 事件仍然冒泡到 document！
document.addEventListener('click', () => console.log('仍会触发 —— 原生已到达'));
// 要彻底阻断原生传播：
// e.nativeEvent.stopImmediatePropagation() —— 但这只影响 root 之后的原生 listener
// 正确做法：外部原生 listener 挂在比 root 更早的位置（如 window 捕获阶段）

// —— 捕获阶段对齐 ——
// <div onClickCapture={...}> -> dispatchCaptureEvent：用原生捕获阶段真实时序
// 合成事件的 capture 版本与原生捕获顺序完全一致（React16 是模拟，时序有偏差）
```
