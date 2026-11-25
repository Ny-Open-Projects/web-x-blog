---
title: [NODE-919] 笔试题——实现降级路径定期探活（自动验证降级可用）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-919：手写降级探活

**需求与边界**：
- 需求：降级探活（SCN-联想-890）——① 定时触发降级（合成流量——SCN-OPS-281 注入）；② 降级验证（降级响应正确——SCN-NODE-778 策略生效）；③ 恢复（验证后恢复正常——SCN-NODE-799 清理）；④ 探活失败告警（降级路径损坏——P0，SCN-联想-890）。
- 边界：① 探活的范围（关键接口降级链——SCN-联想-833）；② 探活的频率（每日——SCN-联想-890）；③ 探活的标记（合成流量标记——SCN-NODE-717 不污染指标）。

**答**：
```javascript
cron('0 4 * * *', async () => {                        // 每日（SCN-联想-890）
  for (const api of criticalApis()) {
    const marker = syntheticTag();                     // 合成标记（SCN-NODE-717）
    injector.inject({ target: api.downstream, type: 'error', pct: 100,
      windowMs: 5000, observe: 'degrade-active' });    // 注入（SCN-OPS-281）
    const resp = await call(api, { headers: { 'x-synthetic': marker } });
    const degradedOk = resp.degraded && strategyApplied(api, resp);   // 降级生效（SCN-NODE-778）
    if (!degradedOk) alert({ type: 'DEGRADE_PATH_BROKEN', api, level: 'block' });   // P0
    report({ api, degradedOk });                       // 报告
  }
});
```

**评分点**:
- 每日自动探活（SCN-联想-890）。
- 合成标记（不污染指标——SCN-NODE-717）。
- 降级失效 P0 告警（SCN-联想-890/OPS-229）。
- 注入器联动（SCN-OPS-281）。
