---
title: [WCN-050] WC 在设计系统中的落地路径是什么？与 npm 组件包、Monorepo 联动怎么做？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-050：WC 在设计系统中的落地路径是什么？与 npm 组件包、Monorepo 联动怎么做？

**答**：
- 落地路径：token 层（CSS 变量字典）→ 基础组件（Button/Input，纯 WC）→ 组合组件（Table/Form，内部可复用框架实现再导出 WC 包装）→ 框架适配层（React/Vue 包装器按需生成）。
- Monorepo 结构：`tokens/`（design tokens 构建为 CSS 变量）、`core/`（WC 实现）、`adapters/`（react/vue 包装）、`docs/`（Storybook 用 WC 直接预览）。
- 分发策略：`@acme/wc-core`（自动 define 版）、`@acme/wc-elements`（仅类）、`@acme/react`（适配层）；语义化版本 + custom-elements.json changelog。
- 渐进迁移：新页面用 WC，存量页面在框架适配层复用同一 WC（React 19 原生支持 props 传递，Vue 用 defineCustomElement 双向桥）。
- 治理要点：视觉回归（Playwright 截图 shadow 内元素）、API 破坏性变更检查（manifest diff）、双版本共存窗口期（tag 加 v2 后缀）。

```json
// packages/wc-core/package.json
{ "name": "@acme/wc-core",
  "exports": {
    "./button": "./src/button.define.js",      // 自动注册
    "./elements/button": "./src/button.js",    // 仅类
    "./theme.css": "./dist/tokens.css" },
  "files": ["dist", "custom-elements.json"] }
```

```javascript
// adapters/react 自动生成示意
import { MyButton } from '@acme/wc-core/elements/button';
import { createComponent } from '@lit/react';
import * as React from 'react';
export const Button = createComponent({
  tagName: 'acme-button', elementClass: MyButton, react: React,
  events: { onAcmeClick: 'acme-click' },   // 事件映射为 props
});
```
