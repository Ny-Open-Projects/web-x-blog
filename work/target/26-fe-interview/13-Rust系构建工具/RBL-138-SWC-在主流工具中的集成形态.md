---
title: [RBL-138] SWC 在 Next/Vite/Rspack 里的集成形态有什么不同
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-138：SWC 在 Next/Vite/Rspack 里的集成形态有什么不同

**答**：
- Next.js：深度定制嵌入——编译、压缩、react-refresh、字体优化全走内置 SWC fork，用户无法直接改 .swcrc；提供 next/babel 兼容层兜底自定义 Babel 插件（但会退回 JS 编译路径，变慢）。
- Rspack：内置 swc 编译内核（builtin:swc-loader，零 FFI 复制成本），js 层 swc-loader 是兜底；minify 也默认 SWC。配置在 rspack.config 的 module.rule 里写 jsc 结构。
- Vite：可选 swc 插件（vite-plugin-swc / @vitejs/plugin-react-swc）替代 Babel/esbuild transform，主要为了 React HMR 稳定与大型项目编译提速；dev 时 esbuild 已很快，收益集中在 HMR 重编译场景。
- 共同点：都是把 SWC 当"编译函数库"用，而不是 CLI 产品；差异在宿主对配置的暴露程度（Next 收敛、Rspack 灵活、Vite 折中）。
- 追问钩子：被宿主内置的 SWC 版本不可控（Next fork 尤甚），语法支持差异要查宿主版本，不是看 SWC 官方文档。

```javascript
// Vite + @vitejs/plugin-react-swc：一行换核
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react-swc';

export default defineConfig({
  plugins: [
    react({
      // 透传 swc 配置（subset）
      swcOptions: {
        jsc: { target: 'es2020', transform: { react: { runtime: 'automatic' } } },
      },
    }),
  ],
});
// 收益典型值：千文件级项目 dev 冷启动 transform 阶段从 ~8s 降到 ~2s
// 但注意：Vite 的依赖预构建仍走 esbuild，SWC 只接管源码 transform。
```
