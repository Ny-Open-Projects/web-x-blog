---
title: [RBL-110] bun build 的打包能力与 esbuild 相比如何？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-110：bun build 的打包能力与 esbuild 相比如何？
**答**：
- 能力面：bundle/minify/splitting/sourcemap/target（browser/node/bun）/loader（ts/jsx/json/css 基础支持）——与 esbuild 的 API 面高度相似，速度同量级（部分场景更快）。
- 差异点：bun build 内置 TS/JSX 转译且零配置；css 处理更早期（复杂 CSS 管线不如 esbuild 成熟）；插件 API 较新（onLoad/onResolve 风格类似 esbuild）。
- 应用场景：服务端/CLI/边缘函数打包（bun target）最顺；完整前端应用构建管线（HTML 注入、复杂 chunk 策略）仍建议 Vite/Rspack。
- --compile 特性：打包为独立二进制（嵌运行时），部署不需要安装 runtime，这是 esbuild 没有的。
- 迁移注意：esbuild 插件生态丰富，bun build 的插件需要小改；define/env 注入语义对齐。
- 追问钩子：bun build 的定位是"bun 生态内闭环"，不是要替代完整前端构建器——一体化优势场景是服务端/工具链。

```bash
# 前端 bundle
bun build ./src/index.ts \
  --outdir dist --target browser --minify --splitting --format esm

# 服务端 + 编译独立二进制（部署免 runtime）
bun build --compile ./server.ts --outfile myserver

# 插件
# Bun.plugin({ setup(build) {
#   build.onLoad({ filter: /\.svg$/ }, (args) => ({ contents: `export default ${JSON.stringify(args.path)}`, loader: 'js' }));
# }})
```
