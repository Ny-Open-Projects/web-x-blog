---
title: [ARC-240] RBAC 与前端监控的结合：权限异常如何被监控发现？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-240：RBAC 与前端监控的结合：权限异常如何被监控发现？
**答**：
- 权限异常三类：快照服务故障（拉取失败率）、判定引擎 bug（渲染出无权内容）、数据漂移（菜单与路由不一致）。
- 监控指标：perm-snapshot 失败率/延迟 P90、403 率（分页面/分权限码）、热更延迟（变更到生效时长）、一致性问题（手输 URL 被 403 的占比——过高说明菜单口径错了）。
- 告警规则示例：某权限码 403 率突增 → 可能是权限中心误回收，优先级高；某页面快照就绪 P90 > 2s → 加到性能看板。
- 复盘闭环：权限相关故障单自动关联"当时的快照版本与变更记录"，缩短归因。

```typescript
// 指标上报埋点
const permMetrics = {
  snapshotReady: (ms, ok) => perf.report('perm-ready', { ms, ok }),      // 就绪时延
  denied: (code, page) => metric.inc('perm-403', { code, page }),        // 403 率
  hotLatency: (ms) => perf.report('perm-hot-update', { ms }),            // 变更→生效
};
// Dashboard 聚合：
// - perm-403{code="order:audit"} 突增 5x @ 5min → 告警到权限中心 owner
// - perm-ready p90 > 2000ms → 性能看板 + 优化任务
```
