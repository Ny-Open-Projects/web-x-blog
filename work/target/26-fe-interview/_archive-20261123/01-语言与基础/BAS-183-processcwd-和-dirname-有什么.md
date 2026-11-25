---
title: [BAS-183] process.cwd 和 __dirname 有什么区别？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-183：process.cwd 和 __dirname 有什么区别？
**答**：
- process.cwd()：进程的当前工作目录，取决于你在哪里执行 node 命令，运行中可变。
- __dirname：当前模块文件所在目录的绝对路径，永远相对文件本身（CommonJS）。
- ESM 里没有 __dirname，用 `fileURLToPath(new URL('.', import.meta.url))` 等价替换。

```javascript
// 假设文件在 /app/scripts/run.js，你在 /app 下执行 node scripts/run.js
console.log(process.cwd());  // /app —— 随启动命令的位置变化
console.log(__dirname);      // /app/scripts —— 恒等于该文件所在目录
// ESM 等价写法
// import { fileURLToPath } from 'url';
// const __dirname = fileURLToPath(new URL('.', import.meta.url));
```
