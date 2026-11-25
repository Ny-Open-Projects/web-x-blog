---
title: [ENG-218] flaky 测试的治理怎么体系化？重试是解药还是毒药？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-218：flaky 测试治理怎么做？
**答**：
- 重试是毒药：自动重试掩盖 flaky 且放大不确定性——重试只允许「隔离观察模式」（重试时标记结果为 flaky 候选），不允许重试后报绿。
- 治理流水线：flaky 检测（同 commit 多次运行差异/CI 与本地差异）→ 自动隔离（标 skip quarantine，不阻塞门禁但看板可见）→ 定期修（隔离测试有 SLA，两周不修强制删除或修好）。
- 常见根因分类：时间依赖（没 mock clock）、顺序依赖（共享状态）、异步竞态（sleep 等待改条件等待）、外部依赖（真网络/真数据库）——分类统计指导专项。
- 阻止新增：CI 统计每 PR 的 flaky 贡献（改动的测试是否新引入不稳定），超标拦截。
- 追问钩子：为什么「隔离不阻塞门禁」优于「失败阻塞」与「直接删除」——阻塞让团队麻木点重跑（真实回归被淹没），删除丢掉覆盖；隔离保持测试存在且可见，用 SLA 强制收敛到「修或删」。

```javascript
// flaky 检测：同 commit N 次运行
async function detectFlaky(test, { runs = 5 } = {}) {
  const results = await Promise.all(Array(runs).fill(0).map(() => runTest(test)));
  const passRate = results.filter(Boolean).length / runs;
  return { flaky: passRate > 0 && passRate < 1, passRate,
    quarantine: passRate < 1 && markQuarantine(test) };
}
// 隔离 SLA
setInterval(() => quarantined.filter(t => t.age > 14 * 864e5)
  .forEach(t => enforceFixOrDelete(t)), 864e5);
```
