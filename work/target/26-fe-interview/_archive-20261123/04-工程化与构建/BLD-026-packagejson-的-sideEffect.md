---
title: [BLD-026] package.json 的 sideEffects 字段全解？CSS 副作用的坑是什么？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-026：package.json 的 sideEffects 字段全解？CSS 副作用的坑是什么？
**答**：
- sideEffects: false：声明所有文件都无副作用，未被使用的模块可整体删除（哪怕有顶层执行代码）；这是"性能上最激进"的承诺。
- sideEffects: true 或缺省：保守策略，所有模块都可能被保留（默认行为）。
- sideEffects 数组：精确豁免，如 `["*.css", "**/polyfill.js"]`，数组成员支持 glob；未匹配的文件视为无副作用。
- CSS 坑：`import './style.css'` 从 JS 角度"未使用任何导出"，若 sideEffects: false 没豁免 css，样式会被直接 shake 掉——这是组件库样式丢失的最常见原因。
- 数组里匹配的是"路径字符串"，写法要与模块路径匹配（通常 `**/*.css` 才能覆盖子目录）。

```json
// package.json（组件库）: sideEffects 精确声明
{
  "name": "my-ui-lib",
  "sideEffects": [
    "**/*.css",
    "**/*.scss",
    "./src/polyfill.js",
    "./src/register-components.js"
  ]
}
```

```javascript
// webpack.config.js：sideEffects 需要生产模式且依赖包的 exports/module 字段
module.exports = {
  mode: 'production',
  optimization: { sideEffects: true, usedExports: true },
  resolve: {
    mainFields: ['module', 'main'], // 优先 ESM 入口 才能参与 shaking
  },
};

// 误配后果示例：
// { "sideEffects": false } 且组件库入口 import './index.css'
// -> 使用方 import { Button } from 'my-ui-lib' 时样式被 shake
// 修复：数组中加 "**/*.css"
```
