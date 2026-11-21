---
title: [MFW-237] 流式 SSR 的 TTFB 与 RSC Payload 字节优化
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-237：流式 SSR 字节优化

**答**:
- Payload 构成：组件树序列化（props/children 引用图）——重复大对象多次序列化是膨胀主源（同一 data 传给 5 个 client 组件 = 5 份拷贝）
- 瘦身手段：server 端裁剪 props（只传渲染字段——不传全量 row）、共享大对象用模块级状态或 URL 再取（不序列化重复）、列表传 id + 客户端按需拉（超长列表）
- TTFB 优化：Shell 极小化（layout 不做重查询——Suspense 包住数据段让首字节 < 200ms）、压缩（flight 是文本，gzip/brotli 收益大——确认 CDN 对 RSC 内容类型启用压缩）
- 度量：Payload 大小进监控（按路由 P95）——回归告警（新增 client props 导致 payload 翻倍可被捕获）

```javascript
// 瘦身：server 端只传渲染字段
- <Row row={hugeRow} />                       // 全量 50 字段
+ <Row id={row.id} title={row.title} />        // 渲染只需 3 字段
// 监控：按路由记录 RSC payload P95 字节，涨 50% 告警
```
