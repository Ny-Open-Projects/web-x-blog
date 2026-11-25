---
title: [RBL-519] Rolldown 的 Rollup 兼容语义清单：哪些语义是硬底线
date: 2026-11-21
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-519：Rolldown 的 Rollup 兼容语义清单：哪些语义是硬底线

**答**:
- Rolldown 要接管 Vite 的 build，就必须对齐 Rollup 的语义契约——硬底线清单：
- 1) **Tree-shaking 精度**：ESM 静态分析的按导出摇树（含副作用标注 /* @__PURE__ */、sideEffects 字段语义）——精度不足会造成「摇掉有用代码」（正确性事故）或「摇不掉死代码」（体积事故）。
- 2) **输出分块算法**：manualChunks 语义 + 动态 import 分割点 + 循环依赖的分块归属——chunk 边界影响缓存与加载行为。
- 3) **插件协议**：Rollup 插件钩子（transform/resolveId/generateBundle 等）的调用时机与参数语义——Vite 插件建立在 Rollup 钩子上。
- 4) **模块执行顺序**：ESM 导入提升语义下的模块初始化顺序（含循环引用的 TDZ 行为）——运行时正确性底线。
- 软兼容（可差异化）：非核心选项的默认值、日志格式、内部优化（如并行）——差异化空间在「更快」不在「不同」。
- 追问钩子：Tree-shaking 的语义争议点——`sideEffects: false` 的包级标注被滥用（误标导致摇掉副作用代码）是生态级正确性问题——Rolldown 对错误标注的防御（保守回退）是质量细节。

```javascript
// Rolldown 的 Rollup 兼容语义清单
const ROLLDOWN_COMPAT = {
  硬底线: {
    treeShaking: 'ESM 静态分析按导出摇树（@__PURE__ 注解 + sideEffects 语义）——精度不足=正确性/体积事故',
    chunking: 'manualChunks 语义 + 动态 import 分割点 + 循环依赖归属',
    plugin: 'Rollup 钩子（transform/resolveId/generateBundle）调用时机与参数语义——Vite 插件的地基',
    执行顺序: 'ESM 导入提升 + 循环引用 TDZ 行为——运行时正确性底线',
  },
  软兼容: '非核心默认值/日志格式/内部优化——差异化空间在「更快」不在「不同」',
  争议点: 'sideEffects:false 包级标注滥用 → 误摇副作用代码（生态级正确性问题）——Rolldown 保守回退防御',
}
```
