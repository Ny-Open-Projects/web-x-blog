---
title: [SOFT-735] 手写 timePortrait：日历数据→四桶分布（产出/复利/影响/培养）、配比偏差诊断、调参建议？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-735：手写 timePortrait：日历数据→四桶分布（产出/复利/影响/培养）、配比偏差诊断、调参建议

**需求与边界**：
- 实现 timePortrait(events, target)。
- 边界要求：① events 每条含 { hours, bucket: 'output'|'growth'|'influence'|'mentoring' }；② 输出实际配比 vs 目标配比（P6-7 标配 50/20/15/15——SOFT-725）；③ 偏差 >10pp 的桶标诊断（过高/过低）；④ 诊断给出调参建议（具体活动类别转移）；⑤ 无 events 抛错。

**答**：
```javascript
function timePortrait(events, target = { output: 50, growth: 20,
  influence: 15, mentoring: 15 }) {
  if (!events?.length) throw new Error('无日历数据');
  const totalH = events.reduce((a, e) => a + e.hours, 0);
  const actual = {};
  for (const e of events)
    actual[e.bucket] = +(((actual[e.bucket] ?? 0) + e.hours)
      / totalH * 100).toFixed(1);
  const rows = Object.keys(target).map(b => {
    const diff = +(actual[b] - target[b]).toFixed(1);
    return { bucket: b, actual: actual[b], target: target[b], diff,
      diagnose: Math.abs(diff) <= 10 ? 'OK'
        : diff > 0 ? `过高${diff}pp——挤占了其他桶`
        : `过低${diff}pp`,
      fix: diff < -10 ? FIX[b] : null };
  });
  return { rows, totalHours: totalH };
}
const FIX = {
  growth: '每天固定1h学习块（日历预定——不靠意志力）',
  influence: '每周1篇署名文档+月1次分享（SOFT-720）',
  mentoring: '固定每周15min×新人1:1（SOFT-714）',
  output: '产出是根基——检查是否被会议侵蚀，砍低效会',
};
```

**评分点**:
- 感知与现实的量化对照（日历统计 vs 自我感觉）。
- 偏差 10pp 阈值诊断 + 每桶具体调参建议。
- 无数据抛错（不空谈配比）。

