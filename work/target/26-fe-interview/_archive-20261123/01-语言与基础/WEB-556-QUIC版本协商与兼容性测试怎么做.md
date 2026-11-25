---
title: [WEB-556] QUIC 版本协商与兼容性测试怎么做
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTP3]
type: 面试题
---

## WEB-556：QUIC 版本协商与兼容性测试怎么做

**答**：
- QUIC v1 是当前主流，但草案期版本（draft-27~34）仍在部分 SDK/老客户端存在：服务端要明确「只支持 v1」还是兼容多版本，版本不匹配时回 Version Negotiation 包
- 兼容性矩阵要建起来：主流浏览器（Chrome/Edge/Firefox/Safari）× App 内 WebView（Android WebView 对 h3 支持滞后）× 自研 SDK（cronet/自封装 quic 库）
- 测试方法：用 curl(--http3)/nghttp3/openssl 各跑一遍握手，加上真实设备矩阵（老 Android 机型是重灾区），产出支持度报表
- 灰度按客户端能力下发 Alt-Svc：对不支持/支持差的 UA 不下发，避免「给了引导但握手必失败」的负收益
- 协议升级预案：未来 h3 演进（如多路径扩展）落地时，同样走版本协商灰度，不要假设「h3 就是一个固定版本」

```bash
curl -sI --http3-only https://example.com -o /dev/null -w '%{http_version}\n'
# 输出 HTTP/3 → v1 正常；失败查 ALPN 与版本支持
# 矩阵落库: { ua: 'Android WebView 9x', h3: false, action: '不下发Alt-Svc' }
```
