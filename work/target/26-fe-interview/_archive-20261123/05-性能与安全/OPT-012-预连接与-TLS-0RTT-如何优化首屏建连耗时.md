---
title: [OPT-012] 预连接与 TLS 0-RTT 如何优化首屏建连耗时？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-012：预连接与 TLS 0-RTT 如何优化首屏建连耗时？

**答**：
- 一个新域名的完整建连 = DNS（1 RTT）+ TCP 握手（1 RTT）+ TLS 握手（1~2 RTT），跨域第三方资源首请求可能白白多花 200~400ms。
- `preconnect` 让浏览器提前并行完成这三步，之后请求直接复用连接。
- TLS 1.3 的 0-RTT（early data）允许复用会话的客户端在第一个握手包里直接携带请求数据，进一步省 1 RTT。
- 0-RTT 数据有重放风险，服务端只应对幂等的 GET 开启；`preconnect` 控制在 2~4 个关键域，多了反而抢占带宽。

```html
<!-- 一一对应：预连接关键第三方域 + 服务端开启 0-RTT 的说明 -->
<link rel="preconnect" href="https://cdn.example.com" />
<link rel="preconnect" href="https://api.example.com" crossorigin />
<link rel="dns-prefetch" href="https://static.third-party.com" />

<!-- Nginx 服务端开启 TLS1.3 与 0-RTT（仅接受幂等请求）：
     ssl_protocols TLSv1.2 TLSv1.3;
     ssl_early_data on;
     配合 proxy_set_header Early-Data $ssl_early_data; 在应用层拦截非幂等重放 -->
```

## 三、代码分割与产物优化
