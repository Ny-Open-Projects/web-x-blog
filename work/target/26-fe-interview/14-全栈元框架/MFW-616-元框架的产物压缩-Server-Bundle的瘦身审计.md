---
title: [MFW-616] Server Bundle 瘦身审计
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-616：Server Bundle 瘦身审计

**答**:
- server bundle 的瘦身维度（RBL-586 的 server 侧）：1) **external 化**（serverDependenciesWhitelist/Blacklist——依赖打包 vs external：standalone 追踪 vs 函数体积）；2) **未用导出的摇树**（server bundle 的 sideEffects——RBL-613）；3) **trace 的保守包含**（动态 require = 整包进——audit 工具：standalone 的 node_modules top10）；4) **serverless 函数的冷启动预算**（bundle 体积 → 冷启动时长——预算门禁）。
- 瘦身的具体手段：依赖替换（moment → dayjs RBL-739——server bundle 也适用）；动态 import 切分（低频依赖 lazy——冷启动 RBL-518）；native 模块的独立层（prisma engine 二进制——镜像分层 RBL-681）。
- 审计自动化：构建输出 server bundle 体积 → 归因（依赖树）→ 门禁（体积超预算 fail）。
- 追问钩子：为什么「server bundle 瘦身」的 ROI 低于 client 但仍值得做？——server bundle 影响冷启动（每次扩容/函数冷启）而非用户感知（用户不下载 server bundle）；ROI 低的原因：影响面是「基础设施成本」而非「用户指标」；值得做的场景：serverless 冷启动敏感（高并发扩容/定时任务）+ 内存成本（实例内存 = 计费）；「server 侧的性能预算」与 client 预算的优先级差异——用户感知优先是排序原则（RBL-952 占比 × 收益的 server 版：server bundle 的「占比」= 冷启动时长占比）。

```typescript
// server bundle 审计
// next.config: { experimental: { serverComponentsExternalPackages: ['sharp', 'prisma'] } }
// external：native/重依赖不打进 bundle（standalone trace 拷贝）
// 瘦身审计（standalone）
function auditServerBundle(standaloneDir, { budgetMB = 100 } = {}) {
  const size = du(standaloneDir);                        // 总体积
  const top = topDeps(`${standaloneDir}/node_modules`, 10);
  return { sizeMB: size, over: size > budgetMB, top };   // top 依赖：瘦身靶点
}
// 动态 import 切分（冷启动）
// 反模式：顶层 import heavyAnalytics（冷启动就加载）
// 修正：请求时 lazy
export async function GET() {
  const { track } = await import('./heavy-analytics');   // 首次请求才加载
  return handle(track);
}
```
