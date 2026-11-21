---
title: [NODE-100] 综合案例：一次 TTFB 从 1.8s 到 200ms 的全链路优化？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-100：综合案例：一次 TTFB 从 1.8s 到 200ms 的全链路优化？
**答**：
- 现象：首页 SSR 接口 TTFB P75 1.8s。定位（Server-Timing 分解）：数据聚合 1.2s（3 个下游**串行**请求 + 1 个未命中缓存）→ 渲染 0.3s（组件树过大）→ 网络与排队 0.3s（实例 CPU 高、事件循环 lag 高）。
- 优化四板斧：① **串行改并行** + 批量接口合并（N+1 → 1 次 IN 查询）；② **多级缓存**：整页缓存匿名流量（s-maxage=60）+ Redis 缓存聚合结果（命中率 85%）；③ **流式渲染**：骨架先发，慢块 Suspense 包裹；④ **容量**：事件循环 lag 定位到大 JSON 序列化（NODE-085 案例二同因），流式透传 + 扩容。
- 收益复核：聚合 1.2s → 180ms（并行+缓存命中），渲染 0.3s → 80ms（流式首字节），TTFB P75 200ms，P99 450ms。
- 方法论沉淀：**先测量后优化**（Server-Timing/火焰图定位），优化后必须复压测验证并固化基线（CI 性能门禁）。

```javascript
// 优化前：串行 + 无缓存（1.2s 聚合）
// const user = await fetchJSON(USER_API);        // 300ms
// const feed = await fetchJSON(FEED_API);        // 500ms
// const ads = await fetchJSON(ADS_API);          // 400ms  → 串行合计 1.2s

// 优化后：并行 + 整页缓存 + 流式
app.get('/home', async (req, res) => {
  const isAnonymous = !req.cookies.sid;

  // 1. 匿名流量：CDN/边缘缓存整页（优化点三：绝大多数请求不再回源）
  if (isAnonymous) {
    res.setHeader('cache-control', 'public, s-maxage=60, stale-while-revalidate=300');
  } else {
    res.setHeader('cache-control', 'private, max-age=0');
  }

  // 2. 并行聚合 + 批量合并（优化点一：1.2s → 180ms）
  const [user, feed, ads] = await Promise.all([
    user ? fetchJSON(`${USER_API}/me`) : Promise.resolve(null),        // 并行
    cachedLoader(`feed:${user?.uid ?? 0}`, () => fetchJSON(`${FEED_API}/batch?ids=hot,new`), 120),  // 批量接口 + Redis 缓存
    cachedLoader('ads:home', () => fetchJSON(`${ADS_API}/banners`), 300),
  ]);

  // 3. 流式渲染：骨架先发（优化点二：TTFB 前移）
  const stream = renderToPipeableStream(<Home user={user} feed={feed} ads={ads} />, {
    onShellReady() {
      res.setHeader('server-timing',
        `agg;dur=${aggCost}, render;dur=${renderStart() - aggStart}`);
      stream.pipe(res);
    },
  });
});

// 4. 缓存加载器（进程内 + Redis 两级，NODE-051 精简版）
async function cachedLoader(key, loader, ttlSec) {
  const local = localLRU.get(key);
  if (local) return local;
  const remote = await redis.get(key).then((v) => v && JSON.parse(v));
  if (remote) { localLRU.set(key, remote); return remote; }
  const data = await loader();
  localLRU.set(key, data);
  await redis.setex(key, ttlSec, JSON.stringify(data));
  return data;
}

// 优化前后基线（CI 性能门禁阈值）
const BASELINE = { ttfb_p75: 200, ttfb_p99: 450, agg_cost: 180, cache_hit_rate: 0.85 };
// 每次发布跑基准压测：autocannon -c 100 -d 30 /home → 超过基线 20% 阻断合并
```

---

## 补充说明

- 本文件为 **NODE-001 ~ NODE-100**，与既有 01~18 专题（WEB/H5/CSS/JS/TS/V3/R19/ENG/PER/BAS/SCN/OPT/FRP/AGT/ALG/OPS/ARC/BLT 前缀）互不重复，专注服务端能力域。
- **NODE-101 ~ NODE-200** 为进阶篇：事件循环与框架源码级、网络协议深入、数据库与安全深入、可观测性、高并发稳定性、微服务协作、TypeScript 工程与综合体系设计，共十章。








---

## 十一、事件循环与异步源码级
