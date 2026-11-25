---
title: [WEB-133] DNS 缓存分哪几层？TTL 怎么影响故障切换速度？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-133：DNS 缓存分哪几层？TTL 怎么影响故障切换速度？
**答**：
- 层级：浏览器进程内缓存 → 系统 resolver 缓存（/etc/hosts 优先级更高）→ 本地递归 DNS → 权威 DNS。
- TTL 决定每层"记多久"：TTL 越长命中率越高，但故障切换要等旧记录自然过期。
- 迁移与容灾 SOP：提前把 TTL 降到 60 秒 → 等旧值过期 → 切流量 → 稳定后再调回长 TTL。
- 浏览器有独立的 DNS 缓存与连接池（chrome://net-internals/#dns 可看可清）。
- 注意：某些递归服务器会最小化或"钉住" TTL，客户端拿到的值不一定等于权威配置值。

```bash
# 连续两次查询同一个递归 DNS，观察 TTL 递减，说明命中了本地解析器缓存
dig +noall +answer api.example.com
sleep 5
dig +noall +answer api.example.com
# 直接问权威服务器，TTL 应该是配置的原始值
dig @ns1.example.com api.example.com +noall +answer
# macOS 清系统 DNS 缓存
sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder
```
