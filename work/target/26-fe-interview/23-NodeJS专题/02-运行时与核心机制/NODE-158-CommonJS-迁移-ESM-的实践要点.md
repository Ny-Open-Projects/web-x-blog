---
title: [NODE-158] CommonJS 迁移 ESM 的实践要点？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-158：CommonJS 迁移 ESM 的实践要点？
**答**：
- 第一步：`package.json` 加 `"type": "module"`；CJS 互操作用 `createRequire` 兼容旧依赖。
- 语法迁移四件套：import/export 替代 require、相对导入**必须带扩展名**（`./routes.js`）、`__dirname/__filename` 用 `import.meta.url` 重建、动态 `require()` 改 `await import()`。
- 收益：真静态分析（打包/树摇）、顶层 await（初始化连接）、与浏览器生态语法统一。
- 库发布注意：`exports` 字段声明双格式或纯 ESM，消费方 Node 版本有下限要求（纯 ESM 需要 ≥12.20）。

```javascript
// ESM 迁移核心对照
import { fileURLToPath } from 'node:url';
import path from 'node:path';
import express from 'express';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url); // 兼容只支持 CJS 的旧依赖
const legacyDep = require('some-cjs-only-pkg');

const __filename = fileURLToPath(import.meta.url); // CJS 全局变量替代
const __dirname = path.dirname(__filename);

// 相对导入必须带扩展名：import './routes' 报错 → import './routes.js'
const app = express();
export default app;

// 顶层 await：初始化连接不再需要 async main 包裹
await prisma.$connect();
app.listen(env.PORT);
```

---

## 二十、综合与体系
