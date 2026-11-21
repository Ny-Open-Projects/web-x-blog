---
title: [WEB-532] WebSocket 网关升级失败的排查
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 排查SOP]
type: 面试题
---

## WEB-532：WebSocket 网关升级失败的排查

**答**：
- 失败形态：握手返回 200/400/502 而不是 101 Switching Protocols——升级请求在某层被当成普通 HTTP 处理
- 分层排查：Nginx 缺 `proxy_set_header Upgrade/Connection` 配置 → SLB/网关未开 WS 支持 → 服务端 origin 校验拒绝 → 防火墙拦 Upgrade 头
- 特征识别：连接立刻关闭 vs 授权后被踢（401/403）vs 长连接反复断（超时配置），三种症状对应三类层
- 修复模板：Nginx 需 `proxy_http_version 1.1` + Upgrade 头透传 + 合理的 read timeout；云 LB 检查是否启用 WebSocket/长连接模式
- 客户端配合：握手失败要有降级通道（轮询/SSE），保证业务可用性不依赖单通道

```nginx
location /ws/ {
    proxy_pass http://ws_backend;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_read_timeout 300s;   # 小于心跳周期的两倍
}
```
