---
title: [OPS-285] 发布系统自身的 SLO 怎么定义？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## OPS-285：发布系统 SLO 怎么定义？
**答**：
- SLO 维度：发布系统是关键基础设施——可用性（编排器/flag 服务/哨兵可达性）、时效（发布流水线 P95 时长/回滚 P95）、正确性（产物完整性/分流正确性/留痕完整性）——每个维度有明确 SLO 与错误预算。
- 错误预算的行为：发布系统预算烧完（发布故障频发）→ 冻结新功能开发（发布系统自身进入稳定模式，SCN-SLA-722 机制自用）。
- SLO 面向用户：发布系统的用户是「发布工程师与值班」——SLO 定义要覆盖他们的核心痛点（排队时长/失败重试成本）。
- SLO 度量自动化：SLO 指标从系统遥测自动计算（SCN-OPS-207 事件流）——手工统计的 SLO 必然失真。
- 追问钩子：为什么发布系统要「用错误预算治理自己」——发布系统故障会阻塞全团队交付（爆炸半径最大的基础设施）；错误预算机制让「发布系统自身的稳定性投入」有量化触发（预算烧完即冻结功能开发）——用自己治理别人的机制治理自己，是最有说服力的体系示范。

```javascript
const releaseSystemSLO = {
  availability: { orchestrator: 0.999, flagService: 0.9995, sentinel: 0.999 },
  latency: { pipelineP95: '20min', rollbackP95: '5min' },
  correctness: { artifactIntegrity: 1.0, splitCorrectness: 1.0, auditComplete: 1.0 },
  budget: { burn: errorBudget, action: 'burnout → freeze-features', selfApply: true },
};
```
