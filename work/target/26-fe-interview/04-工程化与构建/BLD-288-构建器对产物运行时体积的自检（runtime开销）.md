---
title: [BLD-288] 产物运行时开销（runtime 体积占比）自检怎么做？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-288：runtime 开销自检怎么做？
**答**：
- runtime 构成：打包器的模块加载器/HMR/互操作代码/polyfill——非业务代码占比过高意味着工具开销挤占业务体积。
- 度量：runtime chunk 单独度量（SCN-BLD-219 runtimeChunk）+ polyfill 占比（core-js 体积）/互操作辅助代码（__interopRequireDefault 数量——ESM-CJS 边界过多的信号）。
- 治理：runtime 占比超阈值触发审查（换打包器？依赖 ESM 化？polyfill 重算）——runtime 是「工具的税」，要定期体检。
- 追问钩子：为什么「互操作辅助代码数量」是依赖健康度的信号——每个 CJS↔ESM 边界都生成 interop 辅助代码（__importDefault 等）；数量多说明依赖树里 CJS 包占比高（摇树差 + 双实例风险）——它把「依赖格式健康度」变成了可从产物直接计数的指标。

```javascript
// runtime 自检
const runtimeRatio = runtimeChunk.size / totalSize;
if (runtimeRatio > 0.05) alert('runtime 占比过高——审查打包器开销');
// interop 计数
const interops = bundle.match(/__interopRequireDefault/g).length;
if (interops > 500) warn('CJS 边界过多——依赖 ESM 化优先');
```
