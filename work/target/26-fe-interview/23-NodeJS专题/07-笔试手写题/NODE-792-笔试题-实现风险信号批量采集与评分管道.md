---
title: [NODE-792] 笔试题——实现风险信号采集与评分管道（批量/脱敏/降级）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-792：手写风控管道

**需求与边界**：
- 需求：风控信号管道（SCN-联想-556/563）——① 信号批量接收（服务端聚合——SCN-联想-592 批量上报对端）；② 信号 schema 校验与脱敏（白名单——SCN-联想-584）；③ 评分异步管道（同步规则 + 异步模型——SCN-NODE-686）；④ 降级（模型服务挂 → 规则兜底——SCN-NODE-669）。
- 边界：① 信号字段白名单（未注册拒绝——fail-closed，SCN-联想-584）；② 批量去重（seq + sid——SCN-联想-592）；③ 评分结果缓存（同用户短 TTL——重复请求秒回）。

**答**：
```javascript
app.post('/risk/signals', bulkLimit(), async (req, res) => {
  const signals = req.body.events.filter(e => COLLECT_SCHEMA[e.type]);   // 白名单（SCN-联想-584）
  const deduped = dedupBySidSeq(signals);              // 去重（SCN-联想-592）
  const clean = cleanSignals(deduped);                 // 脱敏（SCN-NODE-698）
  await mq.publish('risk.signals', batch(clean));      // 异步评分管道
  const syncVerdict = syncRules(clean);                // 同步规则先行（SCN-NODE-686）
  res.json({ verdict: syncVerdict });                  // 同步响应
});
consumer.on('risk.signals', async (batch) => {
  let scores;
  try { scores = await modelScore(batch, { timeout: 500 }); }
  catch { scores = fallbackScores(batch); }            // 模型挂 → 规则兜底（SCN-NODE-669）
  await persistScores(scores);                         // 评分落库（后续请求查询）
});
```

**评分点**:
- 白名单 fail-closed（未注册信号拒绝——SCN-联想-584）。
- 同步规则 + 异步模型双层（SCN-NODE-686 分工）。
- 模型降级规则兜底（SCN-NODE-669 熔断配套）。
- 批量去重 + 脱敏（SCN-联想-592/698 联动）。
