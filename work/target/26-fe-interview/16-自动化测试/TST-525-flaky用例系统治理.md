---
title: [TST-525] 大规模场景下 flaky 用例如何系统治理
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-525：大规模场景下 flaky 用例如何系统治理

**答**：
- 结论：flaky 治理 = 检测（N 次重跑统计）+ 归因（环境/时序/数据/测试本身）+ 隔离（自动 quarantine）+ 修复闭环（根因库 + 负责人 + SLA）。
- 做法：CI 对失败用例自动重跑 2~3 次，稳定复现的进「可疑池」；按错误指纹聚类归因；高 flaky 的自动隔离并开 issue，禁止长期 skip 掩盖。
- 追问钩子：重跑「治好后」就放行是否掩盖问题？——重跑只用于「判定是否 flaky」，不用于「让构建通过」；真正的修复必须落到根因，隔离有有效期与 SLA。

```javascript
// flaky 检测：N 次重跑，统计不稳定度
function detectFlaky(resultsByRun) { // [{name, status}] 数组，每个元素是一次完整运行
  const byName = {};
  for (const run of resultsByRun) for (const r of run)
    (byName[r.name] ||= []).push(r.status);
  return Object.entries(byName).map(([name, statuses]) => {
    const flips = new Set(statuses).size > 1;
    const failRate = statuses.filter(s => s === 'fail').length / statuses.length;
    return { name, flaky: flips && failRate > 0 && failRate < 1, failRate };
  }).filter(x => x.flaky);
}
```
