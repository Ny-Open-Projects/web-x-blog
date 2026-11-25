---
title: [WEB-551] QUIC 迁移：证书与 HTTPS 配置有哪些坑
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-551：QUIC 迁移：证书与 HTTPS 配置有哪些坑

**答**：
- QUIC 强制 TLS1.3：还在用 TLS1.2 证书配置/老密码套件的服务器，QUIC 监听直接起不来或握手全失败
- 中间证书链不全在 QUIC 下更隐蔽：TCP TLS 客户端还会走 AIA 补全，QUIC 握手失败更快且日志少，上线前用 `openssl s_client`/在线检测工具全链路验一遍
- 证书热更新要同步到 QUIC 层：很多自建 QUIC 服务 reload 只重载 TCP 配置，QUIC 监听还挂旧证书，到期瞬间全站 h3 失败
- ECDSA 证书优先：QUIC 握手包有大小限制（Initial 包 ~1200B 填充），RSA 2048 证书握手消息更大，ECDSA 更容易单包完成、0-RTT 更稳
- OCSP stapling：QUIC 同样支持且建议开启，但 stapling 刷新逻辑要与 TCP 侧独立验证，避免一边有一边没有

```bash
openssl s_client -connect example.com:443 -quic -alpn h3 -verify_return_error
# 检查点: TLS1.3 协商成功 / 证书链完整 / ALPN h3 被选中
# 证书轮换 SOP: TCP 与 QUIC 配置同文件管理, reload 后双协议各探活一次
```
