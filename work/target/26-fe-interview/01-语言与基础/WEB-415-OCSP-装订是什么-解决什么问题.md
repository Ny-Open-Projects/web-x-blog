---
title: [WEB-415] OCSP 装订是什么，解决什么问题
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTPS]
type: 面试题
---

## WEB-415：OCSP 装订是什么，解决什么问题

**答**：
- 证书吊销检查有两条路：CRL（下载整张吊销列表，大而慢）和 OCSP（实时单查，但暴露用户访问记录）
- OCSP 的痛点：浏览器每次握手去查 CA，多一次 RTT；CA 的 OCSP 服务故障时握手可能被拖慢
- 装订（Stapling）：由服务端定时去 OCSP 查好响应，握手时随证书一起发给浏览器，浏览器免查
- 收益：少一次外部请求、隐私（CA 看不到谁在访问你的站）、可用性不依赖 CA 实时在线
- 排查钩子：某站点偶现握手慢，可用 `openssl s_client -status` 看装订响应是否有效

```bash
openssl s_client -connect example.com:443 -status </dev/null 2>/dev/null | grep -A5 "OCSP"
# 有 "OCSP Response Status: successful" 说明装订生效
```
