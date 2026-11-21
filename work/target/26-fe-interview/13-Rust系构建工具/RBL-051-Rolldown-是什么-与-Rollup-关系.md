---
title: [RBL-051] Rolldown 是什么？与 Rollup 是什么关系？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-051：Rolldown 是什么？与 Rollup 是什么关系？
**答**：
- 一句话定位：Rolldown 是 Rollup 的 Rust 重写版，目标是"API 兼容 Rollup + 性能对标 esbuild"，由 Vite 团队推进，未来作为 Vite 的默认底层。
- 关系演进：Rollup 作者lukastaegtmeyer 参与 Rolldown 设计，Rollup 保持 JS 实现作为规范基准，Rolldown 吸收其语义；Vite 团队官方宣布 Rolldown 是"Rollup 的继任者"。
- 兼容策略：Rollup 的 output 选项（format/entryFileNames/globals）、插件钩子（resolveId/load/transform）、treeshake 配置语义对齐；但 Rolldown 额外内置 esbuild 级转换与压缩（不需要外部 minifier）。
- 差异点：Rolldown 不追求 100% 复刻 Rollup 的全部内部行为（如部分冷门警告），以"插件可用 + 产物语义一致"为验收线。
- 定位差异：Rollup 适合库打包（产物干净、无 runtime），Rolldown 同样强调库打包语义并延伸到应用场景（配合 Vite）。
- 追问钩子：为什么 Vite 要换内核？——dev 用 esbuild、prod 用 Rollup 的双内核导致 dev/prod 产物不一致，Rolldown 统一后消除这个问题。

```javascript
// rolldown.config.js：与 rollup.config.js 高度同构
import { defineConfig } from 'rolldown';
export default defineConfig({
  input: 'src/index.ts',
  output: [
    { format: 'esm', dir: 'dist/esm', entryFileNames: '[name].js' },
    { format: 'cjs', dir: 'dist/cjs' },
  ],
  plugins: [
    // resolveId / load / transform 钩子语义与 rollup 一致
    {
      name: 'my-plugin',
      transform(code, id) {
        if (id.endsWith('.svg')) return { code: `export default ${JSON.stringify(id)}` };
      },
    },
  ],
});
```
