---
title: [AIC-331] AI 评审发现 PR 过大（建议拆分），如何让拆分建议「可执行」而非一句「拆小点」？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-331：AI 评审发现 PR 过大（建议拆分），如何让拆分建议「可执行」而非一句「拆小点」？
**答**：
- 基于依赖图拆：AI 分析 diff 内文件的依赖关系，输出「可独立合入的变更组」（拓扑排序）。
- 每组附独立验收标准与回归范围，保证每组 PR 单独可验证。
- 拆分顺序考虑冲突成本：公共接口变更组先行。
- 给出拆分后的 diff 预览（按组切割的 patch），人确认后自动生成多个 PR。

```javascript
async function suggestSplit(pr: PR) {
  const groups = topoGroups(pr.files, depsGraph);      // 依赖图分组
  if (groups.length < 2) return 'ok';
  return groups.map(g => ({ files: g, patch: slicePatch(pr.diff, g),
                            acceptance: perGroupCriteria(g) }));
}
r
```
