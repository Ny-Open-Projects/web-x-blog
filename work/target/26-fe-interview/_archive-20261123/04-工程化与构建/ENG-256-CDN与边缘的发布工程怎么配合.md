---
title: [ENG-256] CDN 与边缘的发布工程（缓存刷新/地域差异）怎么配合？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## ENG-256：CDN 发布工程怎么配合？
**答**：
- 发布节奏：先推 immutable 资源到全边缘（无缓存压力）→ 再刷新/更新 HTML（唯一需要刷新的东西）；HTML 更新按地域渐进（先小地域验证再全球）。
- 刷新策略：HTML 用 no-cache 或短 TTL（依赖回源验证）；错误的「全站刷新」会打垮回源带宽——只刷 HTML 是铁律。
- 地域差异处理：多地域部署（不同地域不同版本，灰度按地域切）时 manifest 按地域分发。
- CDN 故障预案：多 CDN 灾备（DNS 切换演练过）、本地兜底资源（关键资源的 Service Worker 缓存）。
- 追问钩子：为什么「只刷 HTML」能省 99% 刷新成本——hash 资源 URL 每次发布都变（天然无旧缓存问题），唯一不变的 HTML 才有缓存失效需求；全站 purge 既慢又贵还会引发回源风暴。

```bash
# 发布顺序
push-assets-to-all-edges dist/     # 1. immutable 资源全球预热
cdn.purge({ paths: ['/index.html'], region: ['cn-north'] })   # 2. HTML 地域渐进
# SW 兜底
workbox.precache(criticalAssets)   # CDN 挂时本地兜底
```
