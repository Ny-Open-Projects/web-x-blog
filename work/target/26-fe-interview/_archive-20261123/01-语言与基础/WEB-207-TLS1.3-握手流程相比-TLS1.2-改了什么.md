---
title: [WEB-207] TLS 1.3 握手流程相比 TLS 1.2 改了什么？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTPS]
type: 面试题
---

## WEB-207：TLS 1.3 握手流程相比 TLS 1.2 改了什么？

**答**：
- RTT 减少：TLS 1.2 完整握手 2-RTT；TLS 1.3 客户端在 ClientHello 里直接带上密钥共享（key_share），1-RTT 完成握手，复用会话时 0-RTT。
- 算法裁剪：删掉 RSA 密钥交换（无前向保密）、CBC 模式、RC4/3DES 等弱算法，只留 AEAD（AES-GCM、ChaCha20-Poly1305）与 ECDHE/DHE。
- 握手加密：ServerHello 之后的握手报文全部加密，TLS 1.2 的证书是明文传输的。
- 单轮握手：去掉了 ChangeCipherSpec 的冗余交互，密钥派生用 HKDF 一次算齐三阶段密钥（early/handshake/application）。

```bash
# 实测对比握手 RTT 与协商协议
openssl s_client -connect cloudflare.com:443 -tls1_3 </dev/null 2>/dev/null \
  | grep -E 'New, TLSv|Cipher is'
# Wireshark 抓包对比：TLS1.2 能看到明文证书，TLS1.3 证书在 EncryptedExtensions 之后
```
