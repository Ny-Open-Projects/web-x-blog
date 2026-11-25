---
title: [WCN-165] WCN 支持多品牌/多租户主题的工程方案：一套组件服务多个品牌怎么做到？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 选型与工程落地]
type: 面试题
---

## WCN-165：WCN 支持多品牌/多租户主题的工程方案：一套组件服务多个品牌怎么做到？

**答**：
- 单实现多主题：组件只读 component token（`--acme-btn-bg`），品牌差异全部在 token 层——`<html data-brand="b">` 挂载对应品牌 token 集，级联天然生效，组件零改动。
- token 构建矩阵：Style Dictionary 按 brand × mode（light/dark）交叉产出 `tokens.brand-b.dark.css`；按需加载当前品牌+模式的两份文件。
- 品牌级结构差异：极端差异（布局/图标不同）用 slot/part 扩展点而不是分叉组件；确需分叉时在 core 里做策略注入（`config.partDecorators`）而非复制组件。
- 多租户 SaaS：租户 token 服务端下发（构建时按租户生成 CSS link），宿主 index.html 动态注入；缓存按租户+版本。
- 验证：视觉回归矩阵 = 组件 × 品牌 × 模式全组合截图；token 契约 lint（组件禁用裸色值）。

```css
/* tokens.brand-a.css */
:root, [data-brand="a"] { --acme-btn-bg: #2563eb; --acme-font: Inter; }
/* tokens.brand-b.css */
[data-brand="b"] { --acme-btn-bg: #dc2626; --acme-font: "Noto Sans SC"; }
/* dark 变体 */
[data-brand="b"][data-mode="dark"] { --acme-btn-bg: #ef4444; }
/* 组件（一份实现）内：background: var(--acme-btn-bg) */
```

```html
<html data-brand="b" data-mode="dark">
  <link rel="stylesheet" href="/tokens/brand-b.dark.css">
```
