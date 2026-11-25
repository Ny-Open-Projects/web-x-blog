---
title: [NODE-008] Node 的全局对象有哪些？globalThis 解决了什么问题？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-008：Node 的全局对象有哪些？globalThis 解决了什么问题？
**答**：
- Node 特有全局：`process`、`Buffer`、`global`、`setImmediate`/`clearImmediate`、`__dirname`/`__filename`（CJS）；浏览器特有：`window`、`document`、`navigator`。
- `globalThis` 是 ES2020 标准，**跨环境统一**的全局对象：Node 中等于 `global`，浏览器中等于 `window`/`self`，Worker 与 Node 工具链通用——isomorphic 代码不再需要 `typeof window !== 'undefined'` 这类嗅探。
- 注意：ESM 中 `__dirname` 不存在、顶层 `this` 是 `undefined`（CJS 中是 `exports`）；`process.env` 是对象但值全为字符串，空串会被判定 falsy，配置解析要小心。

```javascript
// 跨环境单例：利用 globalThis 防止重复初始化（BFF SDK 常见模式）
function getTracer() {
  if (!globalThis.__app_tracer__) {
    globalThis.__app_tracer__ = {
      createdAt: Date.now(),
      spanId: Math.random().toString(36).slice(2),
    };
    console.log('tracer 初始化一次');
  }
  return globalThis.__app_tracer__;
}
console.log(getTracer() === getTracer()); // true

// 环境判断的正确姿势
const isNode = typeof process !== 'undefined' && process.versions?.node;
const isBrowser = typeof window !== 'undefined' && typeof document !== 'undefined';
console.log({ isNode: Boolean(isNode), isBrowser });

// process.env 坑：所有值都是字符串
process.env.PORT = '0';            // 期望"未配置走默认 3000"
const port = Number(process.env.PORT) || 3000; // 必须显式转数字，否则 '0' 是 truthy
console.log(port);                 // 3000
```

---

## 二、Stream 与 Buffer
