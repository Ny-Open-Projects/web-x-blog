---
title: [MFW-241] 元框架产物的冷启动分层优化（Edge 与 Node 双态）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-241：冷启动分层优化

**答**:
- 冷启动构成：进程/isolate 创建（平台侧不可控）+ 模块加载与求值（bundle 大小线性）+ 连接池预热（DB/Redis）+ JIT 预热（首请求慢）
- Node 态手段：bundle 拆分（server-only 路由懒 require）、v8 compile cache（RBL-479 同款——解析成本前移构建期）、TOP-LEVEL 副作用最小化（import 时不建连接——首请求才连）、预热探针（部署后 healthcheck 打几轮真实路由触发 JIT）
- Edge 态手段：bundle ≤ 1MB 预算（依赖审计砍 Node 专属库）、无状态快启动（不建池——HTTP 驱动 DB）
- 度量口径：P95 cold start（分平台/分路由）——优化前先有基线分解（哪一段占多少毫秒）

```text
分解：isolate 20ms + 模块求值 80ms（随 bundle） + 首连接 50ms + JIT 30ms
手段：compile cache / 懒 require / 部署后预热探针 / Edge 瘦身 ≤1MB
```
