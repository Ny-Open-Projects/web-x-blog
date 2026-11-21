---
title: [WCN-289] 去框架化设计系统的 token 管线（设计稿 → token → CSS 变量）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-289：去框架化设计系统的 token 管线（设计稿 → token → CSS 变量）？
**答**：
- 单一事实源：tokens.json（Figma 同步导出）→ 生成 CSS 自定义属性 + TS 类型（构建期）。
- 多主题：同一 token 集合 × 主题映射表 → 多套 CSS 变量文件（运行时类切换）。
- 版本化：token 变更 PR 可视 diff（颜色/间距），破坏性变更（删 token）走审批。
- 消费校验：lint 禁止组件写死颜色（必须 var(--ds-*)）。

```javascript
# token 管线
figma-tokens pull → tokens.json
style-dictionary build → tokens.css tokens.dark.css tokens.ts
lint: 禁止 #hex 出现在组件样式（CI）
r
```
