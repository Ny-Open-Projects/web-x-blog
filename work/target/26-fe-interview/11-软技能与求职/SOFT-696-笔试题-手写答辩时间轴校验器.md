---
title: [SOFT-696] 手写 timelineCheck：陈述稿分段时长核算、超时预警、砍量建议（90%版本）？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-696：手写 timelineCheck：陈述稿分段时长核算、超时预警、砍量建议（90%版本）

**需求与边界**：
- 实现 timelineCheck(segments, limit)：segments 每段 { name, words, must: bool }。
- 边界要求：① 中文语速按 240 字/分钟估算时长；② 总时长超 limit 报超时并给砍量建议（先砍非 must 段，每段砍 30%——90% 版本生成）；③ must 段不可砍（定位与核心案例）；④ 每段占时占比输出（核心案例须 ≥50% 否则警告结构失衡）。

**答**：
```javascript
function timelineCheck(segments, limitMin = 15) {
  const RATE = 240;                                  // 字/分钟
  const withTime = segments.map(s => ({ ...s,
    minutes: +(s.words / RATE).toFixed(1) }));
  const total = withTime.reduce((a, s) => a + s.minutes, 0);
  const over = +(total - limitMin).toFixed(1);
  const result = { segments: withTime, total, limit: limitMin };
  if (over > 0) {
    const cuttable = withTime.filter(s => !s.must)
      .sort((a, b) => b.minutes - a.minutes);
    result.overBy = over;
    result.cutPlan = cuttable.slice(0, 2).map(s => ({
      name: s.name, action: `砍30%：${s.words}→${Math.round(s.words * 0.7)}字`,
      saves: +(s.minutes * 0.3).toFixed(1) }));       // 90%版本
    result.note = cuttable.length === 0
      ? '全部为must段——结构必须重排'
      : `按砍量计划可省 ${result.cutPlan.reduce((a, c) => a + c.saves, 0)} 分钟`;
  }
  const core = withTime.filter(s => s.tag === 'case')
    .reduce((a, s) => a + s.minutes, 0);
  if (core / total < 0.5)
    result.structureWarn = '核心案例占比<50%——评委评深度，结构失衡';
  return result;
}
```

**评分点**:
- 语速估算+超时砍量计划（must 段保护、非 must 先砍 30%）。
- 结构占比校验（核心案例 ≥50%——评深度不评广度）。

