---
title: [WCN-109] WCN 在 Svelte / Solid 宿主中如何使用？事件与 prop 绑定有什么差异？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 跨框架复用]
type: 面试题
---

## WCN-109：WCN 在 Svelte / Solid 宿主中如何使用？事件与 prop 绑定有什么差异？

**答**：
- Svelte：`<x-dialog bind:this={el} on:dialog-close={fn}>`；props 走 attribute 字符串或 `bind:value`（Svelte 会 set property）；5 的 runes 里 `$state` 与 WC 事件联动靠回调写回。
- Solid：JSX 对自定义元素属性默认走 attribute——对象/函数要用前缀 `prop:`（`prop:data={obj}`）强制 property 传递；事件用 `on:xxx`（不自动 retarget）。
- 共同坑：宿主的响应式值传给 WC attribute 时会字符串化，对象必须走 property 通道；事件对象是 CustomEvent 不是框架合成事件。
- 双向绑定：Svelte `bind:value` 要求 WC 实现 value getter/setter 与 input/change 事件（WCN-027 的约定）；Solid 用受控事件 + 信号回写。
- 类型：两个框架都有 GlobalComponents/JSX 扩展机制，从 custom-elements.json 生成。

```svelte
<!-- Svelte -->
<script>
  let el; // bind:this
  let v = $state('');
</script>
<x-dialog bind:this={el} on:dialog-close={(e) => console.log(e.detail.action)}>
  <x-input bind:value={v} />
</x-dialog>
```

```jsx
// Solid：prop: 前缀强制 property 传递
<x-dialog on:dialog-close={(e) => console.log(e.detail.action)}>
  <x-input prop:value={v()} on:input={(e) => setV(e.detail.value)} />
</x-dialog>
```
