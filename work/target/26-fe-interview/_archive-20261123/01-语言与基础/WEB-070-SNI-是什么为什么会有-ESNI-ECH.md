---
title: [WEB-070] SNI 是什么？为什么会有 ESNI/ECH？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-070：SNI 是什么？为什么会有 ESNI/ECH？
**答**：
- 同一台 IP 上部署多个 HTTPS 站点时，服务器需要在握手最早期知道客户端要访问哪个域名才能选对证书——这就是 SNI，在 ClientHello 中明文携带域名。
- 问题：SNI 是明文的，网络中间设备能看到你在访问哪个站点，等于泄露浏览目标。
- ESNI（后演进为 ECH Encrypted Client Hello）用站点 DNS 记录里发布的公钥把整个 ClientHello 加密，隐藏域名。
- 前端感知：ECH 依赖 DNS 的 HTTPS 记录与 DoH，配置于服务端与浏览器侧，应用代码无感。

```nginx
# 同一 IP 托管两个 HTTPS 站点，依赖 SNI 区分并选择证书
server {
    listen 443 ssl;
    server_name api.example.com;
    ssl_certificate     /etc/ssl/api.example.com.crt;
    ssl_certificate_key /etc/ssl/api.example.com.key;
}
server {
    listen 443 ssl;
    server_name www.example.com;
    ssl_certificate     /etc/ssl/www.example.com.crt;
    ssl_certificate_key /etc/ssl/www.example.com.key;
}
```

```bash
# 观察 SNI 的明文暴露与指定 SNI 的效果
# 不带 SNI，服务器只能返回默认站点证书
openssl s_client -connect 1.2.3.4:443 </dev/null | openssl x509 -noout -subject
# 显式携带 SNI，服务器返回对应域名的证书
openssl s_client -connect 1.2.3.4:443 -servername www.example.com </dev/null \
  | openssl x509 -noout -subject
```
