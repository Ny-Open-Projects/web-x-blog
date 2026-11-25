---
title: [SCN-719] SLA 看板的多环境（生产/预发/演练）数据隔离怎么做？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-719：多环境数据隔离怎么做？
**答**：
- 环境维度强制：所有 SLI 带环境标签（env），看板查询强制 env 过滤——混入演练/压测数据是 SLA 看板最常见的事故（压测流量把 P95 打爆，误告警）。
- 压测标识：压测流量全链路打标（header + SDK 识别），采集侧丢弃或单独存储；演练期间演练环境单独视图。
- 防误看：看板环境切换器显式高亮当前环境；默认生产，切走时有确认提示；生产视图若混入非生产数据（对账任务检测）告警。
- 演练视图价值：故障演练（SCN-OPS）的演练环境数据单独存，用于验证告警链路而非计入 SLA。
- 追问钩子：为什么不让 SDK 自动判环境——SDK 判定（域名/特征）不可靠且易绕过，采集入口强制要求显式 env 标识 + 网关二次校验。

```javascript
// 采集入口校验
app.post('/rum/sli', (req, res) => {
  const env = req.body.dims.env;
  if (!ENVS.includes(env)) return res.status(400).json({ code: 'BAD_ENV' });
  if (env !== 'prod' && looksLikeProdSLI(req.body))
    return res.status(403).json({ code: 'ENV_MISMATCH' });   // 非 prod 却带生产特征：拒绝
  store.write(env, req.body);
  res.ok();
});
// 压测流量识别
const isLoadTest = (req) => req.headers['x-loadtest'] === '1' || MARKER_IPS.has(req.ip);
```
