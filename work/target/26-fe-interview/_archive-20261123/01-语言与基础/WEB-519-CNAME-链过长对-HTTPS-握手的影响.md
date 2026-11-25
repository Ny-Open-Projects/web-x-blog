---
title: [WEB-519] CNAME 链过长对 HTTPS 握手的影响
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 排查SOP]
type: 面试题
---

## WEB-519：CNAME 链过长对 HTTPS 握手的影响

**答**：
- CNAME 链：`cdn.example.com → vendor.map.fastly.net → ...`，每一跳都是一次 DNS 查询（多数可被缓存，但首次/低 TTL 时叠加 RTT）
- 影响：DNS 段耗时拉长 → TTFB 上升；链过长还容易因某一跳故障导致整体不可用
- 排查：dig 查 CNAME 链路，统计跳数与每跳 TTL；RUM 的 dns 段分位数突然劣化往往对应 CDN 厂商改了调度链
- 优化：自建/直连厂商提供的稳定域名、减少中间层、合理设置 TTL（不小于 300s）
- 面试钩子：浏览器对 DNS 预解析（dns-prefetch）只能覆盖第一跳，链下游无法预解析

```bash
dig +short cdn.example.com   # 逐跳看 CNAME
# 输出多行 = 链长；TTL 用 dig 查询的 answer 段查看
```
