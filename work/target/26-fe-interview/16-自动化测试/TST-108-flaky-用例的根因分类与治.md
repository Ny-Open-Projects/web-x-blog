---
title: [TST-108] flaky 测试的根因有哪些？怎么系统性治理？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-108：flaky 测试的根因有哪些？怎么系统性治理？
**答**：
- 根因五类：① 时序竞争（动画/异步渲染未完成就断言，隐性 sleep 补丁）；② 环境漂移（时区、分辨率、字体、网络、第三方接口抖动）；③ 数据污染（用例共享数据、顺序依赖、后端脏数据）；④ 依赖抖动（外部接口限流、第三方服务超时）；⑤ 并发干扰（并行 worker 抢资源、端口/账号冲突）。
- 治理四步：第一步**度量**——CI 收集每个用例的重试率/失败率，产出 flaky 榜单（Playwright retries + JSON 报告可统计）；第二步**隔离**——flaky 用例打 tag（`test.fixme` 或 `@flaky`）移出主干门禁，进独立 job 定时跑；第三步**修复**——按根因对症（条件等待替代 sleep、mock 三方、唯一数据前缀、worker 隔离）；第四步**闭环**——修不完的定期清理或删除，别让 flaky 名单越滚越大。
- 重试的正确用法：`retries: 2` 是止血不是治疗——掩盖 flaky 但掩盖不了根因，必须配合榜单治理；且断言失败的 Error 要标记 fatal 不重试（断言重跑没有意义）。
- 文化：把 flaky 率当质量指标（目标 <1%），谁写的谁修；Code Review 时重点审「sleep、随机数、依赖顺序」三个 flaky 味。
- 追问钩子：Google 怎么做？——FailureAtlas/自动禁用 + 自动归因，核心思想都是先隔离止血再归因修复。

```javascript
// flaky 榜单生成：从 Playwright JSON 报告统计重试率
const report = require('./test-results.json');
const stats = {};
for (const s of report.suites) {
  for (const spec of flatten(s)) {
    for (const t of spec.tests) {
      const retried = t.results.length > 1;
      stats[spec.title] ||= { runs: 0, retries: 0 };
      stats[spec.title].runs += t.results.length;
      stats[spec.title].retries += t.results.filter((r) => r.status !== 'passed').length;
    }
  }
}
const flakyTop = Object.entries(stats)
  .map(([name, { runs, retries }]) => ({ name, rate: retries / runs }))
  .filter((x) => x.rate > 0).sort((a, b) => b.rate - a.rate).slice(0, 10);
console.table(flakyTop); // 输出周报，隔离 top10
```
