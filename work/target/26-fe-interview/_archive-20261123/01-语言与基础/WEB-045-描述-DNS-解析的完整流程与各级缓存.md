---
title: [WEB-045] 描述 DNS 解析的完整流程与各级缓存。
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-045：描述 DNS 解析的完整流程与各级缓存。
**答**：
- 顺序：浏览器 DNS 缓存 → 操作系统缓存（hosts 文件）→ 本地 DNS 服务器（递归查询）→ 根域名服务器 → 顶级域服务器（.com）→ 权威域名服务器，拿到 IP 后逐级返回并缓存。
- 查询方式：客户端到本地 DNS 是递归查询，本地 DNS 到各级域名服务器一般是迭代查询。
- 缓存时间由 TTL 控制，TTL 太短解析频繁、太长切换不灵活，发版前常提前调低 TTL。
- 前端优化手段：`dns-prefetch`、`preconnect`，以及 HTTPDNS 绕过运营商 DNS 劫持。

```bash
# 实测 DNS 解析链路
dig +trace www.example.com      # 展示从根到权威服务器的完整迭代过程
dig www.example.com +noall +answer   # 看最终结果与 TTL

nslookup www.example.com        # 备用工具
sudo dscacheutil -flushcache    # macOS 清空系统 DNS 缓存

# 查看 hosts 本地映射（优先级高于 DNS）
cat /etc/hosts
```
