---
title: [MFW-551] Turbopack 的函数级缓存：Rust 管道与按需编译
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-551：Turbopack 函数级缓存与按需编译

**答**:
- Turbopack 的差异化：1) **函数级增量**（RBL-087：模块内函数级缓存——不只模块级；改一个函数只重编译该函数——Turbo 引擎的任务图记忆化）；2) **按需编译**（dev 不全量 build——请求什么编译什么（persisted cache + lazy graph——dev server 的模块图是懒展开的）；3) Rust 管道（核心编译全 Rust——JS 插件跨 NAPI RBL-562）。
- 与 Vite 的架构对比：Vite = esbuild 转换 + rollup 打包（dev ESM 按需、prod rollup 全量）——dev/prod 行为差异（双引擎）；Turbopack = 统一引擎（dev/prod 同管道——一致性优先）；「双引擎的一致性风险」（dev 可 prod 崩——构建差异 bug 类）vs Turbopack 的统一成本（重 Rust 工程）。
- 持久化缓存：跨进程缓存（.turbo 目录——函数级缓存落盘 RBL-633）——重启后秒恢复。
- 追问钩子：为什么「dev/prod 双引擎」是元框架要消灭的架构债？——双引擎的行为差异 = 「dev 跑通 prod 崩」的 bug 类（构建配置在两引擎语义不同）；统一引擎（Turbopack/Vite 的 rolldown 迁移 RBL-590）让「dev 的正确性承诺覆盖 prod」——一致性是元框架的隐性 SLA：dev/prod 的行为等价是「语义等价验证」的常驻目标（RBL-649 的运行时版）。

```javascript
// Turbopack 的任务图记忆化（概念）
const taskGraph = new Map();                             // taskKey -> { deps, result }
function memoizedTask(key, compute, deps) {
  const cached = taskGraph.get(key);
  if (cached && deps.every(d => taskGraph.get(d)?.version === cached.depVersions[d]))
    return cached.result;                                // 依赖版本不变 → 直接复用
  const result = compute(deps.map(d => taskGraph.get(d)?.result));
  taskGraph.set(key, { result, version: hash(result),
    depVersions: Object.fromEntries(deps.map(d => [d, taskGraph.get(d)?.version])) });
  return result;
}
// 函数级粒度：key = module:exportName（不只 module）
// memoizedTask('src/page.tsx:Header', compileHeader, ['src/page.tsx:parse'])
// 按需编译：dev server 收到 /page 请求 → 只展开该路由闭包
// 未触达的路由模块不编译（graph lazy）
```
