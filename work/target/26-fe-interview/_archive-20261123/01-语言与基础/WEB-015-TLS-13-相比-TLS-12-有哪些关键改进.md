---
title: [WEB-015] TLS 1.3 相比 TLS 1.2 有哪些关键改进？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-015：TLS 1.3 相比 TLS 1.2 有哪些关键改进？
**答**：
- 握手从 2-RTT 减到 1-RTT，支持会话恢复时 0-RTT。
- 删除不安全套件：移除 RSA 静态密钥交换、CBC 模式、RC4、MD5 等，只保留 AEAD（AES-GCM、ChaCha20-Poly1305）。
- 强制前向安全：密钥交换只允许（EC）DHE，私钥泄露也无法解密历史流量。
- 握手过程中的 ServerHello 之后大部分消息已加密，减少元信息暴露。

```nginx
# TLS 1.3 生产配置：只保留安全套件，开启会话恢复
server {
    listen 443 ssl;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers off;      # TLS 1.3 忽略此指令，由客户端优先
    ssl_early_data on;                  # 开启 0-RTT（注意重放风险，见 WEB-009）
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 1d;
    ssl_session_tickets on;             # 会话票据，配合 1-RTT 恢复
}
```
