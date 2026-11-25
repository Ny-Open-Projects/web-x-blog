---
title: [WEB-236] DNS 递归查询与迭代查询的区别？解析全过程
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, DNS]
type: 面试题
---

## WEB-236：DNS 递归查询与迭代查询的区别？解析全过程

**答**：
- 递归查询：客户端→本地 DNS，「你必须给我最终答案」；迭代查询：本地 DNS→根/顶级/权威服务器，「你告诉我下一步问谁」。分工上客户端只需面对本地 DNS。
- 完整链路：浏览器缓存 → 系统缓存（hosts）→ 本地 DNS（运营商/8.8.8.8）→（迭代）根域名服务器告知 .com 的 NS → 顶级域 NS 告知 example.com 的 NS → 权威 NS 返回 A 记录 IP。
- 多级缓存带 TTL：每一层都缓存，DNS 改记录生效要等 TTL 过期，所以老项目「换 IP」要提前调低 TTL。
- 前端相关：`dns-prefetch` 提前解析第三方域名；IP 不变迁移用 CNAME；大厂内部用 HTTPDNS 绕运营商劫持。

```bash
# 追踪解析链路
dig +trace www.example.com
# 看 TTL 与缓存
dig www.example.com | grep -A1 'ANSWER SECTION'
```
