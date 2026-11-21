---
title: [NODE-598] Node 服务的灰度发布与 AB 实验的协同（共用分桶体系）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-598：灰度与 AB 协同
**答**:
- 概念区分：灰度（发布安全机制——新旧版本过渡：按比例放量观察，ARC-370）vs AB（实验机制——假设验证：多变体对照）。共用基础设施：分桶/名单/放量/监控——一套体系两个用途。
- 协同设计：分桶维度复用（灰度与实验同 uid 因子但不同层/盐——互不干扰 NODE-597）、灰度期嵌套实验（新版本灰度 5% 内跑 AB——灰度桶内再分实验桶）、紧急停用联动（灰度回滚 → 相关实验自动暂停——发布事件联动实验状态）。
- 监控协同：灰度指标（错误/性能——发布护栏 ARC-446）与实验指标（业务转化）分离呈现——不同决策不同数据。
- 流程协同：发布单与实验单关联（同一变更的灰度计划与实验计划一次评审）、实验转正 = 灰度全量（实验胜出 → 直接转灰度全量流程）。
- 治理：双系统的开关债务统一治理（灰度完成的旧版本清理 + 实验结束的分支清理——ARC-288）。
```javascript
// 协同编排
release.on('canary:5%', async (ev) => {                          // 灰度事件
  const exp = ev.linkedExperiment;
  if (exp) await experiments.startWithin(exp, { onlyIn: 'canary-buckets' }); // 灰度桶内实验
});
release.on('rollback', (ev) => experiments.pause(ev.linkedExperiment));    // 回滚联动暂停
```
