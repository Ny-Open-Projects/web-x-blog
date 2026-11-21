---
title: [R19-311] RSC 应用怎么做 A/B 实验（服务端分流与边缘分流）？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-311：RSC 应用怎么做 A/B 实验？
**答**：
- 服务端分流：middleware（Next）按 userId hash 写实验分组 cookie，RSC 按分组渲染变体——payload 里只含所分配变体，无闪烁。
- 边缘分流：CDN/边缘函数按 cookie 或 header 分流到不同缓存桶——需控制缓存 key 维度。
- 客户端兜底：脚本实验（SDK 渲染后切换）会闪烁且污染 payload——RSC 场景优先服务端分流。
- 数据：实验曝光埋点带分组号，指标看板按分组对比（转化/INP）。
- 注意：实验变体影响缓存命中率（key 增加分组维度），实验结束及时清理路由规则。
