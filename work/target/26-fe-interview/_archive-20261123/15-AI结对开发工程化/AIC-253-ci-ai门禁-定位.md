---
title: [AIC-253] AI 参与的 CI 门禁（自动评审/风险分级）应该定位为「阻塞」还是「建议」？如何演进？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-253：AI 参与的 CI 门禁（自动评审/风险分级）应该定位为「阻塞」还是「建议」？如何演进？
**答**：
- 起步阶段只做「建议」：评论式反馈不阻塞合并，先积累采纳率数据建立信任。
- 高危项（密钥泄露、危险 API、依赖风险）可先行阻塞——误报率低且后果重的项。
- 演进路径：建议→白名单内阻塞→全面阻塞，每一步都要有误报率数据支撑（< 5%）。
- 防止「狼来了」：采纳率跌破阈值自动降级回建议模式并告警。

```javascript
const gatePolicy = {
  phase1: { mode: 'comment', metrics: ['adoptionRate'] },
  phase2: { mode: 'block', only: ['secret-leak', 'dep-vuln', 'dangerous-api'], maxFp: 0.05 },
  phase3: { mode: 'block-all' },
  autoDowngrade: 'adoptionRate < 0.3 持续两周 → 降回 comment 并告警',
};
r
```
