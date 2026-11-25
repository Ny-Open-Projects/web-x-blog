---
title: [NODE-887] 笔试题——实现接口级熔断演练（注入 → 验证 → 报告）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-887：手写熔断演练

**需求与边界**：
- 需求：熔断演练（SCN-OPS-281/NODE-732）——① 注入下游故障（SCN-NODE-799 注入器）；② 熔断触发验证（open 事件 + 降级生效——SCN-NODE-732）；③ 恢复验证（half-open → closed——SCN-NODE-669）；④ 演练报告（触发时效/降级时效——SCN-OPS-215 计时）。
- 边界：① 注入范围（单下游/灰度小流量——SCN-OPS-281 范围限定）；② 演练与降级联动的完整性（SCN-NODE-778 链）；③ 报告进覆盖度（SCN-OPS-279）。

**答**：
```javascript
async function breakerDrill(target) {
  const t0 = Date.now();
  injector.inject({ target, type: 'error', pct: 100, windowMs: 30_000 });   // 注入（SCN-NODE-799）
  const opened = await waitFor(() => breaker(target).state === 'open', 10_000);   // 熔断触发验证
  const degraded = await waitFor(() => degradeActive(target), 5_000);   // 降级生效（SCN-NODE-778）
  injector.stop();                                     // 清理（SCN-NODE-799）
  const recovered = await waitFor(() => breaker(target).state === 'closed', 30_000);   // 恢复（SCN-NODE-669）
  const report = { opened: Date.now() - t0, degraded, recovered,
    pass: opened && degraded && recovered && (Date.now() - t0) < 45_000 };   // SCN-OPS-215 计时
  coverage.record({ mode: target, pass });             // 覆盖度（SCN-OPS-279）
  return report;
}
```

**评分点**:
- 注入→熔断→降级→恢复全链验证（SCN-NODE-799/732/778）。
- 分段计时（SCN-OPS-215）。
- 恢复验证（SCN-NODE-669）。
- 覆盖度联动（SCN-OPS-279）。
