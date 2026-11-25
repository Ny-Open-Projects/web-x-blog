---
title: [WCN-126] Svelte 4 的编译时 invalidate 机制是什么？它与运行时追踪（Svelte 5）的差异？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 编译器方向]
type: 面试题
---

## WCN-126：Svelte 4 的编译时 invalidate 机制是什么？它与运行时追踪的差异？

**答**：
- Svelte 4 原理：编译器静态扫描组件内"哪些变量被模板读取、哪些赋值发生"，给每个响应变量分配 bitmask；赋值语句被改写为 `$$invalidate(i, x = v)`，模板插值改为 `$$dirty & mask ? expr : cached`。
- 特点：依赖在编译期完全确定（赋值点即触发点），无运行时追踪开销；但依赖静态——深层对象修改（`obj.a.b = 1`）不自动触发，需显式重新赋值 `obj = obj`。
- Svelte 5（运行时追踪）：`$state` 信号内核动态收集依赖，深层 proxy 自动响应、`$derived` 惰性；编译期只负责语法转换与 DOM 更新块生成。
- 迁移动因：Svelte 4 模型在跨组件共享状态、异步派生上表达力不足；位图数量有上限，大型组件退化为全量 dirty。
- 面试要点：能对比"赋值即触发"与"读取即追踪"两种心智的边界差异（隐式全等比较、作用域限制在组件内）。

```svelte
<!-- Svelte 4 源码 -->
<script>
  let name = 'a';
  let obj = { deep: { v: 1 } };
  function fix() { obj = obj; }  // 深层修改需手动触发
</script>
<span>{name}</span>
```

```javascript
// Svelte 4 编译产物（示意）
$$invalidate(0, (name = 'a'));                 // mask bit0
$set_text(span, ($$dirty & 1) ? name : cached); // 编译期静态依赖
// 对比 Svelte 5：obj.deep.v = 1 直接触发（proxy + 信号），无需 obj = obj
```
