---
title: [WCN-707] 组件库要支持按需加载，导出设计怎样才对 tree-shaking 友好？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-707：组件库要支持按需加载，导出设计怎样才对 tree-shaking 友好？

**答**：
- 结论：采用 ESM + 具名导出 + `sideEffects:false` 声明；避免顶层副作用（如立即注册所有自定义元素），把注册拆成显式的 `registerXxx()` 由调用方触发。
- 每个组件独立文件、独立入口（subpath exports），消费者 `import { Button } from '@ds/button'` 只打包用到的；CSS 也按组件拆分。
- 追问钩子：为什么 `export * from './index'` 的桶文件有时会破坏 tree-shaking？考察对 barrel file 与副作用传播的理解。

```javascript
// package.json
{
  "sideEffects": ["**/*.css"],
  "exports": {
    "./button": "./dist/button.js",
    "./table": "./dist/table.js"
  }
}
// dist/button.js —— 具名导出，无顶层注册副作用
export class DsButton extends HTMLElement {}
export function registerButton() {
  if (!customElements.get('ds-button')) customElements.define('ds-button', DsButton);
}
// 消费者：只引入 button，table 不会进包
import { registerButton } from '@ds/button';
registerButton();
```
