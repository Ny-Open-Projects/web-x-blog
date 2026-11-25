---
title: [NODE-780] 笔试题——实现 API 版本路由与废弃统计（Sunset 流量归零）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-780：手写版本路由

**需求与边界**：
- 需求：API 版本治理（SCN-NODE-694）——① 双版本路由（v1 deprecated/v2——并存）；② 废弃统计（旧版本消费方精确识别——按 appKey/IP 聚合）；③ Sunset 头（RFC 标准——客户端可感知）；④ 流量归零才下线（数据驱动——SCN-NODE-694）。
- 边界：① 旧版本响应缓存（deprecated 响应 no-store——防止旧响应长期驻留）；② 消费方通知（定向——SCN-OPS-245 ack）；③ 强制下线的豁免（个别消费方延期——豁免记录）。

**答**：
```javascript
const v1Stats = new Map();                             // 消费方 → 请求数
app.use('/v1', (req, res, next) => {
  res.setHeader('Deprecation', 'true');
  res.setHeader('Sunset', 'Sat, 01 Jan 2027 00:00:00 GMT');
  res.setHeader('Link', '</v2/docs>; rel="deprecation"');
  const consumer = req.headers['x-app-key'] ?? req.ip;   // 消费方识别
  v1Stats.set(consumer, (v1Stats.get(consumer) ?? 0) + 1);   // 精确统计（SCN-NODE-694）
  next();
}, v1Router);
// 下线决策（数据驱动）
function canSunset() {
  const active = [...v1Stats.entries()].filter(([k, n]) => n > 0 && withinDays(k, 30));
  return { ready: active.length === 0,
    blockers: active.map(([k]) => k),                  // 还有谁在用——定向催升级（SCN-OPS-245）
    note: '流量归零才下线——时间制强断会打断未升级方' };
}
```

**评分点**:
- Sunset/Deprecation 标准头（客户端可感知——SCN-NODE-694）。
- 消费方精确统计（appKey/IP 聚合——定向催升级）。
- 流量归零才下线（数据驱动——非日历强断）。
- 旧版本 no-store（废弃响应不驻留缓存）。
