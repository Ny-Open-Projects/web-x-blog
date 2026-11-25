---
title: [SCN-711] SLA 看板的实时性怎么保证？哪些视图要实时哪些可以延迟？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-711：看板实时性怎么保证？
**答**：
- 分级实时：值班核心指标（burn rate/活跃告警）准实时（30s 刷新或推送）；趋势图分钟级；周报/报表离线层（小时级重算）——分级是因为实时聚合成本随精度指数上升。
- 增量刷新：推送只带「变更的指标」，前端 patch 更新（不整板刷新）；多 tab 打开时共享一个数据连接（BroadcastController + SharedWorker）。
- 数据新鲜度标注：每个面板显示「数据截至 xx:xx + 延迟 xx s」，延迟超阈值面板变灰——防止把 5 分钟前的数据当实时。
- 断流降级：推送断开时退化为轮询并标黄提示。
- 追问钩子：为什么不用 WebSocket 全实时推送——看板多数面板 30s~1min 更新足够，全实时推送的连接与服务端聚合成本不划算，按需分级。

```javascript
const REFRESH_POLICY = {
  burnRate: { mode: 'push', maxAge: 30_000 },
  trend: { mode: 'push', maxAge: 60_000 },
  weekly: { mode: 'pull', ttl: 3600_000 },
};
function usePanel(metricKey) {
  const { data, ts } = useBoardData(metricKey);      // 共享连接（SharedWorker）
  const stale = Date.now() - ts > REFRESH_POLICY[key].maxAge * 3;
  return { data, staleText: `截至 ${fmt(ts)}${stale ? '（延迟）' : ''}`, stale };
}
```
