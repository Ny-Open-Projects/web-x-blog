---
title: [OPT-048] TLS 层怎么优化？会话复用和 TLS 1.3 各省多少？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-048：TLS 层怎么优化？会话复用和 TLS 1.3 各省多少？

**答**：
- TLS 握手是首屏 RTT 大头：TLS 1.2 全握手 2-RTT，TLS 1.3 降到 1-RTT，会话复用后 0-RTT，弱网下省 300ms+。
- 会话复用两机制：**Session ID**（服务端存状态）与 **Session Ticket**（加密状态下发给客户端），Nginx 默认开 ticket 但要配稳定的密钥文件，多机共享否则命中率近 0。
- TLS 1.3 的 0-RTT 有重放风险，只对 GET 类幂等请求安全，敏感接口要服务端拒重放。
- 证书链裁剪 + ECDSA 证书比 RSA 小一半、握手计算量低，都是零代码改动的收益。

```nginx
# 一一对应：Nginx TLS 层优化完整配置
server {
    listen 443 ssl;
    http2 on;

    # 1. TLS 1.3 优先，1.2 兜底；1.3 自动获得 1-RTT 握手
    ssl_protocols TLSv1.2 TLSv1.3;

    # 2. 会话复用：ticket 密钥固定到文件，多台机器共用同一份，命中率才能上去
    ssl_session_tickets on;
    ssl_session_ticket_key /etc/nginx/tls/session_ticket.key; # openssl rand 80 > 该文件
    ssl_session_cache shared:SSL:50m;  # Session ID 缓存，50m 约可存 20 万会话
    ssl_session_timeout 1d;            # 会话有效期，长了复用率高但安全窗口变大

    # 3. OCSP stapling：由服务端代查证书状态随握手下发，省掉客户端 OCSP 查询 RTT
    ssl_stapling on;
    ssl_stapling_verify on;
    ssl_trusted_certificate /etc/nginx/tls/chain.pem;
    resolver 223.5.5.5 valid=300s;

    # 4. ECDSA 证书 + 裁剪后的证书链（中间证书只带必要的那一级）
    ssl_certificate     /etc/nginx/tls/fullchain.pem;
    ssl_certificate_key /etc/nginx/tls/privkey.pem;

    # 5. TLS 1.3 0-RTT：配合 GET 幂等接口开启
    ssl_early_data on;
    proxy_set_header Early-Data $ssl_early_data; # 透传给应用，应用侧拒绝对 0-RTT 请求做写操作
}
```
