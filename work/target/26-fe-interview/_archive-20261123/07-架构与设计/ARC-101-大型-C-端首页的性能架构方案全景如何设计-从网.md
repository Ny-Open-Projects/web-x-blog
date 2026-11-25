---
title: [ARC-101] 大型 C 端首页的性能架构方案全景如何设计（从网络到渲染分层）？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-101：大型 C 端首页的性能架构方案全景如何设计（从网络到渲染分层）？
**答**：
- 分四层设计：网络层（CDN、HTTP/2、预连接、TLS 优化）→ 资源层（分包、代码分割、图片协议）→ 渲染层（SSR/流式、骨架屏、关键 CSS 内联）→ 数据层（BFF 聚合、边缘缓存、降级兜底）。
- 先定性能预算再谈优化：预算写进 CI 卡口（LCP < 2.5s、JS < 300KB gzip），不是事后补救。
- 度量闭环：RUM 真实用户监控按"机型×地域×版本"分维度看 P75，实验室数据只做回归参考。
- 架构上留降级路径：任何一层失效都能退回上一层的可用形态（SSR 挂了退 CSR，接口挂了退缓存快照）。

```yaml
# 首页性能预算与分层架构配置（CI 卡口消费）
performance_budget:
  metrics:
    LCP:  { p75: 2500, hard_limit: 3000 }   # ms，超 hard_limit 阻塞发布
    INP:  { p75: 200,  hard_limit: 300 }
    CLS:  { p75: 0.1,  hard_limit: 0.15 }
  resources:
    js_total_gzip:  300KB     # 含所有首屏 chunk
    css_critical:   14KB      # 关键 CSS 内联上限
    image_lcp:      150KB     # LCP 图片压缩后上限
layers:
  network: { cdn: multi-region, preload: [dns-prefetch, preconnect], protocol: h2 }
  render:  { mode: ssr-streaming, fallback: csr, skeleton: inline-css }
  data:    { bff_aggregate: true, edge_cache_ttl: 60s, degrade: static-snapshot }
enforcement:                  # 卡口动作
  - Lighthouse CI 每次发布前跑，预算超标阻断
  - RUM 周报按维度下钻，连续两周劣化触发专项
```
