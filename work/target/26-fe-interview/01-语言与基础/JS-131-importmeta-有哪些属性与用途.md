---
title: [JS-131] import.meta 有哪些属性与用途？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-131：import.meta 有哪些属性与用途？

**答**：
- import.meta 是 ESM 专属的元数据对象，属性由宿主环境注入，CJS 中不可用。
- 通用属性 `url`：当前模块的绝对 URL，配合 `new URL(path, import.meta.url)` 可替代 __dirname。
- Node 专属：`import.meta.dirname / filename / resolve()`（20.11+）；打包器注入 `env`（Vite）、`webpackHot` 等。
- 判断入口模块：Deno/Bun 的 `import.meta.main`；浏览器没有对应能力，需要入口约定。

```javascript
// 1. url：模块绝对地址（浏览器与 Node 通用）
console.log(import.meta.url); // file:///path/to/mod.mjs 或 https://cdn/mod.mjs

// 2. 由 url 推导资源路径 —— 替代 __dirname / __filename
const here = new URL('.', import.meta.url).href;              // 所在目录
const sibling = new URL('./data.json', import.meta.url).href; // 同目录文件
// fetch(sibling) 在浏览器 Worker 场景非常常用

// 3. Node 专属（20.11+）
// import.meta.dirname   // '/path/to'（替代 path.dirname(fileURLToPath(...))）
// import.meta.filename  // 'mod.mjs'
// import.meta.resolve('./other.js') // 返回解析后的 URL 字符串

// 4. 打包器注入
// Vite：import.meta.env.MODE / .DEV / .PROD / 自定义 VITE_ 变量
// if (import.meta.env.PROD) initSentry();

// 5. 查看宿主给了什么
console.log(Object.keys(import.meta)); // 浏览器通常 ['url']
```
