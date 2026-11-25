---
title: [WEB-138] Charles/Fiddler 抓 HTTPS 的原理是什么？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-138：Charles/Fiddler 抓 HTTPS 的原理是什么？
**答**：
- 本质是中间人：抓包工具对客户端伪装成服务端、对服务端伪装成客户端，两条 TLS 各自独立。
- 前提是客户端信任工具的根证书——工具用它动态为每个域名签发"假证书"。
- 不装证书时浏览器报 NET::ERR_CERT_AUTHORITY_INVALID，这正是证书链校验在工作。
- App 侧还有"证书绑定"（SSL Pinning）挡中间人，需关闭校验或用系统级桥接才抓得到。
- 排障用途：看请求头细节、Map Local 改响应、模拟慢速与断网。

```bash
# 1) 把系统代理指向抓包工具
networksetup -setwebproxy Wi-Fi 127.0.0.1 8888
networksetup -setsecurewebproxy Wi-Fi 127.0.0.1 8888
# 2) 信任根证书后即可解密 HTTPS；用 mitmproxy 验证同一原理
mitmdump --listen-port 8888
# 3) 证书绑定的应用会拒绝假证书，表现为连接直接失败
curl -x http://127.0.0.1:8888 https://api.example.com -v 2>&1 | grep -i 'certificate'
```
