---
title: [MP-358] 小程序的设计系统：主题 token 与暗色模式
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 面试题, 架构]
type: 面试题
---

## MP-358：小程序的设计系统：主题 token 与暗色模式

**答**：
- token 载体：CSS 变量（小程序 wxss 支持 var()）挂 page/:root 等价物（page 选择器）——data-theme 切换
- 暗色模式：darkmode: true（app.json）+ theme.json（导航栏/tabbar 的暗色配置）+ 页面层 data-theme——系统暗色跟随（wx.onThemeChange）
- token 管道：Figma tokens → 脚本生成 wxss 变量文件（与 Web 同源工具链）——双端设计一致性的工程保障
- 组件库适配：第三方组件库（WeUI/Vant Weapp）的主题变量覆盖——组件库 CSS 变量命名与自家 token 的映射层
- 深水点：图片/插画的暗色适配（小程序无 CSS filter 全能力——brightness 可用）——「暗色下的图片资产双套」或滤镜降亮度

```json
// app.json
{ "darkmode": true, "themeLocation": "theme.json" }
```

```css
/* theme.wxss (生成的 token) */
page { --bg: #fff; --fg: #222; }
@media (prefers-color-scheme: dark) { page { --bg: #121212; --fg: #eee; } }
/* 手动切换: page[data-theme=dark] { --bg: #121212; } */
.card { background: var(--bg); color: var(--fg); }
```
