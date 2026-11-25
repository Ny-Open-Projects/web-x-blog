---
title: [WCN-809] 多时区跨地区团队如何协同维护一套 WC 平台？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-809：多时区跨地区团队如何协同维护一套 WC 平台？

**答**：
- 结论先行：跨时区协同的本质是「用文档和自动化替代同步沟通」——把决策写进 ADR、把规则写进 CI、把状态写进看板，让交接不需要开会。
- 异步优先：所有设计决策落 ADR（背景/选项/结论/影响），代码审查用详细 PR 模板，避免依赖实时会议；重大变更设「24 小时异议期」给其他时区反应时间。
- 交接班机制：用轮值 owner + 交接文档（当日变更、待决事项、线上告警状态），保证任何时刻都有人能接手线上问题。
- 自动化兜底：CI 强制契约/a11y/体积门禁，让「人不在也能拦住坏变更」；监控告警按时区轮值 on-call。
- 工具与规范：统一 commit 规范、标签语义、文档站单一信息源，避免各地维护各自的「小抄」导致口径不一。
- 追问钩子：面试官会问「紧急事故半夜发生怎么办」——答：on-call 轮值 + 自动降级预案（如自动回滚 + 降级注册），把「需要人醒着」的场景压到最少。

```javascript
// 跨时区交接记录：状态可交接、决策留痕、异议期可配置
function handover({ changes, pending, alerts, region }) {
  return {
    from: region,
    timestamp: new Date().toISOString(),
    summary: [
      `变更: ${changes.join('; ') || '无'}`,
      `待决: ${pending.join('; ') || '无'}`,
      `告警: ${alerts.length ? alerts.join('; ') : '正常'}`,
    ].join('\n'),
    objectionWindowHours: 24, // 重大变更给其他时区异议时间
  };
}
console.log(handover({ changes: ['token v3 发布'], pending: ['是否弃用 ds-old'], alerts: [], region: 'CN' }));
```
