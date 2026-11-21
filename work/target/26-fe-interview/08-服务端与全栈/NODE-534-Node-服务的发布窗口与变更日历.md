---
title: [NODE-534] Node 服务的发布窗口管理（变更日历/冻结期/冲突检测）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-534：发布窗口与变更日历
**答**:
- 冻结期体系：常规冻结（大促/月末资金结算/节假日——发布平台按日历自动禁非紧急发布）、紧急例外通道（hotfix 审批后可越冻结——留痕与事后复盘 ARC-478）、冻结前的变更清仓（冻结前一周集中发布——积压到解冻反而风险集中）。
- 变更日历：全平台变更日程公开（谁在什么时候发什么——冲突可视）、同服务变更互斥（发布锁：同一服务同时只允许一个变更——防叠加事故 NODE-478）、依赖顺序调度（协议变更 → 依赖方变更的先后约束自动检查 NODE-164 服务端版）。
- 冲突检测自动化：发布申请时自动检查（日历冲突/服务锁/依赖顺序/容量窗口——不满足阻断并提示）。
- 窗口选择策略：业务低峰发布（凌晨窗口——变更影响最小）、灰度启动时间（保证灰度观测窗口在有人值守时段——晚上 10 点后不启动新灰度）。
- 度量：冻结期违规数（应趋零）、变更冲突拦截次数（机制在工作的证据）、发布窗口外变更占比。
```javascript
// 发布申请校验
async function requestRelease(req) {
  const checks = [ freezeCalendar(req.time), serviceLock(req.svc),
                   depOrder(req.changes), capacityWindow(req.time) ];
  const blocked = (await Promise.all(checks)).filter(r => !r.ok);
  if (blocked.length && req.type !== 'hotfix')
    throw new ReleaseBlocked(blocked);                            // 冻结/冲突阻断（hotfix 走审批）
}
```
