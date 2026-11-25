---
title: [NODE-880] 笔试题——实现封网期紧急发布通道（升级审批+灰度强制）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-880：手写紧急通道

**需求与边界**：
- 需求：封网紧急通道（SCN-OPS-880）——① 升级审批（双人+值班经理——SCN-OPS-253）；② 强制灰度（紧急发布也走 canary——SCN-OPS-204 准入）；③ 时间窗豁免记录（审计——SCN-OPS-220）；④ 封网期的通道滥用监控（紧急通道频率——滥用告警）。
- 边界：① 紧急的判定标准（P0 资损/可用性——SCN-OPS-229 分级）；② 紧急发布的缩短流程（跳过软门禁——硬门禁保留，SCN-OPS-229）；③ 事后补审（SCN-OPS-227 复盘）。

**答**：
```javascript
async function emergencyRelease(plan) {
  if (!freezeCalendar.isFrozen(plan.window)) return normalRelease(plan);   // 非封网走常规
  if (!isEmergency(plan)) return { blocked: 'FREEZE' };   // 非紧急：拒绝（SCN-OPS-229 分级）
  const approvals = await requireApprovals(['owner', 'platform', 'oncall-mgr']);   // 双人+值班（SCN-OPS-253）
  const gates = hardGatesOnly(plan);                   // 硬门禁保留（软门禁跳过——SCN-OPS-229）
  const result = await executeWithGray(plan, { gates, canary: 'mandatory' });   // 强制灰度（SCN-OPS-204）
  audit({ emergency: true, approvals, gatesSkipped: plan.skippedSoft });   // 审计（SCN-OPS-220）
  schedulePostReview(plan);                            // 事后补审（SCN-OPS-227）
  emergencyChannelStats.track();                       // 滥用监控（频率告警）
  return result;
}
```

**评分点**:
- 升级审批（双人+值班——SCN-OPS-253）。
- 强制灰度（紧急也走 canary——SCN-OPS-204）。
- 硬门禁保留软门禁跳过（SCN-OPS-229 分级）。
- 事后补审 + 滥用监控（SCN-OPS-227）。
