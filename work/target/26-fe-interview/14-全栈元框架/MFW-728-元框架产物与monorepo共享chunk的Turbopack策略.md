---
title: [MFW-728] Turbopack 共享 chunk 策略
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-728：Turbopack 共享 chunk 策略

**答**:
- Turbopack 的 chunk 策略（RBL-551 扩展）：1) **模块级缓存**（每个模块独立编译任务——函数级粒度）；2) **共享 chunk 的自动识别**（多入口/多路由引用的模块 → 自动提共享 chunk（基于引用分析——不需要 manualChunks RBL-596 的自动化版）；3) **按需编译与 chunk**（dev 按需编译——chunk 边界在 dev 中是动态的（请求驱动的 chunk 分割）；prod 构建全量分析（最终 chunk 布局）。
- 与 webpack 的对比：webpack 的 splitChunks 配置（manualChunks 函数——手动声明）；Turbopack 的自动分割（引用分析驱动——零配置）；「配置驱动的分割 vs 分析驱动的分割」：自动分割的准确性（依赖图完整——分析精确）vs 配置的灵活性（手动微调——业务知识注入）。
- 追问钩子：为什么「自动 chunk 分割」不需要 manualChunks 配置？——Turbopack/Rolldown 的引用分析完整（全模块图——每个模块被谁引用精确知道）；基于引用图的自动决策（引用数 × 模块大小的加权——比人工 manualChunks 更精确）；「配置 vs 分析」：手动 = 人类判断（可能有遗漏/过时）；分析 = 机器判断（全量数据——但可能不符合业务意图）；自动优先 + 手动覆盖的分层（Turbopack 的策略）。

```typescript
// Turbopack 的自动 chunk 分割（概念）
interface ModuleRef { module: string; importedBy: Set<string>; sizeKB: number; }
function autoChunk(modules: ModuleRef[]) {
  return modules.map(m => {
    const refCount = m.importedBy.size;
    if (refCount >= 5 && m.sizeKB >= 10)
      return { module: m.module, chunk: 'shared', reason: `${refCount} 引用 × ${m.sizeKB}KB` };
    if (refCount === 1)
      return { module: m.module, chunk: 'route-specific', reason: '单路由引用' };
    return { module: m.module, chunk: 'shared', reason: '多路由引用（<5 但 >1）' };
  });
}
// 对比 manualChunks（webpack 手动）
// webpack: manualChunks: (id) => { if (id.includes('node_modules')) return 'vendor'; }
//  ↑ 手动规则：所有 node_modules → vendor（粗粒度——React 可能只有少数用）
// Turbopack: 引用分析自动（细粒度——按实际引用分）
```
