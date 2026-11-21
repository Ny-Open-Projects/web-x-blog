---
title: [H5-111] 颜色对比度要求是什么？prefers-contrast 与forced-colors 如何适配？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-111：颜色对比度要求是什么？prefers-contrast 与forced-colors 如何适配？
**答**：
- WCAG AA 门槛：正文**至少 4.5:1**、大字号（≥18.66px 粗体或 ≥24px）3:1、UI 组件边界与图形 3:1；AAA 分别 7:1 与 4.5:1。
- 高频翻车点：占位符灰色对白底不足 4.5:1、disabled 虽然豁免但别拿它做常态、浅色主题里的次级文字 (#999) 压线失败。
- 媒体查询适配：`prefers-contrast: more` 用户要求更高对比——加深文字、加粗边框；`prefers-color-scheme` 深色主题下重算对比。
- `forced-colors: active`（Windows 高对比度模式）：浏览器强制用系统色替换颜色，代码职责变为**保住结构线索**——`forced-color-adjust: none` 谨慎使用，边框/焦点环别删。
- 验证工具：DevTools 颜色拾取器自带对比度读数与 AA/AAA 标记；axe 的 color-contrast 规则批量扫描。

```css
/* 1) 基础：达标对比的调色板（白底正文 #333 ≈ 12.6:1） */
:root {
  --text: #333;
  --text-secondary: #595959;    /* 7:1，稳过 AA */
  --placeholder: #6e6e6e;       /* ≥4.5:1，替代常见的 #999 */
  --border: #767676;            /* UI 组件 3:1 门槛 */
}

/* 2) 用户系统级要求更高对比时 */
@media (prefers-contrast: more) {
  :root { --text: #000; --text-secondary: #1a1a1a; --border: #000; }
  .card { border-width: 2px; }
  a { text-decoration: underline; }        /* 对比之外再加非颜色线索 */
}

/* 3) 深色主题下重算，别只反转颜色 */
@media (prefers-color-scheme: dark) {
  :root { --text: #e8e8e8; --text-secondary: #b3b3b3; }
}

/* 4) Windows 高对比度模式：保结构，放行系统配色 */
@media (forced-colors: active) {
  .btn { border: 1px solid ButtonText; }   /* 用系统色变量保住按钮轮廓 */
  :focus-visible { outline: 3px solid Highlight; }
  .chart-bar { forced-color-adjust: none; } /* 仅图表保自有配色 */
}
```

```html
<!-- 落地自检：占位符与禁用态的对比处理 -->
<input placeholder="请输入手机号" style="color: var(--text);">
<style>
  ::placeholder { color: var(--placeholder); opacity: 1; } /* opacity 别再打折 */
  button:disabled { color: var(--text-secondary); }        /* 豁免但别过淡 */
</style>
```

## 二十、综合与现代 API
