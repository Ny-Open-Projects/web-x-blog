---
title: [BLD-069] Rollup 的定位与优势是什么？为什么说它是"库打包首选"？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-069：Rollup 的定位与优势是什么？为什么说它是"库打包首选"？
**答**：
- 定位：面向 JS 库/组件库打包，输出干净的 ESM/CJS/UMD 产物；webpack 面向应用（code splitting、loader 生态、HMR），Rollup 面向"最终产物质量"。
- 优势：基于 ESM 静态图的极致 tree-shaking（比 webpack 更激进）、作用域提升默认开启、产物几乎无运行时代码（没有 webpack 的 __webpack_require__ 噪音）、配置简单。
- 生态位：Vite 生产构建底座、多数 npm 包（vue、react 相关工具链）的构建器。
- 取舍：应用级 code splitting 与 HMR 弱于 webpack，复杂资源处理靠插件堆叠；所以"库用 Rollup，应用用 webpack/Vite"。

```javascript
// rollup.config.js：库打包典型配置
import resolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import babel from '@rollup/plugin-babel';

export default {
  input: 'src/index.js',
  output: [
    { file: 'dist/index.mjs', format: 'esm', sourcemap: true },         // 给 bundler 用的现代入口
    { file: 'dist/index.cjs', format: 'cjs', exports: 'auto' },         // Node CJS
    { file: 'dist/index.umd.js', format: 'umd', name: 'MyLib',          // CDN/script 标签
      globals: { react: 'React' }, sourcemap: true },
  ],
  external: ['react', 'react-dom'],       // peer 依赖必须 external 不打进包
  plugins: [
    resolve(),                            // 解析 node_modules
    commonjs(),                           // CJS 转 ESM 参与 shaking
    babel({ babelHelpers: 'bundled', exclude: 'node_modules/**' }),
  ],
};

// package.json 配套字段（text 代码块）：
// "main": "dist/index.cjs", "module": "dist/index.mjs",
// "exports": { ".": { "import": "./dist/index.mjs", "require": "./dist/index.cjs" } },
// "peerDependencies": { "react": ">=17" }
```

**追问**：

1. 为什么 React 必须写进 `external`？→ 打进来会导致应用里存在两份 React，hooks 立刻报 "Invalid hook call"；同时要在 `peerDependencies` 里声明版本范围，交给使用方安装。
2. Rollup 的 tree-shaking 什么时候会失效？→ 模块有顶层副作用（立即执行的调用、装饰器、CJS 动态 require）或 package.json 没标 `sideEffects: false`，需要 `/*#__PURE__*/` 显式标注。
3. 同时产出 ESM 和 CJS 时 `exports` 怎么写？→ 用条件导出分别指向 `import`/`require`，并单独给 `types`；要注意 dual package hazard——同一包被两条路径加载会出现两份实例和两份单例状态。
