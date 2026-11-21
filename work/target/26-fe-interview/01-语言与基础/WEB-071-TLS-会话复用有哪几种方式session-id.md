---
title: [WEB-071] TLS 会话复用有哪几种方式？session id、session ticket、PSK 有何区别？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-071：TLS 会话复用有哪几种方式？session id、session ticket、PSK 有何区别？
**答**：
- Session ID 复用：服务器把会话状态存在服务端并下发 ID，重连时客户端带上 ID，服务器查表恢复会话，只需 1-RTT（TLS1.3 中 0-RTT）。缺点是服务端有存储压力、不利于负载均衡。
- Session Ticket：服务器把加密后的会话状态发给客户端保存，重连时客户端原样带回，服务器解密恢复——无服务端存储，但要保证所有节点共享 ticket 加密密钥。
- PSK（TLS 1.3）：复用演化为预共享密钥，ClientHello 直接带 PSK 身份与 early data，实现 0-RTT。
- 工程要点：ticket 密钥要定期轮换；0-RTT 数据有重放风险（见 WEB-080）。

```nginx
# nginx 的会话复用配置
ssl_session_cache shared:TLS:10m;   # Session ID 模式：所有 worker 共享 10MB 会话表
ssl_session_timeout 1h;             # 会话可复用的时长
ssl_session_tickets on;             # 开启 Session Ticket 模式
ssl_session_ticket_key /etc/ssl/ticket.key;  # 多节点必须共享同一密钥文件，否则复用命中率骤降
# 命中复用时 curl 会打印 Reused, 抓包可见握手从 2-RTT 降到 1-RTT
```

```bash
# 验证会话复用：两次连接使用同一个 session 文件
curl -sv -o /dev/null --session-id-file /tmp/sess https://example.com 2>&1 | grep -i session
curl -sv -o /dev/null --session-id-file /tmp/sess https://example.com 2>&1 | grep -i reused
```
