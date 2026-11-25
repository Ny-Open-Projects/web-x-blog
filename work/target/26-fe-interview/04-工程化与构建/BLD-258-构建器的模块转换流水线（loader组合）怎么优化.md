---
title: [BLD-258] 模块转换流水线（loader 组合）怎么优化？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-258：转换流水线怎么优化？
**答**：
- 流水线成本：每模块经过的 loader 数 × 每 loader 处理时间——优化方向：减少经过的 loader（include 收窄）、减少重复转换（缓存）、换快 loader（swc/esbuild 替 babel）。
- include/exclude 的精确性：node_modules 里也有需要转换的（ESM 源码包）——exclude node_modules 一刀切会输出未编译语法（SCN-BLD-235 残留）；按需 include。
- loader 间的格式协商：一个 loader 输出的格式必须是下一个 loader 期望的输入（ts→js 才能进 minify）——中间格式的约定。
- 转换缓存的键：模块内容 + loader 配置 + loader 版本——漏了 loader 版本（升级 babel 后旧缓存）是脏缓存来源。
- 追问钩子：为什么「exclude node_modules」在 ESM 包时代失效——历史上 node_modules 是编译产物（可直接用）；现在越来越多包发布 ESM 源码语法（可选链/管道操作符）或需要按 browserslist 编译——exclude node_modules 会输出含现代语法的产物（低版本白屏）；正确姿势是按包的「发布形态」决定 include（SCN-BLD-235 产物扫描兜底）。

```javascript
{
  test: /\.[jt]sx?$/,
  include: [srcDir, /node_modules\/(esm-source-pkg)/],  // 精确 include
  use: [{ loader: 'swc-loader', options: { cacheDirectory: true,
    cacheIdentifier: swcVersion + presetVersion } }]   // 缓存键含版本
}
```
