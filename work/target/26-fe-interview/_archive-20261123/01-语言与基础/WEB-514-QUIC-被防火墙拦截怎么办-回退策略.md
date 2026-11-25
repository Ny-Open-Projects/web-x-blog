---
title: [WEB-514] QUIC 被防火墙拦截怎么办，回退策略设计
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTP3]
type: 面试题
---

## WEB-514：QUIC 被防火墙拦截怎么办，回退策略设计

**答**：
- 现状：企业防火墙、部分运营商对 UDP 443 拦截或限速，QUIC 握手超时——表现为「部分用户直连失败、部分正常」
- 浏览器内建回退：HTTP/3 失败自动落回 HTTP/2，用户无感，但会浪费一个超时周期（首次访问多几百毫秒）
- 服务端设计：Alt-Svc 持续通告 H3；若 RUM 显示某地区 H3 成功率低，可在接入层对相应地域关闭通告
- 客户端加速：连接池记住「该域名 H3 可用/不可用」，失败后短期内不再尝试（happy eyeballs 思路）
- 排查方法：RUM 按 nextHopProtocol 分组看成功率，用拨测脚本从异常地区实测 UDP 443 连通性

```javascript
// 上报协议分布，监控 H3 回退率
addEventListener('load', () => {
  const nav = performance.getEntriesByType('navigation')[0];
  report({ proto: nav.nextHopProtocol, region: geo || '' });
});
```
