---
title: [OPT-026] CDN 与缓存命中率如何实战调优？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-026：CDN 与缓存命中率如何实战调优？

**答**：
- 命中率公式：命中率 = 边缘节点直接响应的比例；未命中就要回源，回源慢则用户直接买单。
- 提升手段一：**稳定且唯一的缓存 key**——URL 带 content hash（`app.a3f9c2.js`）+ `Cache-Control: immutable, max-age=31536000`；HTML 不带指纹则用短 `s-maxage` + 主动刷新。
- 提升手段二：URL 规范化——统一 query 顺序、剔除时间戳等无意义参数，避免"同一个文件因参数不同而缓存多份"。
- 提升手段三：预热（发布前推送到边缘）+ 回源合并（多个边缘同时回源只打源站一次）；用响应头 `X-Cache: HIT/MISS` 监控命中率。

```javascript
// 一一对应：统计真实用户 CDN 命中率的采集脚本
// 利用 PerformanceResourceTiming + 响应头标记统计 HIT/MISS
function collectCacheHitRatio() {
  const entries = performance.getEntriesByType('resource')
    .filter((e) => e.name.includes('cdn.example.com'));

  const stats = { hit: 0, miss: 0 };
  entries.forEach((e) => {
    // nextHopProtocol 可区分边缘命中（h2/h3 直连边缘）与回源延迟
    // 多数 CDN 会注入自定义响应头，这里演示通过 Performance API 估算
    const fromEdge = e.nextHopProtocol.startsWith('h');
    if (e.transferSize === 0 && fromEdge) stats.hit++;  // 0 传输量多为缓存命中/304
    else stats.miss++;
  });

  // 上报到监控系统（09 章的上报通道）
  navigator.sendBeacon('/collect/cache-ratio', JSON.stringify(stats));
}
window.addEventListener('load', () => setTimeout(collectCacheHitRatio, 3000));
```

## 五、SSR、SSG 与 PWA 离线
