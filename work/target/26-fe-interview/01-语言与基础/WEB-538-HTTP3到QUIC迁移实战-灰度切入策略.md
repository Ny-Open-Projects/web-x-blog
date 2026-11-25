---
title: [WEB-538] HTTP/3 到 QUIC 迁移实战：灰度切入策略怎么设计
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTP3]
type: 面试题
---

## WEB-538：HTTP/3 到 QUIC 迁移实战：灰度切入策略怎么设计

**答**：
- 灰度单元按「域名 × 机房 × 流量比例」三维切：先选非核心静态域名开 1% 流量，而不是全站开关
- 切入靠响应头引导而非客户端配置：`Alt-Svc: h3=":443"; ma=86400`，浏览器只在支持且首访成功后才用 h3 重连，天然自带回退
- 分层验证：接入层（CDN/网关 h3 开关）→ 服务端（握手成功率、0-RTT 占比）→ 前端（Performance 里 protocol 采样上报）
- 灰度指标卡点：h3 命中率、h3 请求失败率（对照 h2）、P75 TTFB、连接复用率；任一劣化超阈值先降级再排查
- 观察周期至少覆盖一周：UDP 弱网表现有明显的运营商/地域差异，工作日与周末流量结构也不同

```javascript
// 前端采样上报实际生效的协议，支撑灰度决策
const report = () => {
  const nav = performance.getEntriesByType('navigation')[0];
  if (!nav) return;
  navigator.sendBeacon('/api/mon/protocol', JSON.stringify({
    proto: nav.nextHopProtocol,   // 'h3' / 'h2' / 'http/1.1'
    ttfb: nav.responseStart - nav.startTime,
    region: window.__REGION__,
  }));
};
addEventListener('pagehide', report);
// 网关侧灰度：按 header/cookie/地域路由到 h3 集群，异常一键切回 h2
```
