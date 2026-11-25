---
title: [NODE-879] 笔试题——实现发布窗口校验执行器（窗口+封网+豁免）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-879：手写窗口校验

**需求与边界**：
- 需求：发布窗口校验（SCN-OPS-258/322）——① 窗口规则（工作日 14-17 时——SCN-OPS-322）；② 封网期（SCN-OPS-880 大促封网）；③ hotfix 豁免（升级审批——SCN-OPS-322）；④ 并发发布上限（SCN-OPS-322）。
- 边界：① 时区（目标地域本地——SCN-联想-831）；② 节假日日历（SCN-OPS-322 节前）；③ 校验记录审计（SCN-OPS-220）。

**答**：
```javascript
async function releaseWindowCheck(plan) {
  if (plan.hotfix && plan.waiver)                      // hotfix 豁免（SCN-OPS-322）
    return audit({ bypass: 'HOTFIX', plan: plan.id }) ?? { allowed: true };
  const local = toLocalTime(plan.window, plan.region); // 时区（SCN-联想-831）
  if (freezeCalendar.isFrozen(local)) return { blocked: 'FREEZE' };   // 封网（SCN-OPS-880）
  if (holidayCalendar.daysTo(local) <= 2) return { blocked: 'PRE_HOLIDAY' };
  const wd = local.getDay(), hr = local.getHours();
  if (wd === 0 || wd === 6 || wd === 5 && hr >= 12 || hr < 14 || hr >= 17)
    return { blocked: 'OUT_OF_WINDOW', note: '周五下午/节假日禁发（SCN-OPS-258）' };
  const concurrent = await concurrentReleases(plan.region);   // 并发上限（SCN-OPS-322）
  if (concurrent >= 2) return { blocked: 'CONCURRENT', note: `已有 ${concurrent} 个发布` };
  audit({ plan: plan.id, window: 'allowed' });
  return { allowed: true };
}
```

**评分点**:
- 窗口规则 + 封网 + 节前（SCN-OPS-258/322）。
- hotfix 豁免审计（SCN-OPS-229/220）。
- 并发上限（SCN-OPS-322）。
- 时区感知（SCN-联想-831）。
