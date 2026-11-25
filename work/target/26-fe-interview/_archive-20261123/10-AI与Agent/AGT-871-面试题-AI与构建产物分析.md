---
title: [AGT-871] 构建产物（bundle）异常（体积暴涨）AI 辅助定位：输入什么才能准？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-871：构建产物（bundle）异常（体积暴涨）AI 辅助定位：输入什么才能准

**答**：
- 输入三件套：产物 diff（本次 vs 上次：新增模块/体积变化/依赖图变化）、提交 diff（哪个 commit 引入）、历史趋势（是渐进劣化还是突增）。只有体积数字没有 diff，AI 只能说"体积大了"这种废话。
- 归因到「人的动作」：定位到 commit+PR+作者，输出"PR #123 引入 X 库全量导入（+120KB），建议改具名导入"——可行动到人。
- 门禁联动：体积预算超限时自动跑该分析，分析结果直接附在 CI 失败信息里。

```javascript
async function bundleAttribution(build) {
  const diff = await artifactDiff(build.prev, build.current);
  const commits = await git.diffCommits(build.prev, build.current);
  return llm.attribute({ diff, commits, trend: historyTrend(build) }, {
    require: '归因到 commit+模块+修复建议',
  });
}
// CI 门禁联动
sizeBudget.onExceed(async (report) => {
  report.attribution = await bundleAttribution(report.build);
});
```

