---
title: [WCN-113] WCN 跨框架复用时样式策略怎么定？token 外置、preflight 冲突与 Tailwind 兼容如何处理？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 跨框架复用]
type: 面试题
---

## WCN-113：WCN 跨框架复用时样式策略怎么定？token 外置、preflight 冲突与 Tailwind 兼容如何处理？

**答**：
- 分层：组件自有样式（影子树内静态 CSS）+ 主题 token（外部 CSS 变量）+ 宿主 reset 不入侵（preflight/Tailwind base 不进影子树——这既是隔离的好处也是问题：按钮丢默认样式，组件要自带重置）。
- token 契约：`--wc-*` 前缀清单 + 默认值内置于组件（`var(--wc-btn-bg, #2563eb)`），宿主框架各自在其入口注入 token（React 用 CSS 文件、Vue 用 :root 样式）。
- Tailwind 宿主：宿主的 utility class 无法直接作用影子树内部——要么组件暴露 `part` 让宿主用 `::part()` + Tailwind arbitrary variant（`x-btn::part(btn){@apply ...}`）定制，要么组件内置 token 映射（如 `--wc-radius` 对齐宿主的 rounded 设计）。
- 字体/行高继承：preflight 不进入影子树导致继承差异，组件 `:host { font: inherit; line-height: inherit }` 显式对齐。
- 旧浏览器降级：无 Shadow DOM 支持的环境（极少）可构建"light DOM 输出 + CSS 前缀"产物（Lit 的 shadowless 模式思路）。

```css
/* 组件内（影子树） */
:host {
  font: inherit; line-height: inherit;      /* 对齐宿主 preflight 后的排版 */
  color: var(--wc-fg, var(--wc-fallback, #111));
}
button {
  all: unset;                                /* 自带重置，不依赖宿主 reset */
  background: var(--wc-btn-bg, #2563eb);
  border-radius: var(--wc-radius, 8px);
}
```

```css
/* 宿主（React/Vue 各自注入） */
:root { --wc-btn-bg: var(--ant-color-primary, #1677ff); --wc-radius: 6px; }
x-btn::part(icon) { width: 1em; }            /* ::part + Tailwind 生态共存 */
```
