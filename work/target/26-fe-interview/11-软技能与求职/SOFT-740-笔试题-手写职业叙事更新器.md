---
title: [SOFT-740] 手写 narrativeUpdator：经历→层级叙事组装、一致性校验（简历/答辩/面试口径）、半年更新提醒？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-740：手写 narrativeUpdator：经历→层级叙事组装、一致性校验（简历/答辩/面试口径）、半年更新提醒

**需求与边界**：
- 实现 narrativeUpdator(experiences, narrative)。
- 边界要求：① experiences 每条含 { period, level, keyword, evidence[3件套] }，evidence 三件套（数字/文档/他人评价）缺一标 GAP；② 叙事按层级关键词组装（P5交付守信→P6独立owner→P7体系杠杆的成长线）；③ 一致性校验：narrative 与 resume/defense 的关键字段比对（不一致列差异）；④ 更新提醒：距上次更新 >6 个月触发；⑤ 输出叙事 markdown + 差异清单。

**答**：
```javascript
function narrativeUpdator(experiences, narrative, { resume, defense,
  lastUpdated }) {
  const ORDER = { P5: 0, P6: 1, P7: 2, P8: 3 };
  const sorted = [...experiences].sort((a, b) =>
    ORDER[a.level] - ORDER[b.level]);
  const gaps = [];
  for (const e of sorted) {
    const [num, doc, social] = e.evidence ?? [];
    if (!num || !doc || !social)
      gaps.push({ period: e.period, missing:
        [!num && '数字', !doc && '文档', !social && '他人评价']
          .filter(Boolean) });                        // 三件套检查
  }
  const md = sorted.map(e =>
    `**${e.level}：${e.keyword}**\n${e.period}——${e.summary}\n` +
    `证据：${(e.evidence ?? []).filter(Boolean).join('｜')}`).join('\n\n');
  const inconsistencies = [];
  for (const e of sorted) {
    for (const [scene, text] of [['resume', resume?.[e.level]],
      ['defense', defense?.[e.level]]]) {
      if (text && text.keyword !== e.keyword)
        inconsistencies.push({ level: e.level, scene,
          narrative: e.keyword, sceneSays: text.keyword });
    }
  }
  const stale = lastUpdated && (Date.now() - lastUpdated) > 183 * 864e5;
  return { narrative: md, evidenceGaps: gaps,
    inconsistencies, staleUpdate: stale ? '叙事>6个月未更新' : null };
}
```

**评分点**:
- 证据三件套缺一标 GAP（每段经历都有数字+文档+他人评价）。
- 跨场景一致性校验（简历/答辩口径比对——叙事不一致的防御）。
- 半年更新提醒（叙事是活文档）。

