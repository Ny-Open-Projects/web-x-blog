---
title: [SCN-1222] AI 对话的深色模式与代码主题适配
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1222：AI 对话的深色模式与代码主题适配

**答**：
- 适配：暗色模式下代码高亮主题同步切换（highlight.js 主题双套）、图片/图表适配。
- 无闪：切换无闪白（CSS 变量过渡），系统偏好跟随（prefers-color-scheme）。
- 图表：AI 生成图表（SVG/Canvas）暗色适配（颜色 token 化）。

```javascript
// 暗色适配
function themeAwareRender(html, theme) {
  return html
    .replace(/class="hljs"/g, `class="hljs hljs-${theme}"`)
    .replace(/--chart-color/g, theme === 'dark' ? '--chart-color-dark' : '--chart-color');
}
matchMedia('(prefers-color-scheme: dark)').addEventListener('change',
  e => rerenderAll(e.matches ? 'dark' : 'light'));
```
