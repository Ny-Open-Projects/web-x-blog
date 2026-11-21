---
title: [MFW-267] Edge 环境连 Redis 的限制与替代
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## MFW-267：Edge 连 Redis

**答**:
- 限制：Edge Runtime 无 TCP socket——传统 redis 客户端（ioredis）不可用；可用形态：HTTP 网关型（Upstash REST——每命令一 HTTPS）、或 Redis 落池到 Node 层（Edge 只出签名请求）
- 成本与延迟：REST 型每命令 20-50ms + 计费按命令——高 QPS 场景费用爆炸；管道化（一次请求多条命令）与本地微缓存（Edge 内 100ms TTL）是降费两手
- 架构建议：Edge 热路径尽量无状态（JWT 本地验签不查 Redis）——Redis 只在必要点（限流计数/会话版本）出 HTTP 手
- Node 层混合：重 Redis 语义（pub/sub/streams）留 Node 路由段——Edge/Node 按需分层

```text
Edge×Redis 决策：无 TCP → REST 驱动（Upstash）或 Node 层代理
降费：pipeline 合命令 + Edge 内 100ms 微缓存
首选：JWT 本地验签让热路径零 Redis
```
