---
title: [WCN-067] Qwik 的 signal/store 与其延迟执行（resumability）模型怎么配合？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Signals]
type: 面试题
---

## WCN-067：Qwik 的 signal/store 与其延迟执行（resumability）模型怎么配合？

**答**：
- Qwik 的目标：首屏 0 JS，交互时按需恢复（resume）。状态不靠"水合"重放，而是序列化进 HTML（`q:id`），闭包拆分成可单独懒加载的 qrl chunk。
- signal/store 在此模型下必须"可序列化"：`useSignal`/`useStore` 的值写入 DOM 属性与序列化块，客户端首次交互时直接恢复值，无需重跑组件函数。
- 依赖追踪的落点：Qwik 不做传统细粒度追踪，而是以"任务粒度"响应——`useTask$`（显式 track 数组）监视 signal 变化执行任务，组件渲染按需重跑。
- 配合方式：`useSignal` 的 `.value` 在服务端渲染时是快照，交互处理器（qrl）读取时从序列化状态恢复；更新某个 signal 只拉取对应的处理 chunk。
- 取舍：任务粒度比表达式粒度粗，但省掉水合成本，适合内容站/电商静态页；重交互应用则 Solid/Vue 更细。

```tsx
// Qwik：状态序列化 + 任务粒度响应
const Cmp = component$(() => {
  const count = useSignal(0);            // 序列化进 HTML
  useTask$(({ track }) => {
    track(() => count.value);            // 显式声明追踪目标
    console.log('count =', count.value);
  });
  return <button onClick$={() => count.value++}>{count.value}</button>;
});
// 点击时才下载 onClick$ 的 chunk；count 值从 DOM 快照恢复，无水合
```
