---
title: [WEB-311] ECDHE 的"前向保密"到底保护了什么？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTPS]
type: 面试题
---

## WEB-311：ECDHE 的"前向保密"到底保护了什么？
**答**：
- 如果用 RSA 密钥传输：服务器私钥泄漏，历史抓包可全部解密（私钥长期不变）。ECDHE 每次握手生成临时密钥对，会话密钥不落盘、不随私钥泄漏。
- 前向保密 = 过去的通信在密钥泄露后依然安全；TLS1.3 只保留带 FS 的套件，RSA 密钥交换已删除。
- 注意边界：FS 防密钥泄漏不防端点被黑（客户端中木马照样能被窃听）。

```javascript
// ECDHE: 每次会话临时密钥
const ecdh = (a, b) => 'shared-' + ((a * b) % 97); // 椭圆曲线点乘示意
const session1 = ecdh(7, 13), session2 = ecdh(5, 11); // 不同的临时私钥
console.log(session1 !== session2); // true：会话密钥互不相关
// 服务器私钥（签证书用）泄漏 ≠ 历史会话可解
```
