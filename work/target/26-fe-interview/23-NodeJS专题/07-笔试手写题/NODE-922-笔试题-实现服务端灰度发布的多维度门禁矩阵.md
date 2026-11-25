---
title: [NODE-922] 笔试题——实现灰度多维门禁矩阵（配置/数据/依赖/流量）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-922：手写多维门禁

**需求与边界**：
- 需求：多维门禁矩阵（SCN-OPS-229/886/917/859）——① 四维门禁（配置/数据兼容/依赖/流量准入——全链）；② 各维的门禁项与分级（SCN-OPS-229）；③ 矩阵的并行执行（Promise.allSettled——SCN-NODE-729）；④ 总判定（全过才放行——SCN-OPS-229）。
- 边界：① 各维复用（编号引用）；② 豁免的统一入口（SCN-OPS-229）；③ 矩阵的报告（SCN-OPS-261）。

**答**：
```javascript
const GATE_DIMENSIONS = {
  config: configSyncCheck,                             // SCN-NODE-886
  data: dataCompatGate,                                // SCN-OPS-829
  deps: canaryDepsCheck,                               // SCN-NODE-917
  traffic: (r) => ({ ok: grayRulesReady(r), note: '分流规则就绪' }),   // SCN-OPS-216
};
async function multiDimGate(release) {
  const results = await Promise.allSettled(            // 并行（SCN-NODE-729）
    Object.entries(GATE_DIMENSIONS).map(async ([dim, check]) =>
      ({ dim, ...await check(release) })));
  const failures = results.filter(r => r.status === 'fulfilled' && !r.value.ok)
    .map(r => ({ dim: r.value.dim, detail: r.value.issues ?? r.value.unready }));
  const waived = failures.filter(f => release.waivers?.[f.dim]);   // 豁免（SCN-OPS-229）
  return {
    pass: failures.every(f => waived.includes(f)),
    failures, waived,
    report: forReviewBoard(failures),                  // SCN-OPS-261
  };
}
```

**评分点**:
- 四维门禁矩阵（配置/数据/依赖/流量——全链覆盖）。
- 并行执行 + 总判定（SCN-NODE-729/OPS-229）。
- 豁免统一入口（SCN-OPS-229）。
- 报告（SCN-OPS-261）。
