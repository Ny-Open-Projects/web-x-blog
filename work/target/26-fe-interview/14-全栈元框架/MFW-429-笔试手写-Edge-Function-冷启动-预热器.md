---
title: [MFM-429→MFM→MFW-429] 笔试：手写边缘函数冷启动预热器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-429：MFM→429：冷启动预热器
**答**：实现 `createWarmer({ routes, intervalMin = 4, concurrency = 2 } = {})`：1) 按 RUM 热度排序预热（Top 路由每 region 探针请求——isolate 保活防回收；低频路由不值得烧——Top N 外放弃）；2) 预热请求打「影子路径」（`/__warm/r?hash`——命中跳过业务逻辑只激活模块图与连接，真实用户不重复计费）；3) 失败退避（某 region 连续失败 → 该 region 停 10min——预取不掩盖真实故障）；4) 度量：预热后首用户 TTFB 对比（cold/warm 差值——ROI 报告）；5.  与自动扩缩解耦（预热是体验优化不背容量责任）。

```javascript
export function createEdgeWarmer(manifest, rum) {
  const hot = rankByRUM(rum).slice(0, 30)                   // Top30 才值得
  async function tick(region) {
    for (const r of batchOf(2, hot)) {
      if (backoff.has(region)) continue                     // region 级退避
      const t0 = now()
      const r2 = await get(`https://${regionHost(region)}/__warm/${sig(route(r))}`)
      if (!r.ok) { backoff.set(region, now() + 600_000); continue }   // 不掩盖真故障
      coldP50.record(route(r), now() - t0)                  // cold/warm 差值=ROI
    }
  }
  setInterval(() => regions.forEach(theRegion), 4 * 60_000)
  return { kick: warmNowAllRegions, report: () => ({ savings: p50Diff() }) }
}
```
**评分点**：
- 热度驱动 TopN（全站预热=烧钱无底洞——RUM 排序）
- 影子路径（业务零副作用+不计费——预热与真实流量分离）
- region 级退避（连续失败停手——预取不掩盖真故障，告警另走）
- ROI 度量（cold/warm TTFB 差值——优化可量化）
