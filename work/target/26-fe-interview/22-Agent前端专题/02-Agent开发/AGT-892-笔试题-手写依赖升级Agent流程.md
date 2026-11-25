---
title: [AGT-892] 手写 autoUpgrade：breaking解析、影响面扫描、PR组装、监控挂钩与回滚建议？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-892：手写 autoUpgrade：breaking解析、影响面扫描、PR组装、监控挂钩与回滚建议

**需求与边界**：
- 实现 autoUpgrade(dep, from, to)。
- 边界要求：① 从 changelog 解析 breaking（API 变更/删除导出）；② 影响面扫描（用到变更 API 的文件清单）；③ PR 必须带：breaking 点标注+改动+关键路径 E2E；④ 版本策略文件（semver/pin）不得被修改（diff 校验）；⑤ 合并后 7 天错误率监控挂钩，spike 触发回滚建议。

**答**：
```javascript
async function autoUpgrade(dep, from, to, { git, monitor }) {
  const breaking = await parseChangelog(dep, from, to);
  const files = usageScan(dep, breaking.apis);     // 影响面
  const patch = await agent.adapt(files, breaking);
  const pr = await git.openPR({
    title: `chore(deps): ${dep} ${from}→${to}`,
    body: renderBreaking(breaking),
    files: patch,
    checks: { e2e: CRITICAL_PATHS },               // 行为回归
  });
  const policyDiff = await git.diff(pr, ['package-lock.json', 'semver.json']);
  if (policyDiff.changed)
    throw new Error('版本策略文件不得修改');          // 策略保护
  monitor.link(pr, { metric: 'errorRate', days: 7,
    onSpike: () => suggest({ revert: pr, reason: '错误率spike' }) });
  return pr;
}
```

**评分点**:
- breaking 解析驱动适配（不是盲升）；影响面精确到文件。
- 版本策略文件保护（Agent 越权改策略即抛错）。
- 行为回归 E2E 必带 + 7 天错误率挂钩与回滚建议。

