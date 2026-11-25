---
title: [NODE-430] 值班告警与 IM 机器人（告警即入口）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-430：值班告警与 IM 机器人
**答**:
- 告警消息结构化： severity/服务/现象摘要/关键指标快照/runbook 链接/认领与静默按钮（消息即操作入口——值班在 IM 里认领/升级/静默，不用切平台）。
- 机器人能力：告警推送（分级路由到值班群/个人）、快捷操作（认领/转派/静默 30min，带权限校验与审计）、轻查询（"查 order-svc P99"“最近发布”自然语言或指令）、故障快报（自动聚合相关告警为单条事故通报，防刷屏 NODE-404 收敛）。
- 状态闭环：认领状态公开（谁在处理）、处理进展追加（时间线在消息串跟帖）、恢复自动播报（MTTR 自动计算进复盘数据）。
- 防疲劳设计：同源告警合并（指纹聚合后推送）、非值班时段静默策略（P0 例外）、每日告警摘要（低优先级不发即时消息）。
- 安全：机器人操作的权限模型（只有值班可认领/静默，操作留审计日志）。
```javascript
// IM 机器人告警卡片
function alertCard(a) {
  return {
    title: `[${a.severity}] ${a.svc}: ${a.summary}`,
    fields: { p99: a.p99, errRate: a.errRate, release: a.lastRelease },
    actions: [
      { label: '认领', cmd: `ack ${a.id}`, perm: 'oncall' },
      { label: '静默 30m', cmd: `silence ${a.id} 30m` },
      { label: 'Runbook', url: a.runbook }
    ]
  };
}
```
