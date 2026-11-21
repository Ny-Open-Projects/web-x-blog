---
title: Redis 缓存优化与 QPS 压测验证
date: 2026-11-17
categories: [课程, 低代码]
tags: [25-lowcode, 原理, Redis, 性能, JMeter]
---

## Redis 缓存优化与 QPS 压测验证

原理：高频读接口每次请求都走 MySQL 查询+组装，把结果缓存进 Redis（TTL 过期），命中直接返回，把数据库压力挡在缓存层。

**本项目实例**（`getCachedData` 通用封装）：

```ts
getCachedData(cacheKey, callback, { ttl, force }) {
  // 命中直接返回；未命中执行 callback 查库并 set 回填
  // force=true 时把已读到的缓存置空再回源覆盖写回（并非显式 del）
}
```

callback 内用 `Promise.all` 并发查表 + `filter` 筛空值组装 components/id 数组。优化不改业务查询本身，可推广到任意接口。

**压测验证**（JMeter 30-6）：口径一致（清空报告/禁用其他取样器/固定线程数）下实测有缓存 QPS 约 428~440，无缓存约 410——提升有限但稳定，因为该接口查询本身不重。这 teaches 一个真话：**缓存收益取决于原查询成本，压测数据说话而不是拍脑袋**。

方法论：低线程起步逐步加压（1→50→100→200），以「异常%=0 且吞吐量最大」定位最优 TPS。

出处「课程25 · 30-6、29-1」
