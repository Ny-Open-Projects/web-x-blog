---
title: [BAS-109] localhost 和 127.0.0.1 有什么区别？hosts 文件是干嘛的？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-109：localhost 和 127.0.0.1 有什么区别？hosts 文件是干嘛的？
**答**：
- localhost 是域名要先解析（可能解析到 IPv6 ::1）；127.0.0.1 是环回 IPv4 地址。服务只监听 ::1 时用 127.0.0.1 会连不上，反之亦然。
- 127.0.0.0/8 整段都指向本机，127.0.0.2 等同样可用，可在同机模拟不同"IP"。
- hosts 文件把域名映射到 IP、优先于 DNS，本地调试伪造线上域名靠它（macOS 路径 /etc/hosts）。

```bash
# /etc/hosts：本地域名映射
127.0.0.1  dev.example.com
::1        dev.example.com   # 同时映射 IPv6，避免解析回退
sudo dscacheutil -flushcache      # macOS 清 DNS 缓存
curl -v http://dev.example.com:3000
```
