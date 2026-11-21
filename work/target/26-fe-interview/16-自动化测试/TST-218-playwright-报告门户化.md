---
title: [TST-218] 如何把 Playwright 报告升级为团队「测试门户」（趋势/归因/flaky 名单）？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-218：如何把 Playwright 报告升级为团队「测试门户」（趋势/归因/flaky 名单）？
**答**：
- 结构化收集：每次运行的用例结果（时长/重试/失败原因/shard）入库。
- 门户三视图：趋势（通过率/时长）、flaky 排行（按周失败次数）、失败聚类（按错误特征分组）。
- 与代码联动：失败自动关联变更 PR，标出「嫌疑 commit」。
- 门禁闭环：flaky 排行上的用例限期治理，否则自动隔离。

```javascript
// 自定义 reporter：结果入库
class PortalReporter implements Reporter {
  onEnd(result) {
    return post('/api/test-runs', { suite: 'e2e', results: this.results,
      meta: { shard: process.env.SHARD_INDEX, runId: process.env.GITHUB_RUN_ID } });
  }
}
r
```
