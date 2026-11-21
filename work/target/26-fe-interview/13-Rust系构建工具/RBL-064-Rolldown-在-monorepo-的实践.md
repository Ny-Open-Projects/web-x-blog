---
title: [RBL-064] Rolldown 在 monorepo 多包构建中的实践？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-064：Rolldown 在 monorepo 多包构建中的实践？
**答**：
- 场景：workspace 里几十个 npm 包，每包独立产出 ESM/CJS/dts——典型是组件库、工具库集合。
- 加速来源：每个包构建从秒级降到百毫秒级（oxc 解析 + 内置 commonjs/resolve），全仓构建（turbo 并行）总量级下降一个数量级。
- 统一配置：共享 rolldown.config base（如 packages/config），包级只声明 input/external；用 preserveModules 保持内部包产物结构以便增量调试。
- dts 并行：类型声明用 rolldown-plugin-dts 或独立 tsc 任务并行，不阻塞 js 打包。
- 缓存：rolldown 自身增量缓存尚在完善，monorepo 层面用 turbo/nx 任务缓存兜底（产物 + 声明文件进 outputs）。
- 追问钩子：多包构建的另一个方向是"one-shot 打包"（一个 entry 汇总所有包），rolldown 的 advancedChunks 可以按包分组，但会牺牲产物独立发版能力。

```javascript
// packages/config/rolldown.base.js
export const baseConfig = (pkg) => ({
  input: 'src/index.ts',
  external: Object.keys(pkg.peerDependencies || {}),
  output: [
    { format: 'esm', dir: 'dist/esm', preserveModules: true },
    { format: 'cjs', dir: 'dist/cjs' },
  ],
});
// 各包 rolldown.config.js
// import { baseConfig } from '../config/rolldown.base.js';
// export default baseConfig(require('./package.json'));
```
