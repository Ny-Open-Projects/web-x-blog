---
title: [ENG-312] 笔试题——实现 CI 配额与排队治理（浪费任务检测 + 分账）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## ENG-312：手写 CI 配额治理

**需求与边界**：
- 需求：CI 构建记录按团队分账（时长×单价）；检测浪费型任务——① 无变更全量构建（affected 应为空却全跑）；② 重复触发（同 commit 3 次以上）；③ 深水任务白天跑（应 nightly）；输出治理清单与分账报表。
- 边界：① 浪费判定带容忍（小项目全量构建成本可忽略）；② 重复触发排除「合法重试」（手动 re-run 计一次）；③ 分账按 runner 类型差异化单价。

**答**：
```javascript
function ciGovernance(records, { allBuildThreshold = 300 } = {}) {
  const byTeam = groupBy(records, 'team');
  const billing = {}, waste = [];
  for (const [team, list] of Object.entries(byTeam)) {
    billing[team] = list.reduce((s, r) => s + r.minutes * PRICE[r.runnerType], 0);
    // 浪费检测
    for (const r of list) {
      if (r.affectedCount === 0 && r.mode === 'full' && r.minutes > allBuildThreshold / 60)
        waste.push({ team, task: r.task, type: 'EMPTY_AFFECTED_FULL_BUILD', minutes: r.minutes });
      if (r.mode === 'nightly' && inBusinessHours(r.startedAt))
        waste.push({ team, type: 'NIGHTLY_IN_DAYTIME' });
    }
    const byCommit = groupBy(list, 'commit');
    for (const [commit, runs] of Object.entries(byCommit)) {
      const manual = runs.filter(r => !r.isAutoRetry).length;    // 合法重试排除
      if (manual >= 3) waste.push({ team, commit, type: 'REPEATED_TRIGGER', count: manual });
    }
  }
  return { billing, waste: waste.sort((a, b) => b.minutes - a.minutes || b.count - a.count) };
}
```

**评分点**:
- 分账按 runner 类型差异化单价（成本可见 ENG-270）。
- 浪费三分类（空 affected 全量/重复触发/深水白天跑）。
- 合法重试与重复触发的区分（避免误伤）。
- 全量构建成本阈值容忍（小项目不误报）。
