---
title: [WCN-155] WCN 与设计 Token 工具链如何联动？从 Figma 变量到 CSS 变量到组件的完整链路？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 选型与工程落地]
type: 面试题
---

## WCN-155：WCN 与设计 Token 工具链如何联动？

**答**：
- 链路：Figma Variables → 导出 JSON（W3C Design Tokens 格式）→ Style Dictionary 构建为多目标产物（CSS 变量文件 / TS 类型 / iOS/Android 可选）→ `tokens.css` 由宿主注入 :root → WC 组件经 `var(--acme-*)` 消费。
- 主题变体：tokens 按 light/dark/brand 生成多套变量集，主题切换 = 切换挂载的 class/data-theme（CSS 级联自然生效，组件零感知）。
- 契约分层：global（色板/字号）→ alias（语义：primary/success）→ component（`--acme-btn-bg`）；组件只允许引用 component 层，禁止跳层用 global（lint 规则扫描影子树 CSS）。
- 同步自动化：CI 定时或 Webhook 触发 token 构建，PR 展示 token diff；组件的默认值回退与 token 清单对齐（缺 token 时构建告警）。
- 版本化：tokens 独立发包（@acme/tokens），语义化版本；组件 peerDependencies 声明兼容范围。

```json
// tokens.json（W3C 格式节选）
{ "color": { "bg": { "value": "#ffffff", "type": "color" },
  "primary": { "value": "{color.brand.500}", "type": "color" } } }
```

```css
/* Style Dictionary 产物 → 宿主注入 */
:root { --acme-color-bg: #ffffff; --acme-color-primary: #2563eb; }
[data-theme="dark"] { --acme-color-bg: #0f172a; --acme-color-primary: #60a5fa; }
/* WC 内部：background: var(--acme-btn-bg, var(--acme-color-primary)); */
```
