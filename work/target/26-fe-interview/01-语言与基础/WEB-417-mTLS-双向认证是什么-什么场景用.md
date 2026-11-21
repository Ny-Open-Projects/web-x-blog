---
title: [WEB-417] mTLS 双向认证是什么，什么场景用
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTPS]
type: 面试题
---

## WEB-417：mTLS 双向认证是什么，什么场景用

**答**：
- 普通 HTTPS 只有客户端验证服务端证书；mTLS 反过来服务端也要求客户端出示证书，双向认证
- 握手差异：服务端会发 CertificateRequest，客户端需配置 client key/cert，否则连接直接被拒
- 典型场景：B 端 API 开放平台、内部服务间调用（Service Mesh）、金融行业对终端的强身份校验
- 浏览器侧：用户要在系统里安装客户端证书，浏览器弹「选择证书」；程序化访问则在 fetch/代理层带证书
- 前端关联：mTLS 下抓包更麻烦（需导出客户端证书给 Charles），排查报错常是 `SSL handshake failed` 而非 401

```bash
# 命令行验证 mTLS：不带客户端证书会握手失败
curl -v https://api.partner.example.com/data
curl --cert client.pem --key client.key https://api.partner.example.com/data
```
