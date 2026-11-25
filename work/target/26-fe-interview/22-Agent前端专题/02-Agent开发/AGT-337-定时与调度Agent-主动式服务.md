---
title: [AGT-337] 定时与调度 Agent——从被动问答到主动服务？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-337：定时任务型 Agent（每日报告/监控提醒）怎么设计？

**答**:
- 触发模型：定时触发（cron：每日报告）、事件触发（条件满足：价格低于 X 时通知）、状态触发（连续 N 次异常升级）——主动 Agent 的核心是"触发器+轻量检查+按需深度执行"：触发后先便宜检查（规则/小模型），确认值得深度分析才调用 LLM。
- 输出治理：主动推送的打扰控制——价值过滤（没有新信息就不推：与上次相比无变化则静默）、聚合推送（多条小事件合并一条日报）、重要性分级（紧急直达，普通进日报）——主动 Agent 的失败模式是"变成垃圾信息源"。
- 幂等与去重：重复触发防护（同一事件不重复通知）、失败重试与补跑（错过的定时任务是否补跑要有策略）。
- 用户控制：订阅管理（用户自定义触发条件与频率）、暂停开关、历史记录可查——主动权在用户。

```javascript
scheduler.register({
  cron: '0 9 * * *',
  task: async () => {
    const fresh = await cheapCheck(lastSnapshot);   // 便宜检查
    if (!fresh.changed) return;                     // 无新信息不推
    const report = await deepAnalysis(fresh);       // 深度执行
    notify(importance(report), report);
  },
});
// 事件触发：price < X && !notified → 推送（幂等键防重）。
```
