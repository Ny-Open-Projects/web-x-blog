---
title: [WCN-124] Svelte 5 的 runes 编译产物长什么样？编译时响应式与运行时追踪如何结合？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 编译器方向]
type: 面试题
---

## WCN-124：Svelte 5 的 runes 编译产物长什么样？

**答**：
- 编译器把 `let count = $state(0)` 转成对内部 `$.signal` 的读写调用：读 → `$.get(count)`，写 → `$.set(count, v)`；赋值语句被改写。
- `$derived` 转成惰性 computed 节点（`$.derived(() => count * 2)`），`$effect` 转成带清理的 root effect；依赖追踪仍在运行时发生，但代码形态完全隐形。
- 模板编译：每个含响应式读取的插值生成 `$.set_text(node, () => expr)` 的更新块；事件用 `$.event delegated` 委托。
- 与 Svelte 4 的差异：Svelte 4 是"赋值触发 invalidate"（编译期静态依赖，`:invalidated` 位图），Svelte 5 换成真正的信号内核——跨组件（.svelte.js 共享状态）与更细的派生语义。
- 产物特征：无虚拟 DOM、无 React 那样的运行时调度器，包体 ~几 KB。

```svelte
<!-- 源码 -->
<script>
  let count = $state(0);
  let double = $derived(count * 2);
</script>
<span>{double}</span>
```

```javascript
// 编译产物（示意，Svelte 5 内部 API 命名简化）
let count = $.signal(0);
let double = $.derived(() => $.get(count) * 2);
const span = $.template('<span> </span>');
$.set_text(span, () => $.get(double));
$.set(count, $.get(count) + 1);   // count++ 的改写
```
