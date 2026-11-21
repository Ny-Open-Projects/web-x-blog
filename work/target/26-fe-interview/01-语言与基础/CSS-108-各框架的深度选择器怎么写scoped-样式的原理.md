---
title: [CSS-108] 各框架的深度选择器怎么写？scoped 样式的原理是什么？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-108：各框架的深度选择器怎么写？scoped 样式的原理是什么？

**答**：
- Vue scoped 原理：给该组件每个元素加 `data-v-xxx` 属性，选择器编译为 `.foo[data-v-xxx]`，实现隔离。
- 穿透子组件：Vue 3 用 `:deep()`（旧版 `>>>` 与 `/deep/` 已废弃）；只想命中插槽内容用 `:slotted()`。
- CSS Modules 里用 `:global(.foo)` 逃逸哈希；原生 Shadow DOM 天然隔离，靠 ::part 穿透。
- 深度选择器是逃生舱：优先用 props/插槽/CSS 变量定制第三方组件，实在不行再 `:deep()`。
- 深度选择器会破坏隔离边界，团队应约定只允许覆盖第三方组件库。

```vue
<!-- Vue 3 SFC -->
<style scoped>
/* 本组件元素正常隔离 */
.title { color: var(--fg-primary); }

/* 穿透第三方组件内部：编译为 [data-v-x] .el-input__inner */
:deep(.el-input__inner) { height: 36px; }

/* 只作用于父组件传入的插槽内容 */
:slotted(.slot-item) { padding: 4px 8px; }

/* 全局一条（谨慎） */
:global(body) { overflow-x: hidden; }
</style>
```

```css
/* CSS Modules（React 生态）中的等价写法 */
.wrapper :global(.third-party-inner) { color: var(--brand); }
/* 编译后：.wrapper_hash .third-party-inner —— 内部类不哈希 */
```

## 十九、CSS 架构方法
