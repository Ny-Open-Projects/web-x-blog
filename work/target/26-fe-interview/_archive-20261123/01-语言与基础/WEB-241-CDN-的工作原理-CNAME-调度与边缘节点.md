---
title: [WEB-241] CDN 的工作原理：CNAME 调度与边缘节点
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, CDN]
type: 面试题
---

## WEB-241：CDN 的工作原理：CNAME 调度与边缘节点

**答**：
- 接入：源站域名 CNAME 到 CDN 的调度域名（如 `www.example.com → www.example.com.cdn.dnsv1.com`）。
- 调度：用户解析该域名时，CDN 的智能 DNS 按用户 IP 归属（运营商/地理位置）返回最近的边缘节点 IP——移动用户回移动节点，跨网慢。
- 服务：边缘节点有缓存则直接返回（命中），未缓存则回源拉取、缓存后返回（回源）。
- 一致性：边缘节点按 Cache-Control/边缘规则缓存；源站更新后通过刷新（purge）或预热（prefetch）接口管理。
- 收益量化：静态资源就近取，TTFB 从跨国几百 ms 到本地几十 ms；源站带宽被边缘缓存吸收。

```bash
dig +short www.example.com      # 观察 CNAME 链与最终边缘 IP
curl -sI https://www.example.com/app.js | grep -iE 'x-cache|hit|miss'
# X-Cache: HIT 命中边缘缓存
```
