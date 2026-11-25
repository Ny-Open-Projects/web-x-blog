---
title: [BLD-018] 写一个把 markdown 编译成 Vue 组件 / JS 模块的 loader。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-018：写一个把 markdown 编译成 Vue 组件 / JS 模块的 loader。
**答**：
- 思路：loader 输入是 md 文本，用 markdown-it 解析为 HTML，再包装成 Vue SFC 字符串（template 包 HTML，可加 options 区）或纯 JS（导出 html 字符串）。
- 注意 escaped 内容与 JSON 安全（HTML 里含换行要处理），vue loader 需要拿到合法 SFC。
- this.resourcePath 可用于提取文件名生成组件名；可加 this.cacheable() 声明可缓存。

```javascript
// markdown-loader.js
const markdownIt = require('markdown-it');
const md = markdownIt({ html: true, breaks: true });

module.exports = function (source) {
  this.cacheable(); // 输出只依赖输入 可缓存

  const html = md.render(source);
  const componentName = this.resourcePath
    .split(/[\\/]/).pop()          // 取文件名
    .replace(/\.md$/, '')
    .replace(/(^|-)(\w)/g, (_, __, c) => c.toUpperCase());

  // 输出合法 Vue SFC 交给 vue-loader 继续处理
  const sfc = `
<template>
  <article class="markdown-body">${html}</article>
</template>

<script>
export default { name: '${componentName}' };
</script>

<style>
.markdown-body { line-height: 1.7; }
</style>
`;
  return sfc;
};

// webpack.config.js
// module.exports = { module: { rules: [
//   { test: /\.md$/, use: ['vue-loader', './markdown-loader'] }, // 从后往前 先 md 后 vue
// ] } };
```
