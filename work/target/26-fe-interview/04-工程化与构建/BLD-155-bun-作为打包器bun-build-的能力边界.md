---
title: [BLD-155] bun 作为打包器：bun build 的能力边界与适用场景。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-155：bun 作为打包器：bun build 的能力边界与适用场景。
**答**：
- `bun build`（Zig 实现）：esbuild 级别的速度，内置 loader（ts/tsx/jsx、css、文本、WASM? 部分）、原生支持 **宏? 否**——亮点是与 bun 运行时一体：`bun build --target=bun` 出单文件可执行脚本、`--compile` 直接产自包含二进制。
- 边界：插件 API 较新且有限（Bun.plugin 的 onLoad/onResolve）、无 rollup 级产物控制、生态适配（postcss 之外的自定义转换）弱；浏览器产物可用但成熟度低于 esbuild/rollup。
- 典型场景：CLI/服务端工具打包（`bun build --compile server.ts --outfile srv`）、bun 项目内部 bundle、CI 里脚本预打包提速；企业前端产物主链路仍建议 vite/webpack。
- 面试定位：bun 是"运行时优先"的工具集，打包能力是运行时生态的配套，而非主战场。

```bash
# bun build 关键用法
bun build ./src/index.ts --outdir ./dist --target=browser --minify --sourcemap  # 浏览器 bundle
bun build ./src/cli.ts --compile --outfile mytool                               # 单文件可执行（含运行时）
bun build --target=bun ./server.ts --outfile server.bundle.js                   # bun 运行时单文件（无依赖安装部署）

# bunfig.toml：插件（有限能力）
# [serve.static]
# plugins = "./plugins.ts"
```

```javascript
// plugins.ts：bun 的 onLoad/onResolve（与 esbuild 形似但生态独立）
Bun.plugin({
  name: 'yaml-loader',
  setup(build) {
    build.onLoad({ filter: /\.yaml$/ }, async (args) => {
      const text = await Bun.file(args.path).text();
      const js = `export default ${JSON.stringify(require('js-yaml').load(text))};`;
      return { contents: js, loader: 'js' };
    });
  },
});
// 适合：给 bun 跑的脚本/边缘函数做构建；不适合替代主站 vite/webpack 产物链路
```

## 追问（补充）

**追问**：

1. bun build 能替代 webpack 吗？ → 做库和结构简单的应用可以，内置 TS/JSX 且打包极快；但 loader 生态、复杂拆包策略与成熟 HMR 仍不如 webpack 与 vite，业务工程不建议直接换。
2. 什么场景值得上 bun？ → CLI、脚本、Node 服务与产物简单的库，收益主要来自进程启动与依赖安装速度，构建复杂度和生态依赖都不高时风险最小。
3. 迁移风险在哪？ → Node API 兼容度、`.node` 原生模块加载、postinstall 脚本行为差异，以及默认 target 不同导致的产物语法级别不一致。
