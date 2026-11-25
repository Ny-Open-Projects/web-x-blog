---
title: [MP-144] 小程序的样式规范与设计 Token 怎么落地？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-144：小程序的样式规范与设计 Token 怎么落地？
**答**：
- Token 三层：**原始 Token**（色板/字号/间距原始值）→ **语义 Token**（`--color-bg-primary`、`--font-body`）→ **组件 Token**（组件内引用语义 Token）。
- 小程序侧用 CSS variables（页面根 view 挂载），暗色模式通过 `darkmode: true` + theme.json 或变量切换实现。
- Token 源文件由设计工具导出（JSON）→ 脚本生成 `tokens.wxss`，保证设计与代码同源。
- lint 检查禁止硬编码颜色/字号（stylelint 自定义规则），PR 门禁。

```css
/* styles/tokens.wxss —— 由设计导出 JSON 生成，勿手改 */
page {
  --color-brand-500: #07c160;
  --color-text-primary: rgba(0, 0, 0, 0.9);
  --color-bg-primary: #ffffff;
  --font-body: 28rpx;
  --radius-md: 12rpx;
  --space-4: 32rpx;
}
/* 暗色模式：theme.json 或根类切换 */
.theme-dark {
  --color-text-primary: rgba(255, 255, 255, 0.85);
  --color-bg-primary: #191919;
}
.btn {
  color: var(--color-text-primary);
  background: var(--color-brand-500);
  font-size: var(--font-body);
  border-radius: var(--radius-md);
  padding: var(--space-4);
}
```
