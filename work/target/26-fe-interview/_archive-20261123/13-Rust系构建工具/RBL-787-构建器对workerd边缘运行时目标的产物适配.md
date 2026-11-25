---
title: [RBL-787] 边缘运行时目标的产物适配：workerd/edge 的 API 约束与条件打包
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-787：边缘运行时目标的产物适配：workerd/edge 的 API 约束与条件打包

**答**:
- 边缘运行时（Cloudflare Workers/workerd、Vercel Edge）的产物约束：1) **API 面受限**（无 Node 内置模块的完整实现——fs/net 部分可用、无原生模块、无长驻进程）；2) 冷启动敏感（bundle 体积与启动时间线性相关）；3) 单线程 CPU 时间上限（构建器编译的 bundle 不能有重量级初始化）。构建器的 edge 目标需要：Node API 的 polyfill/shim 注入（nodejs_compat 模式）或诊断「不可用 API」。
- 条件打包：edge 目标用 `conditions: ['workerd', 'edge-runtime', 'browser']` 解析（RBL-602 条件导出），包作者用条件提供 edge 版本（fetch 优先于 node http）——解析结果直接影响产物 API 面。
- 体积策略：edge bundle 的预算更紧（1MB 级别）——依赖裁剪（server 依赖里 edge 不需要的部分靠 external + 运行时提供或替换 shim）；「初始化瘦身」（顶层代码只做常量定义，重初始化放首次请求）。
- 兼容性审计：构建器扫描 edge 产物使用的 API（node:crypto 的子集/node:fs 等）对照 workerd 支持表——不支持的 API 精确诊断（哪个模块哪行用了），比运行时报错提前到构建期。
- 追问钩子：为什么 edge 目标「初始化瘦身」比体积优化更优先？——edge 冷启动 = 下载 + 编译 + 顶层执行；顶层执行的重活（大 Map 构建/同步 IO）在每次冷启动都付，而 bundle 下载有缓存缓解；「顶层只声明、请求时初始化」是 edge 产物结构的黄金法则。

```javascript
// edge 目标构建
const edgeBuild = {
  target: 'workerd',
  conditions: ['workerd', 'edge-runtime', 'browser', 'import'],   // 条件解析优先 edge 实现
  external: ['node:fs'],                                 // 或替换 shim
  plugins: [edgeApiAudit()],                             // API 兼容审计
};
// API 审计插件
function edgeApiAudit() {
  const UNSUPPORTED = /require\(['"]node:fs['"]\)|from ['"]node:fs['"]/;
  return {
    name: 'edge-api-audit',
    transform(code, id) {
      if (UNSUPPORTED.test(code))
        throw new Error(`RBL7001: ${id} 使用 node:fs（workerd 不支持）——请用边缘存储 API 或 nodejs_compat`);
      return null;
    },
  };
}
// 初始化瘦身（产物结构审计）
// ✗ 顶层: const bigMap = loadHugeMap();      每次冷启动执行
// ✓ 顶层: let bigMap; export function getMap() { return bigMap ??= loadHugeMap(); }
```
