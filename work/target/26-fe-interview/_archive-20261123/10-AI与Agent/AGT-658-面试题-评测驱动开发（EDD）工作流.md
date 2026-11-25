---
title: [AGT-658] 把 TDD 思路用到提示词/Agent 开发上，完整工作流长什么样？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-658：把 TDD 思路用到提示词/Agent 开发上，完整工作流长什么样

**答**：
- 先写失败用例再改实现：新需求/新 bug 先在评测集里固化（输入+期望判据），确认当前版本失败，然后改提示词/工具，跑到通过才提交。
- CI 集成：PR 自动跑冒烟层，结果贴到 PR 评论（分数 diff + 失败用例列表）；回归分数下跌超阈值阻断合并——提示词改动和代码改动同权限。
- 变更即实验：每次提示词 diff 自动记录「改了什么+分数变化+谁改的」，形成提示词的实验历史，回滚有据可查。

```javascript
// PR 门禁：冒烟层分数守护
function onPullRequest(pr, changed) {
  const runs = changed.prompt ? runTier('smoke') : runTier('smoke', { affectedOnly: true });
  const base = lastGreenScore('smoke');
  if (runs.passRate < base.passRate - 0.02)      // 跌幅>2%阻断
    return block(pr, { failed: runs.failures, diff: scoreDiff(base, runs) });
  comment(pr, renderScoreTable(base, runs));      // PR评论跑分
}
```

