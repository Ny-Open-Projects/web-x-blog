---
title: [NODE-590] Node 服务的活动配置平台（活动生命周期管理）如何建设？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-590：活动配置平台
**答**:
- 活动生命周期：创建（模板选择——营销组件库对应的配置模板 ARC-611 前端沉淀的后端配合）→ 配置（规则/奖品/预算/人群/时间——配置 schema 校验）→ 预览验证（配置试算： dry-run 模拟中奖/预算消耗）→ 上线（定时/手动——状态机）→ 运行监控（成本/参与/异常告警）→ 结束（数据归档）。
- 配置安全：配置评审（涉资活动双人确认——高危变更 NODE-478）、配置校验（规则合法性：概率和=1/预算充足/时间不冲突——发布前校验拦截）、误配置防护（预热检查：上线前自动预演）。
- 灰度与紧急控制：活动灰度（部分人群先行）、紧急停止（一键停发——熔断开关 + 已发放处理策略）、配置热更（规则微调不重启——NODE-388）。
- 数据闭环：活动效果数据（参与/转化/成本——看板）、复盘归档（活动配置快照——同类活动复用）。
- 平台价值度量：新活动上线耗时（配置化前后的对比）、配置差错率。
```javascript
// 活动上线校验
async function launch(campaignId) {
  const cfg = await loadConfig(campaignId);
  validate(cfg, { probSum: 1, budget: sufficient, timeConflict: checkCalendar,
    stockLinked: cfg.prizes });                                  // 发布前校验
  await dryRun(cfg, { sample: 1000 });                           // 配置试演
  await reviewApprove(cfg, { dual: cfg.involvesMoney });         // 涉资双人
  schedule(cfg);                                                 // 状态机上线
}
```
