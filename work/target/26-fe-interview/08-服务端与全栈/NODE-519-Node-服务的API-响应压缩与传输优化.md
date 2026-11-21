---
title: [NODE-519] Node 服务的响应压缩与传输优化（gzip/brotli/流式）如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-519：响应压缩与传输优化
**答**:
- 压缩选型：brotli（压缩率高 ~20% vs gzip，CPU 更贵——静态资源预压缩 brotli、动态响应 gzip 或低级别 brotli）、压缩级别权衡（CPU vs 带宽——大促时压缩是 CPU 大头 NODE-451 容量）；压缩阈值（< 1KB 不压——压缩开销超过收益）。
- 场景细节：JSON 动态响应压缩（gzip level 4~6 平衡）、流式响应（NODE-423：压缩会缓冲——流式禁压缩或用流式压缩 transform，首字节延迟权衡）、大 JSON 优化（字段裁剪优先于压缩 NODE-503——不传比压缩更省）。
- 传输协议：HTTP/2 多路复用（头部压缩 HPACK）、TLS 会话复用、keepalive agent（NODE-352 出站）。
- 缓存配合：ETag/304（内容未变不传 body——协商缓存对 API 同样有效）、增量更新（列表类接口 diff 传输——客户端合并，复杂度高按需）。
- 验证：响应体积分布/压缩率/压缩 CPU 占用监控——大促容量评估含压缩 CPU（ARC-446）。
```javascript
import compression from 'compression';
app.use(compression({ filter: (req, res) =>
  !req.path.startsWith('/stream') && res.getHeader('Content-Type')?.includes('json'),
  level: 5, threshold: 1024 }));                                 // 流式不压；>1KB 才压
// 静态产物：构建期预压 brotli → 服务端直接发 .br（省运行时 CPU）
```
