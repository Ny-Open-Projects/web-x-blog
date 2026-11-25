---
title: [CSS-263] ::selection 定制与限制
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 细节]
type: 面试题
---

## CSS-263：::selection 定制与限制

**答**：
- ::selection 自定义文本选中态的颜色（color/background/text-decoration）——品牌化细节
- 限制严格：只允许少数属性（color、background-color、text-shadow、text-decoration 等），改 padding/font 无效
- 窗口级 vs 元素级：全局 `::selection { … }` + 特定区块覆写（如代码块选中态用主题色）
- 无障碍注意：前景背景必须保证对比度；不要用选中色「隐藏文字」的 hack（背景同色）
- 派生：::target-text（链接跳转目标高亮，Chromium）与 ::highlight()（Highlight API 自定义高亮）

```css
::selection { background: #4285f4; color: #fff; }
pre::selection { background: #111; color: #0f0; } /* 代码块反色 */
```
