---
title: [NODE-827] 笔试题——实现分级降级响应组装器（cache/default/static 级联）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-827：手写级联降级

**需求与边界**：
- 需求：级联降级组装（SCN-NODE-778）——① 策略级联（cache→default→static——链式尝试，SCN-NODE-778）；② 每级超时（级联不拖响应——SCN-NODE-642 预算）；③ 降级标记（SCN-NODE-690）；④ 级联的次数限制（全失败显式 503——SCN-联想-558 exhausted 语义）。
- 边界：① cache 策略的 last-good 时效（SCN-联想-675 陈旧标注）；② 级联的预算消耗（每级预算切片——SCN-NODE-728）；③ 级联事件上报（哪级成功——SCN-NODE-690 聚合）。

**答**：
```javascript
async function cascadeRespond(key, strategies, totalBudget) {
  let budget = totalBudget;
  for (const s of strategies) {                        // 策略级联（SCN-NODE-778）
    const slice = Math.min(budget, s.budget ?? 200);   // 每级预算切片（SCN-NODE-728）
    budget -= slice;
    try {
      const out = await withTimeout(s.run(key), slice);
      report({ level: s.name, ok: true });
      return { ...out, degraded: s.name !== 'primary',
        marker: `X-Degraded: ${s.name}` };             // 降级标记（SCN-NODE-690）
    } catch (e) { report({ level: s.name, ok: false }); continue; }   // 链式尝试
  }
  throw new AllStrategiesFailed();                     // 全失败显式 503（SCN-联想-558）
}
// 策略声明
[{ name: 'cache', run: () => staleCache.get(key), budget: 100 },          // last-good（SCN-联想-675）
 { name: 'default', run: () => DEFAULT[key], budget: 50 },
 { name: 'static', run: () => STATIC[key], budget: 50 }]
```

**评分点**:
- 策略级联 + 每级预算切片（SCN-NODE-728）。
- last-good 时效标注（SCN-联想-675）。
- 全失败显式 503（exhausted——SCN-联想-558）。
- 降级标记 + 事件聚合（SCN-NODE-690）。
