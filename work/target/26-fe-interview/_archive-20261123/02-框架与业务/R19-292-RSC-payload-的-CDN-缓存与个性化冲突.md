---
title: [R19-292] RSC payload 的 CDN 缓存与个性化怎么共存？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-292：RSC payload 的 CDN 缓存与个性化怎么共存？
**答**：
- payload 含用户态就不能共享缓存：按 cookie 分桶（匿名桶）缓存，登录用户不缓存或边缘拆分。
- 静态壳 + 动态洞：静态部分（含 payload 静态段）缓存，个性化段客户端补拉——PPR 思路。
- revalidate 联动：action 变更后 purge 对应路径的 payload 缓存（Next 的 on-demand revalidation）。
- 监控：payload 缓存命中率与「个性化段占比」，命中率骤降通常是 payload 混入用户态字段。
- 口诀：payload 当 HTML 一样对待缓存策略——公私有分离。
