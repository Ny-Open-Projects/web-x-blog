---
title: [RBL-131] SWC 是什么？核心架构与工作原理是怎样的
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-131：SWC 是什么？核心架构与工作原理是怎样的

**答**：
- SWC（Speedy Web Compiler）是 Rust 写的 JS/TS 编译器，定位是 Babel 的平替：解析 → 转换 → 生成一条龙，官方基准比 Babel 快 20~70 倍。
- 架构分三层：`@swc/core`（JS API 入口）、Rust 核心（parser/transformer/minifier）、平台二进制 binding（N-API 分发各平台 prebuilt），用户 npm install 时只下载对应平台的 .node 文件。
- 单次调用内零跨语言开销：Rust 侧完成 parse→transform→codegen，JS 侧只拿字符串结果；不像 Babel 每个 plugin 都是 JS 回调反复进出 AST。
- 它是"库"不是"产品"：Rspack/Vite/Turbopack/Next 都把它当编译内核嵌入，而不是让用户直接跑 swc CLI。
- 追问钩子：SWC 快的代价是插件生态弱——插件要用 Rust/WASM 写，Babel 的 AST 插件体系不能直接搬。

```javascript
// 直接用 @swc/core 做一次 TSX 转换（等价于 Babel 的 preset-react + preset-typescript）
const { transform } = require('@swc/core');

const code = `
const Greet: React.FC<{ name: string }> = ({ name }) => <div>hi {name}</div>;
interface A { x: number }
`;

(async () => {
  const out = await transform(code, {
    filename: 'app.tsx',
    jsc: {
      parser: { syntax: 'typescript', tsx: true },
      target: 'es2020',
      transform: { react: { runtime: 'automatic' } }, // 引入 jsx-runtime，不注入 React
    },
    module: { type: 'es6' },
    isModule: true,
  });
  console.log(out.code); // 已去掉类型标注、JSX 变 import { jsx } from ...
})();
```
