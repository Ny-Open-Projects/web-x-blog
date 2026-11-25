---
title: [WEB-012] 描述一次完整的 TLS 1.2 握手过程。
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-012：描述一次完整的 TLS 1.2 握手过程。
**答**：
- ClientHello：客户端发送支持的 TLS 版本、加密套件列表、客户端随机数。
- ServerHello + Certificate：服务器选定套件，返回证书、服务器随机数；（RSA 密钥交换时）可能带 ServerHelloDone。
- 客户端验证证书链后，用公钥加密预主密钥发给服务器；双方用两个随机数 + 预主密钥算出会话密钥。
- 双方互发 Finished（用会话密钥加密的校验值），验证成功后开始加密通信。
- TLS 1.3 把握手压缩到 1-RTT，并废弃了 RSA 密钥交换（不支持前向安全）。

```mermaid
sequenceDiagram
    participant C as 客户端
    participant S as 服务器
    C->>S: ClientHello<br/>TLS版本 套件列表 客户端随机数
    S-->>C: ServerHello + Certificate<br/>服务器随机数
    C->>C: 验证证书链<br/>校验域名与有效期
    C->>S: 用公钥加密的预主密钥
    S->>S: 用私钥解出预主密钥
    Note over C,S: 双方用两个随机数加预主密钥<br/>推导出会话密钥
    C->>S: Finished 加密校验
    S-->>C: Finished 加密校验
    Note over C,S: 握手完成<br/>后续数据用对称密钥加密传输
```
