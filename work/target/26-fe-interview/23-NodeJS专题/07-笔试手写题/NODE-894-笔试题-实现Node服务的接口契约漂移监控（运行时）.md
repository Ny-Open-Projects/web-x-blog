---
title: [NODE-894] 笔试题——实现接口契约漂移监控（运行时响应 vs 契约）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-894：手写契约监控

**需求与边界**：
- 需求：运行时契约监控（SCN-NODE-677/OPS-289）——① 响应采样比对契约（运行时响应 vs schema/pact——SCN-OPS-894）；② 漂移告警（契约外字段/缺失字段——SCN-OPS-293 分类）；③ 漂移归因（provider 版本——SCN-OPS-231）；④ 门禁联动（漂移率超阈值阻断发布——SCN-OPS-829）。
- 边界：① 采样率（1%——成本，SCN-SLA-724）；② 宽松匹配（类型匹配 vs 精确——SCN-NODE-768）；③ 契约版本（SCN-NODE-694）。

**答**：
```javascript
function contractMonitor(pact) {
  return async (req, respBody) => {                    // 响应拦截采样
    if (Math.random() > 0.01) return;                  // 1% 采样（SCN-SLA-724）
    const mismatch = matchResponse(respBody, pact.response, { rules: pact.matchingRules });   // 宽松（SCN-NODE-768）
    if (mismatch) {
      alert({ type: 'CONTRACT_DRIFT', fields: classifyMismatch(mismatch),   // SCN-ENG-290 分类
        providerVersion: BUILD.commit.slice(0, 8) });  // 归因（SCN-OPS-231）
      driftCounter.increment(pact.consumer);
      if (driftRate(pact.consumer) > 0.05) blockDeploy(pact.provider);   // 门禁（SCN-OPS-829）
    }
  };
}
```

**评分点**:
- 运行时采样比对（1%——SCN-SLA-724）。
- 漂移分类 + 归因（SCN-ENG-290/OPS-231）。
- 漂移率门禁（SCN-OPS-829）。
- 宽松匹配（SCN-NODE-768）。
