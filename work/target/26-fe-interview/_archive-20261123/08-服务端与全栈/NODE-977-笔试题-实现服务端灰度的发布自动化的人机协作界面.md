---
title: [NODE-977] 笔试题——实现发布自动化人机协作界面（建议+确认+覆盖）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-977：手写人机协作

**需求与边界**：
- 需求：人机协作（SCN-OPS-242/283）——① 自动建议（SCN-OPS-283 建议器）；② 人工确认（一键——SCN-OPS-242 便捷）；③ 人工覆盖（覆盖自动决策——SCN-OPS-242）；④ 覆盖的审计（SCN-OPS-273）。
- 边界：① 覆盖的记录（覆盖原因——SCN-OPS-273）；② 覆盖的频率监控（SCN-OPS-284 反博弈）；③ 确认的时效（SCN-OPS-210）。

**答**：
```javascript
async function humanOverride(decision, override, by) {
  const advice = await releaseAdvice(decision.context);   // 自动建议（SCN-OPS-283）
  requireRole(by, 'oncall-mgr');                       // 覆盖权限（SCN-OPS-253）
  audit({ auto: advice.advice, override: override.action,
    overrideReason: override.reason, by });            // 覆盖审计（SCN-OPS-273）
  overrideRate.track(by);                              // 频率监控（SCN-OPS-284 反博弈）
  return executeDecision(override);                    // 执行（SCN-OPS-960）
}
```

**评分点**:
- 自动建议 + 人工覆盖（SCN-OPS-283/242）。
- 覆盖权限 + 审计（SCN-OPS-253/273）。
- 覆盖频率反博弈（SCN-OPS-284）。
