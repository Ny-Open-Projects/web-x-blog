---
title: [ENG-314] 笔试题——实现 ownership 健康度评估（bus factor/响应时长/积压）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## ENG-314：手写 ownership 健康度

**需求与边界**：
- 需求：按包评估所有权健康度——① bus factor（活跃 owner 数）；② PR 审批响应 P95；③ 积压（待审 PR 数/待审天数）；④ 交接风险（单一 owner 且近期贡献集中）。输出红旗清单与交接建议。
- 边界：① 活跃 owner = 近 90 天有审批记录的（注册名单会过期）；② 响应时长 = PR open 到首次 review；③ 健康分加权（bus factor 0.4/响应 0.3/积压 0.3）。

**答**：
```javascript
function ownershipHealth(packages, prs, { activeWindow = 90 } = {}) {
  const cutoff = Date.now() - activeWindow * 864e5;
  return packages.map(pkg => {
    const pkgPrs = prs.filter(p => p.packages.includes(pkg.name));
    const activeOwners = [...new Set(pkgPrs.flatMap(p => p.approvals)
      .filter(a => a.ts > cutoff).map(a => a.by))];
    const responseTimes = pkgPrs.filter(p => p.firstReviewTs)
      .map(p => p.firstReviewTs - p.openTs);
    const pending = pkgPrs.filter(p => !p.mergedTs);
    const backlogDays = pending.length
      ? avg(pending.map(p => (Date.now() - p.openTs) / 864e5)) : 0;
    const busFactor = activeOwners.length;
    const score = busFactor >= 2 ? 0.4 : busFactor === 1 ? 0.15 : 0
      + (quantile([...responseTimes].sort((a, b) => a - b), 0.95) < 2 * 864e5 ? 0.3 : 0)
      + (backlogDays < 3 ? 0.3 : 0);
    return {
      pkg: pkg.name, busFactor, responseP95d: quantile([...responseTimes].sort((a, b) => a - b), 0.95) / 864e5,
      backlogDays, score,
      red: busFactor <= 1 || backlogDays > 7,
      suggest: busFactor <= 1 ? `交接建议: 为 ${pkg.name} 培养第二 owner（双人并行审批期）` : null,
    };
  }).sort((a, b) => a.score - b.score);                // 低分置顶
}
```

**评分点**:
- 活跃 owner 用近窗审批记录（名单过期防御）。
- 三维加权（bus factor/响应/积压）+ 红旗阈值。
- 交接建议含双人并行期（ENG-206 转移流程）。
- 低分置顶输出（治理优先级）。
