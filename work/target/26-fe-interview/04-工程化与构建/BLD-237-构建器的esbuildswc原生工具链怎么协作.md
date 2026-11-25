---
title: [BLD-237] esbuild/swc 原生工具链怎么协作？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-237：原生工具链协作怎么运作？
**答**：
- 分工矩阵：esbuild（JS/TS 转换+打包+压缩——dev 预构建/生产 minify）、swc（JS/TS 转换——babel 替代）、rollup/webpack（最终产物编排——插件生态）——vite = esbuild 转换 + rollup 产物。
- 协作点：esbuild 转换的产物喂给 rollup（转换快、编排稳）；压缩阶段 esbuild minify 替代 terser（SCN-BLD-213 权衡）。
- 原生工具的能力边界：esbuild 插件 API 简陋（复杂转换仍需 babel/postcss）；swc 的转译与 babel plugin 生态差距。
- 版本与一致：原生工具链版本 pin（esbuild 版本影响产物——cache 键入版本）。
- 追问钩子：为什么 vite 要「esbuild 转 + rollup 编」而不是全 esbuild 打包——dev 需要极速转换（esbuild）；prod 需要成熟产物编排（代码分割/摇树/插件生态——rollup）；esbuild 的 splitting 尚不能覆盖 rollup 的产物能力——这是「转换速度」与「产物质量」的分工，不是工具偏好。

```javascript
// vite 的分工
dev:  esbuild transform (毫秒级) + 原生 ESM 服务
prod: esbuild transform → rollup bundle → esbuild minify
// swc 替代 babel
{
  loader: 'swc-loader',                              // 快 20×
  options: { jsc: { parser: { syntax: 'typescript' }, target: 'es2019' } }
}
```
