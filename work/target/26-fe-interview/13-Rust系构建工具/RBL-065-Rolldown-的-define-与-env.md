---
title: [RBL-065] Rolldown 的 define/env 注入如何配置？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-065：Rolldown 的 define/env 注入如何配置？
**答**：
- 顶层 define 选项：对象键为表达式（process.env.NODE_ENV、import.meta.env.X），值为 JSON 字面量字符串，构建期静态替换，语义同 esbuild 的 define。
- 与 vite 的关系：rolldown-vite 场景下 vite 层仍负责 .env 文件加载与 import.meta.env 体系，rolldown 只做替换执行。
- 注意事项：值必须是字符串形式的 JS 字面量（JSON.stringify 后传入）；只替换"标识符路径"表达式（成员访问全匹配），不解析任意代码。
- tree shaking 联动：define 注入 `process.env.NODE_ENV` 为 'production' 后，`if (process.env.NODE_ENV !== 'production')` 分支被摇树/压缩判定为死代码——依赖注入先于摇树的执行顺序。
- 常见坑：define 了 `process.env.NODE_ENV` 但某依赖用 `typeof process`，仍需 external 声明或注入 `process` 全局。
- 追问钩子：运行时配置（构建后可改）应走 window.__CONFIG__ 注入或远程配置接口，不要全塞 define。

```javascript
// rolldown.config.js
export default {
  input: 'src/index.ts',
  define: {
    'process.env.NODE_ENV': JSON.stringify('production'),
    '__BUILD_ID__': JSON.stringify('2026.11.18'),
    'import.meta.env.DEV': 'false',
  },
  output: { format: 'esm' },
};
// 产物：if ('production' !== 'production') {...} → 被压缩器整块删除
```
