---
title: [WEB-540] HTTP/3 迁移：h2/h3 双栈部署的共存方案
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTP3]
type: 面试题
---

## WEB-540：HTTP/3 迁移：h2/h3 双栈部署的共存方案

**答**：
- 双栈是迁移期的标准形态：同一 443 端口 TCP 承载 h2、UDP 承载 h3，证书与域名完全一致，客户端自行协商
- 关键是一致性：CDN/源站在 h2 与 h3 两条链路上的缓存键、回源策略、压缩配置必须相同，否则灰度对照组数据被污染
- Session 复用跨协议打通：TLS session ticket 在 h2/h3 间共享，迁移期老用户从 h2 切 h3 可免完整握手
- 服务端健康检查要双协议分开：UDP 通路抖动不影响 TCP 健康检查，否则会出现「h3 半死但探活全绿」
- 配置漂移防护：h2/h3 配置放同一份 IaC，禁止单边改配置，CI 里加 diff 校验

```nginx
listen 443 quic reuseport;      # UDP，h3
listen 443 ssl;                  # TCP，h2/h1
http2 on;
ssl_early_data on;               # 0-RTT，h2/h3 共享 ticket 生态
add_header Alt-Svc 'h3=":443"; ma=86400' always;
# 注意：reuseport 多 worker 需相同的 quic 密钥配置，否则连接迁移后失联
```
