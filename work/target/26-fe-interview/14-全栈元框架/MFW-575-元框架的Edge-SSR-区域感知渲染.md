---
title: [MFW-575] 元框架 Edge SSR：区域感知渲染与数据就近
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-575：Edge SSR 区域感知渲染

**答**:
- Edge SSR 的区域策略：1) **渲染就近**（edge 函数在全球节点——渲染离用户近 TTFB 小）；2) **数据就近 vs 数据集中**（DB 在主区域 us-east——edge 渲染从 us 取数据 RTT 100ms+ 抵消 edge 优势——「数据也是可复制的」：读副本区域化（Neon region replicas/PlanetScale 分区）；3) 区域感知路由（vercel edge config/env 按 region 分流数据源）。
- Next 的 region 配置：函数 region（vercel 函数部署区域）vs edge（全球）——「SSR 放哪」的决策树：数据集中 → serverless 放数据区（渲染与数据同区 RTT 最小）+ CDN 全球（HTML 缓存全球）；数据可复制 → edge 全球（渲染+数据都就近）。
- 写路径的分区：edge 只读（写回主区——写的一致性与主区 RTT）；「读全球、写集中」的 CQRS 边缘版。
- 追问钩子：为什么「edge SSR + 集中 DB」常常比「区域 serverless + 同区 DB」更慢？——edge 渲染的每个数据 fetch 都跨区（100-200ms × N 个查询——SSR 渲染 3 个查询 = 600ms 额外）；区域 serverless 与 DB 同区（查询 <5ms）——「渲染与数据的物理距离」是延迟的主导项：edge 的收益（离用户近）被数据距离吃掉——TTFB = 调度 + 数据 RTT，数据 RTT 主导时 edge 反而慢；结论：edge SSR 的前提是数据也边缘化（可复制读）。

```typescript
// 区域感知的数据源选择
// next.config: regions: ['iad1']（serverless 区）或 edge runtime
export const runtime = 'edge';
export async function GET(req: Request) {
  const region = req.headers.get('x-vercel-ip-city') ? req.cf?.country : 'us';
  const db = regionDb(region);                           // 区域副本连接
  const data = await db.query(products);                 // 就近读
  return NextResponse.json(data);
}
// 写路径：回主区
async function write(data) {
  return fetch(`${PRIMARY_REGION_URL}/api/write`, { method: 'POST', body: JSON.stringify(data) });
}
// 决策树
const deployDecision = (dataReplicable, queryCount) =>
  dataReplicable ? 'edge-global（读副本全球）'
  : queryCount > 2 ? 'region-serverless（与 DB 同区——数据 RTT 主导）'
  : 'edge-global（查询少 RTT 可接受）';
```
