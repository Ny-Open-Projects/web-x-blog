---
title: [NODE-525] Node 服务的请求合并（网关层 dedup/coalesce）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-525：网关层请求合并
**答**:
- 合并场景：热点请求合并（同一资源 N 个并发请求 → 一个回源，NODE-378 singleflight 网关版）、时间窗合并（微窗口 5~20ms 内同请求攒批——用响应延迟换回源量，适合容忍微延迟的读接口）、前端批合并（前端把 N 个小请求合并成 1 个批量——协议层面 BFF 提供 batch 端点 NODE-483）。
- 合并策略配置：按接口声明（可合并性/窗口大小/最大批量——幂等读默认可合并，写接口不可合并除幂等键）、合并条件（参数完全一致才合并——规范化 key）。
- 与缓存协同：合并 = 缓存 miss 时的回源去重（缓存层内置 singleflight NODE-353）——合并率是缓存体系健康指标。
- 风险控制：合并导致的延迟（等待窗口——按接口敏感度配置）、等待者错误传播（回源失败 → 所有等待者同错——各等待者可有独立降级策略）、内存上限（等待队列上限——防极端堆积）。
- 观测：合并率（每接口：等待者数/回源数——热点识别）、合并节省的回源量（成本收益证据）。
```javascript
// 网关合并器
const coalescer = new Map();
async function withCoalesce(key, fn, { window = 10 } = {}) {
  const pending = coalescer.get(key);
  if (pending) return pending;                                   // 共享回源
  const p = delay(window).then(fn).finally(() => coalescer.delete(key)); // 微窗口攒批
  coalescer.set(key, p);
  return p;
}
```
