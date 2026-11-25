---
title: [NODE-508] Node 服务的 CDN 协同（边缘缓存与回源）策略如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-508：CDN 协同与边缘缓存
**答**:
- 分工：静态资源（immutable 长缓存 ARC-368）、动态 API 的边缘缓存（可缓存 API：Edge 侧缓存——回源率下降）、不可缓存 API（直回源）。CDN 缓存策略是 BFF 缓存体系（NODE-502）的最外层。
- 边缘缓存设计：Cache-Control 精确声明（API 响应头声明可缓存性：s-maxage/stale-while-revalidate——BFF 按接口声明缓存头而非 CDN 侧配置规则）、缓存 key 归一（query 排序/大小写——防同数据多 key 降命中率）、Vary 处理（按 cookie/设备变化的响应——Vary 声明准确否则缓存串户）。
- 失效协同：purge 协议（NODE-507 失效广播触发 CDN purge——API 级失效单 URL/prefix/tag purge）、软失效（stale-while-revalidate：边缘回旧值同时回源刷新——用户无感更新）。
- 回源保护：缓存预热（大促前热点 API 预热回源——防冷缓存击穿 NODE-438）、回源限流（CDN 回源突发保护——回源也打不垮源站）。
- 观测：边缘命中率（按接口分桶）、purge 生效时延、回源率异常告警（命中率骤降 = 缓存配置事故）。
```nginx
# BFF 响应声明（CDN 按 Cache-Control 行为）
add_header Cache-Control "public, s-maxage=60, stale-while-revalidate=30";
add_header Vary "Accept-Encoding, X-Device-Profile";             # 精确 Vary 防串
```
