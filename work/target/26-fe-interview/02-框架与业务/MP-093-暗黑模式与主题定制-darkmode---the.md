---
title: [MP-093] 暗黑模式与主题定制（darkmode / theme.json）怎么做？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-093：暗黑模式与主题定制（darkmode / theme.json）怎么做？
**答**：
- app.json 配 `"darkmode": true` + `"themeLocation": "theme.json"`，用 `@` 变量在导航栏/tabBar 配置中引用主题值。
- theme.json 定义 light/dark 两套变量；wxss 中用 `@media (prefers-color-scheme: dark)` 适配页面样式。
- 监听 `wx.onThemeChange` 处理动态主题；组件库主题走 CSS 变量覆盖。

```json
{
  "app.json": {
    "darkmode": true,
    "themeLocation": "theme.json",
    "navigationBarBackgroundColor": "@navBg",
    "navigationBarTextStyle": "@navTxt"
  },
  "theme.json": {
    "light": { "navBg": "#ffffff", "navTxt": "black" },
    "dark":  { "navBg": "#1f1f1f", "navTxt": "white" }
  }
}
```
