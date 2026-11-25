---
title: [PER-1024] CDN 缓存的命中率怎么诊断与提升
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1024：CDN 缓存的命中率怎么诊断与提升

**答**：
- 命中率构成：请求去重（相同 URL 才命中）+ 缓存规则覆盖 + 回源质量；X-Cache/CF-Cache-Status 头直接标明 HIT/MISS/EXPIRED。
- 常见低命中原因：URL 带动态 query（时间戳/随机数）、缓存头缺失、Cookie 被计入缓存键、资源零散导致同 URL 复用率低。
- 提升手段：URL 规范化（剔除无关 query）、统一构建 hash 命名、Cache Key 配置剔除 Cookie、合并小文件减少请求数。
- 监控：按资源类型/边缘节点拆分命中率，MISS 高发节点单独排查。

```javascript
// CDN 命中率采集
function cdnHit(entry) {
  const status = entry.responseStatus;   // 无法直接读响应头时用 serverTiming
  return performance.getEntriesByType('resource')
    .filter(r => r.name.includes('cdn'))
    .map(r => ({
      url: new URL(r.name).pathname,
      hit: r.serverTiming?.find(t => t.name === 'cache')?.description ?? 'unknown',
      size: r.transferSize,
    }));
}
// 聚合输出 HIT/MISS 比例，MISS 集中的路径单独治理（去 query/补缓存头）
```
