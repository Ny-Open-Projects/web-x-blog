---
title: [CSS-226] 容器查询 style()：样式查询是什么
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 容器查询]
type: 面试题
---

## CSS-226：容器查询 style()：样式查询是什么

**答**：
- @container style()：按「容器的自定义属性值」而非尺寸做分支——同一组件在不同主题/模式下切换样式
- 语法：`@container style(--theme: dark) { … }`；父容器设置 `--theme: dark` 即触发
- 与 size() 查询并存：一个 @container 里可混合；style 查询暂不支持 :has 等复杂条件（只能单属性等值比较）
- 价值：主题化组件的「上下文自适应」——同个卡片放进深色区块自动换配色，不用 JS 传 props
- 兼容：Chromium/Safari 支持，Firefox 部分跟进；生产建议配默认样式兜底

```css
.sidebar { container-type: inline-size; --theme: dark; }
.card {
  background: white; color: #333; /* 默认 */
}
@container style(--theme: dark) {
  .card { background: #1e1e1e; color: #eee; }
}
```
