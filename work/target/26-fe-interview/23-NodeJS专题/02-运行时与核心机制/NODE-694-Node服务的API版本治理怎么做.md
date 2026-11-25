---
title: [NODE-694] API 版本治理怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-694：API 版本治理怎么做？
**答**：
- 版本策略：路径版本（/v1/——直观显式）vs header 版本（Accept——URL 干净）vs 参数版本（?v=2——调试友好）；主流路径版本（缓存友好 + 直观，SCN-BLD-218 条件导出联动）。
- 版本生命周期：新版本发布（兼容期双版本——SCN-OPS-245 通知 ack）→ 流量迁移（消费方升级监控）→ 旧版本废弃（deprecated 响应头 + 日志统计还有谁在用 → 下线）。
- 兼容规则：同版本内只做加法（新增字段可选）——字段语义不变；breaking 进新版本。
- 废弃通知：响应头 Deprecation/Sunset（RFC 标准——客户端可感知）+ 消费方统计（哪些请求还在打旧版本——精准催升级）。
- 追问钩子：为什么「旧版本下线」要基于「消费方统计」而不是「时间到了就删」——时间制下线会打断未升级的消费方（他们的升级周期不可控）；响应头 deprecated + 旧版本请求日志统计，精准识别「还有谁在用」→ 定向催升级 → 流量归零才下线——废弃是数据驱动的迁移，不是日历驱动的强断。

```javascript
// 双版本并存
app.use('/v1', v1Router);                              // 旧版本（兼容期）
app.use('/v2', v2Router);
// deprecated 标注
v1Router.use((req, res, next) => {
  res.setHeader('Deprecation', 'true');
  res.setHeader('Sunset', 'Sat, 01 Jan 2027 00:00:00 GMT');
  oldVersionHits.increment(routeKey(req));             // 消费方统计
  next();
});
```
