---
title: [NODE-320] trace 深水区：告警与 oncall 闭环？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-320：trace 深水区：告警与 oncall 闭环？
**答**:
- 告警内容自足：告警消息附"当下可直接行动的信息"——慢 trace 样例链接、错误日志检索链接、最近变更 diff——oncall 不用从零找线索。
- 告警分级与降噪：P0 呼叫/P1 群播；同 route 同错误 5 分钟收敛一条（DP-264 聚合同款）。
- 闭环度量：告警 MTTR、误报率、告警后转化的修复任务——告警体系自身的 SLO。
- 演练：每月模拟一次告警（chaos 注入慢下游），验证样例 trace 与链接真实可用。

```javascript
// 告警消息组装（平台侧）
function buildAlert(rule, metrics) {
  return {
    level: rule.level,
    summary: `${rule.metric} 超阈值：${metrics.value}（基线 ${metrics.baseline}）`,
    links: {
      traces: traceUrl({ route: metrics.route, minDuration: 2000, since: '15m' }),
      logs: logUrl({ route: metrics.route, level: 'error', since: '15m' }),
      changes: releaseUrl({ service: rule.service, since: '1h' }),
    },
  };
}
```
