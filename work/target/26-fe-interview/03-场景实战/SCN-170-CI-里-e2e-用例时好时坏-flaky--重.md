---
title: [SCN-170] CI 里 e2e 用例时好时坏（flaky），重试也救不了信任度，如何系统性治理？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-170：CI 里 e2e 用例时好时坏（flaky），重试也救不了信任度，如何系统性治理？
**答**：
- 先分类再动手：收集一段时间内的失败记录（trace/video），按"环境不稳 / 等待不当 / 测试间耦合 / 真实 bug"四类归因，前三类是治理对象。
- 等待不当是大头：删掉固定 sleep，统一用"等待状态"（locator 等元素可交互、waitForResponse 等接口返回），用例写法进 lint/评审规范。
- 测试间耦合：用例必须自建数据（factory/seed），不依赖执行顺序与共享账号；并行 worker 用独立数据空间。
- 治理闭环：CI 对 flaky 用例自动打标（失败后重跑通过即记 flaky），周报排名，连续两周 flaky 率超阈值的用例隔离到 nightly，不允许阻塞主干合入。

```yaml
# e2e 稳定性治理：重试隔离 + trace 留档 + 并行数据隔离（Playwright 配置示例）
# playwright.config.yml（节选，实际项目为 .ts，此处以 yaml 说明关键项）
workers: 4                    # 并行，但要求用例数据自建
retries: 2                    # 失败重试 2 次
fullyParallel: true
reporter:
  - list
  - html:
      outputFolder: reports/e2e
use:
  trace: retain-on-failure    # 失败留 trace：定位 flaky 归因的第一手证据
  video: retain-on-failure
  screenshot: only-on-failure

projects:
  - name: stable              # 主干门禁：只跑稳定用例
    testDir: tests/stable
  - name: flaky-quarantine   # flaky 隔离区：nightly 才跑，不阻塞合入
    testDir: tests/quarantine
```

```javascript
// flaky 自动打标：失败后重试通过即记录，周报输出 flaky 榜
export function trackFlaky(results) {
  const flaky = results.filter(r => r.outcome === 'flaky'); // Playwright 结果自带 flaky 判定
  const board = {};
  for (const r of flaky) {
    board[r.title] ??= { count: 0, errors: [] };
    board[r.title].count++;
    board[r.title].errors.push(r.errors?.[0]?.message?.slice(0, 200));
  }
  // 连续超标则移动到隔离区并建 issue
  for (const [title, s] of Object.entries(board)) {
    if (s.count >= 3) {
      gitmvTest(title, 'tests/quarantine/');
      createIssue({ title: `flaky: ${title}`, body: s.errors.join('\n') });
    }
  }
  reportWeekly({ flakyRate: flaky.length / results.length, board });
}
```
