---
title: [NODE-426] Node 服务的分布式追踪：成本与优先级治理如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-426：分布式追踪成本与优先级治理
**答**:
- span 成本结构：每个 span 序列化 + 存储 + 索引；高 QPS 服务全量 span 是成本大头（ARC-356 同构）。治理：采样分层（ARC-297/ARC-351）、span 瘦身（低价值 span 降级为指标计数：内部循环调用不打 span 只累计）、属性裁剪（span 属性白名单，禁整对象塞 attribute）。
- 优先级路由：核心链路（支付）永远低延迟上报（同步批量小延迟）、边缘链路（报表）批量大延迟；错误 trace 保真（ARC-351 尾部采样）。
- 存储分层：热 span（7 天可查）→ 聚合摘要（90 天：服务间依赖图与延迟分布）→ 丢弃；依赖图与 P99 曲线从 span 聚合预计算，不依赖原始明细。
- 观测自身成本：trace 上报量/字节数按服务分账，异常增长告警（新代码狂打 span）。
- 落地纪律：span 命名规范（route 级而非具体 id，防基数爆炸 NODE-372）、自定义 span 评审（新增埋点要证明排障价值）。
```javascript
// 高频内部调用：span 降级为指标
async function internalCall(op, fn) {
  const t = Date.now();
  try { return await fn(); }
  finally { if (slowOrSampled(Date.now() - t)) span.record(op, Date.now() - t); // 采样打 span
            else metrics.histogram('internal.call', Date.now() - t, { op }); }  // 其余只计指标
}
```
