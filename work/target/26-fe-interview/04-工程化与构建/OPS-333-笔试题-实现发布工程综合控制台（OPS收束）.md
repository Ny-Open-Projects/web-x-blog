---
title: [OPS-333] 笔试题——实现发布工程综合控制台（OPS 收束）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## OPS-333：手写发布控制台（OPS 收束）

**需求与边界**：
- 需求：整合 OPS 系列能力的综合控制台数据层——① 发布计划（风险分级/审批流/RACI）、② 灰度状态机（档位/哨兵/熔断）、③ 应急通道（回滚决策树/熔断）、④ 治理面板（机制健康度/审计/SLO 预算）、⑤ 通知路由——单一入口聚合。
- 边界：① 各子模块复用前文实现（引用编号）；② 控制台只做编排不做决策（决策在各子模块）；③ 状态一致性（控制台读各模块的单一事实源）。

**答**：
```javascript
function releaseConsole(planId) {
  const plan = planStore.get(planId);                  // SCN-OPS-291 解析器
  return {
    plan: {
      risk: riskLevel(plan),                           // OPS-297 分级
      approvals: assembleFlow(plan.level, plan),       // OPS-302 审批流
      raci: raciMatrix(plan),                          // OPS-328 责任矩阵
    },
    gray: {
      fsm: grayFSM(plan.id),                           // OPS-292 档位状态机
      srm: srmMonitor(...),                            // OPS-293 分流检测
      sentinel: releaseSentinel(plan.metric),          // OPS-295 哨兵
      verdict: hedgeVerdict(gray, stage),              // OPS-323 对冲判定
    },
    emergency: {
      decisionTree: rollbackDecisionTree,              // OPS-299 回滚决策
      break: circuitBreak,                             // OPS-222 熔断（冻结不回滚）
    },
    governance: {
      health: grayHealth(...),                         // OPS-310 机制健康度
      budget: releaseErrorBudget(...),                 // OPS-312 SLO 预算
      audit: releaseAudit(...),                        // OPS-309 审计链
    },
    notify: notifyRouter,                              // OPS-303 通知矩阵
    note: '控制台只编排，决策在子模块（单一事实源）',
  };
}
// OPS 能力地图（291~332 全链索引）
const OPS_MAP = {
  plan: ['291-parse', '297-risk', '302-approval', '328-raci'],
  gray: ['292-fsm', '293-srm', '294-flag', '295-sentinel', '323-hedge'],
  emergency: ['299-tree', '322-queue', '324-shadow', '326-heal'],
  governance: ['309-audit', '310-health', '312-budget', '315-rules'],
};
```

**评分点**:
- 五区聚合（计划/灰度/应急/治理/通知）全链引用前文实现。
- 控制台只编排不决策（单一事实源声明）。
- 应急通道独立区（永不排队语义）。
- OPS 能力地图收束（291~332 全链索引）。
