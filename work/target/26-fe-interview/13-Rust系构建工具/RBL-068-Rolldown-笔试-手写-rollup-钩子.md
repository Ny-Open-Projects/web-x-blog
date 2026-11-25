---
title: [RBL-068] 笔试：手写一个 Rollup/Rolldown 风格的虚拟模块插件
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-068：笔试：手写一个 Rollup/Rolldown 风格的虚拟模块插件
**答**：实现 virtualModulePlugin({ name, content })：1) resolveId 返回带 \0 前缀的虚拟 id（约定虚拟模块以 \0 开头避免被其他插件处理）；2) load 命中该 id 返回内容；3) 支持函数式 content（入参 env）；4) 其他模块 import 该虚拟模块时正确解析；5) 解释 \0 前缀的作用。

```javascript
function virtualModulePlugin({ name, content }) {
  const VIRTUAL_ID = '\0' + name;
  return {
    name: 'virtual-module',
    resolveId(source) {
      if (source === name) return VIRTUAL_ID;  // 命中：返回虚拟 id 终止默认解析
      return null;                              // 未命中：交回默认 resolve
    },
    load(id) {
      if (id !== VIRTUAL_ID) return null;
      const value = typeof content === 'function' ? content(process.env) : content;
      return `export default ${JSON.stringify(value)};`;
    },
  };
}
module.exports = { virtualModulePlugin };

// 用法：import info from 'build-info'
// new virtualModulePlugin({ name: 'build-info', content: () => ({
//   version: require('./package.json').version,
//   time: Date.now(),
// }) })
```
**评分点**：
- resolveId 返回 null 与返回虚拟 id 的语义区分（null = 交给默认解析）。
- \0 前缀约定：让其他插件（transform 等）可判断并跳过虚拟模块，防止误处理。
- load 只处理命中的 id（返回 null 交回）。
- content 支持静态与函数两种形态。
- 能举例 vite 的 virtual:env / rollup 的 inject_helpers 实际应用。
