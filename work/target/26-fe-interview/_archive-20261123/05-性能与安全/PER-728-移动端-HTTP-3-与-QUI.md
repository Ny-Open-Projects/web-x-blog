---
title: [PER-728] 移动端 HTTP/3 与 QUIC 的弱网收益：前端要做什么才能吃到 0-RTT 与连接迁移的红利？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-728：移动端 HTTP/3 与 QUIC 的弱网收益：前端要做什么才能吃到 0-RTT 与连接迁移的红利？

**答**：
- QUIC 弱网三大收益：0-RTT 重连（省 1~2 RTT）、连接迁移（WiFi/蜂窝切换不断连）、抗丢包（无队头阻塞）——但前端要配合：**Alt-Svc 发现**（服务端响应头告知 h3 端口，浏览器后续请求升级）、预连接（`<link rel=preconnect>` 会尝试 h3）、证书与会话票据缓存正常工作才有 0-RTT。
- 前端注意事项：0-RTT 数据有重放风险（幂等 GET 才可 0-RTT，POST 支付类服务端要拒绝 0-RTT 重放，前端不用特殊处理但要知晓）；连接迁移依赖两端配置；h3 不可用时自动回退 h2（前端无感但要监控协议分布确认升级率）。
- 度量：协议分布（h1/h2/h3 占比，Performance API `nextHopProtocol`）、0-RTT 命中率、切网期间请求失败率对比。
- 落地路径：CDN 开 h3 -> 响应头加 Alt-Svc -> 监控 nextHopProtocol 升级曲线 -> 弱网分桶验证收益。

```javascript

const quicPlaybook = {
  benefits: ['0-RTT 重连省 1~2 RTT', '连接迁移（切网不断连）', '无队头阻塞抗丢包'],
  frontend: { discover: 'Alt-Svc 响应头自动升级，无需 JS 改动',
    preconnect: '<link rel=preconnect> 会尝试 h3',
    replay: '0-RTT 有重放风险：GET 幂等可用，POST 支付类服务端必须拒绝' },
  verify: 'performance.getEntriesByType("resource").map(r => r.nextHopProtocol) 看协议分布',
  rollout: 'CDN 开 h3 -> Alt-Svc -> 监控升级曲线 -> 弱网分桶验证失败率下降',
};
console.log(performance.getEntriesByType('resource')
  .slice(-10).map(r => `${new URL(r.name).host}: ${r.nextHopProtocol}`).join('\n'));
```
