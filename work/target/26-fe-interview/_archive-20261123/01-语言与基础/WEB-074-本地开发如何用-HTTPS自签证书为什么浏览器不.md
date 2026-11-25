---
title: [WEB-074] 本地开发如何用 HTTPS？自签证书为什么浏览器不信任？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-074：本地开发如何用 HTTPS？自签证书为什么浏览器不信任？
**答**：
- 自签证书的"根"是开发者自己，不在操作系统/浏览器的信任库里，所以报 NET::ERR_CERT_AUTHORITY_INVALID——不是证书格式错了，而是信任锚缺失。
- 正确做法：mkcert 在本地生成一个本地 CA 并安装到系统/浏览器信任库，再由它给 localhost 签发证书，链路完整所以无警告。
- 手动 openssl 自签时必须带 SAN（`-addext "subjectAltName=DNS:localhost"`），Chrome 早已不接受只写 CN 的证书。
- 团队共享：把 mkcert 的 rootCA.pem 分发给同事安装，或用内网 CA。

```bash
# 方案一：mkcert 一条龙（推荐）
mkcert -install                                   # 生成本地 CA 并装入信任库
mkcert localhost 127.0.0.1 ::1 dev.local          # 签出证书与私钥
# 输出 localhost+2.pem 与 localhost+2-key.pem

# 方案二：纯 openssl 自签（需手动信任 root）
openssl req -x509 -newkey rsa:2048 -nodes -days 365 \
  -keyout dev.key -out dev.crt \
  -subj '/CN=dev.local' \
  -addext 'subjectAltName=DNS:dev.local,DNS:localhost,IP:127.0.0.1'
# 浏览器导入 dev.crt 到"受信任的根证书颁发机构"后才不报警

# nginx 挂上证书
# server { listen 443 ssl; ssl_certificate dev.crt; ssl_certificate_key dev.key; }
```

## 十四、网络性能与传输
