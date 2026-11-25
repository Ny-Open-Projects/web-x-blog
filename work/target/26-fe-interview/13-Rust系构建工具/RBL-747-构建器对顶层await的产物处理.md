---
title: [RBL-747] 顶层 await 的产物处理：格式限制、chunk 分割影响与降级策略
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-747：顶层 await 的产物处理：格式限制、chunk 分割影响与降级策略

**答**:
- 顶层 await（TLA）的产物约束：1) **只有 ESM 支持**（CJS/UMD/IIFE 无法表达模块级挂起——CJS 的 require 是同步的）——含 TLA 的模块被 external 到 CJS 环境或打包进 UMD 时必须报错诊断，而不是产出坏代码；2) TLA 模块会「传染」：import 它的所有模块都变成异步图——打包器要把 TLA 闭包放进独立 chunk 或确保 import 它的入口本身是 async 语义。
- chunk 分割的影响：TLA 模块不能与「同步必需的模块」同 chunk（会让整包变异步）——构建器处理：TLA 模块及其闭包强制拆分（类似 SCC 不可分割的补集约束「TLA 不可合并」）；产物加载器对 TLA chunk 的加载是 await import（天然兼容）。
- 降级策略：目标环境不支持 TLA（老 Safari）→ 构建器转换 TLA 为「async IIFE 包裹 + 导出 Promise」（语义近似但导出面变 Promise——需要改写使用方），或诊断建议动态 import。转换有语义边界（模块实例化时序变化），默认不自动转、提示处理。
- TLA 与 HMR：TLA 模块的热更新要重新 await 完整模块图——HMR 边界（RBL-600）在 TLA 模块上失效概率高（父模块 accept 后重新执行要等待 TLA 完成），构建器对含 TLA 的模块建议「自接受 + 显式 async 处理」。
- 追问钩子：为什么 TLA 在「库产物」里是反模式？——库的导出面变成 Promise 或强制使用者用 ESM+async，兼容面大幅收窄；库用惰性初始化（导出 init() 函数）替代 TLA——「库产物禁 TLA」是常见 lint 规则。

```javascript
// TLA 检测与 chunk 约束
function analyzeTLA(mod) {
  mod.hasTLA = /(^|\n)\s*await\s+/.test(mod.code) && mod.format === 'es';
  if (mod.hasTLA) {
    for (const parent of graph.importersOf(mod.id)) {
      if (parent.format !== 'es') 
        throw new Error(`TLA 模块 ${mod.id} 被 CJS/UMD 依赖——模块传染诊断`);
    }
    markIndivisibleAsync(mod.id);                        // TLA 闭包不与同步 chunk 合并
  }
}
// 降级转换（诊断提示形态）
// 源码: const config = await fetchConfig();
// 转换: let __config;
//       export const ready = fetchConfig().then(c => { __config = c; });
//       export const getConfig = () => { if (!__config) throw new Error('config 未就绪'); return __config; };
// 提示：导出面变化（config -> getConfig），使用方需改写——故默认不自动转换
```
