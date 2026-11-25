---
title: [PER-1300] 手写一个"性能回归 blame 辅助器"：定位嫌疑 commit
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1300：手写一个"性能回归 blame 辅助器"：定位嫌疑 commit

**答**：
- 需求：implement blame(commits, regressedAt, windowDays=7)。commits 为 [{ sha, ts, files: [], author }]；嫌疑 = regressedAt 前窗口内的 commits；输出 { suspects: [{ sha, author, files, ageDays }], top }（files 与劣化资源路径交集最多的 commit）。
- 边界：劣化资源路径由参数 given；无交集时 top = null；ageDays 保留 1 位；按交集数降序。
- 评分点：窗口过滤；交集打分；排序规则；top 判定

```javascript
function blame(commits, regressedAt, resourcePaths, windowDays = 7) {
  const from = regressedAt - windowDays * 86400_000;
  const suspects = commits.filter(c => c.ts >= from && c.ts <= regressedAt)
    .map(c => ({ ...c,
      ageDays: +((regressedAt - c.ts) / 86400_000).toFixed(1),
      hits: c.files.filter(f => resourcePaths.some(r => f.includes(r))).length }))
    .sort((a, b) => b.hits - a.hits || a.ageDays - b.ageDays);
  return { suspects,
    top: suspects[0]?.hits > 0 ? suspects[0] : null };
}
// 输出贴进劣化报告：top suspect + 交集文件直接定位 PR；
```
