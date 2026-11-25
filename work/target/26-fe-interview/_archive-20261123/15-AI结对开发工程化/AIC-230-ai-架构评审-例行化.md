---
title: [AIC-230] 架构评审如何例行化到日常流程（不是一次性大评审）？AI 在其中扮演什么角色？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-230：架构评审如何例行化到日常流程（不是一次性大评审）？AI 在其中扮演什么角色？
**答**：
- 把架构检查嵌入 PR 流程：每个 PR 做 AI 预审，累计形成架构健康度趋势。
- 月度汇总：AI 汇总当月所有高危发现，输出「架构漂移月报」，人类只看趋势与例外。
- 重点看「累积效应」：单 PR 都合理，合起来却让模块边界糊掉——AI 擅长跨 PR 归纳。
- 触发式深审：漂移指标（耦合度、重复度）超阈值才启动专项评审。

```javascript
// 架构漂移月报（跨 PR 归纳）
async function driftReport(prs: PR[]) {
  const findings = await Promise.all(prs.map(p => preReview(p)));
  const trend = await llm(`汇总本月高危发现，识别跨 PR 的累积模式：
${findings.map(f => JSON.stringify(f.high)).join('\n')}
输出：漂移趋势、模块健康分变化、建议专项评审清单。`);
  return trend;
}
r
```
