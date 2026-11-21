---
title: [RBL-055] Rolldown 的插件系统与 Rollup 插件如何兼容？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-055：Rolldown 的插件系统与 Rollup 插件如何兼容？
**答**：
- 钩子兼容面：resolveId、load、transform、buildStart、buildEnd、generateBundle、renderChunk、writeBundle 等主流钩子语义对齐，大多数纯 JS 的 Rollup 插件可直接跑在 rolldown 上。
- 兼容层机制：rolldown 提供 JS 插件运行时，钩子回调在 Node 侧执行（与 Rspack 类似的 FFI 边界），核心逻辑留在 Rust；性能上"少 JS 插件更快"的规律同样成立。
- 原生插件：rolldown 把高频插件 Rust 化内置（@rolldown/pluginutils、rolldown 的 experimental 原生插件，如 node-resolve、commonjs、json），替代 rollup 的 @rollup/plugin-*。
- 差异点：rollup 插件里操作 bundle 内部结构的深度钩子（augmentChunkHash 的部分用法、Banner/Footer 的极端组合）可能行为不一致；rollup-plugin-* 生态里依赖 acorn AST 的转换插件要用 rolldown 的 AST 桥接或改写。
- 实战建议：优先用官方原生插件 + 少量 rollup 插件兜底；自研插件保持纯 transform（只动 code/id），兼容性最好。
- 追问钩子：rolldown 同时提供 vite-plugin 兼容桥（rolldown-vite 里 vite 插件直接可用）。

```javascript
// rolldown.config.js：原生插件 + rollup 插件混用
import native from 'rolldown/experimental';
import commonjs from '@rollup/plugin-commonjs'; // 兼容层运行

export default {
  input: 'src/index.ts',
  plugins: [
    native.nodeResolve(),   // Rust 内置，替代 @rollup/plugin-node-resolve
    commonjs(),             // JS 插件走兼容层
    { name: 'banner', generateBundle(_, bundle) {
        for (const file of Object.values(bundle)) file.code = '/* MIT */\n' + file.code;
      } },
  ],
};
```
