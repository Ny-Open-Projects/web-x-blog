---
title: [SOFT-881] 手写 perspectiveSim：简历的三视角模拟评分（HR6秒/技术官30秒/经理2分钟）与热区检查？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-881：手写 perspectiveSim：简历的三视角模拟评分（HR6秒/技术官30秒/经理2分钟）与热区检查

**需求与边界**：
- 实现 perspectiveSim(resume)。
- 边界要求：① resume 结构化：{ sections: [{name, order, highlights[]}] }（sections 有顺序）；② HR6 秒：公司/职级/教育/关键词是否在前 1/3 section（SOFT-863）；③ 技术官 30 秒：量化条目与技术栈是否在前 50% 内容（热区检查）；④ 用人经理 2 分钟：JD 痛点案例是否前置；⑤ 输出各视角通过与否+重排建议。

**答**：
```javascript
function perspectiveSim(resume, { jd } = {}) {
  const n = resume.sections.length;
  const posOf = (name) => resume.sections.findIndex(s => s.name === name);
  const hrPass = ['公司', '职级', '教育', '技能关键词']
    .filter(k => posOf(k) !== -1 && posOf(k) < n / 3);
  const hot = resume.sections.slice(0, Math.ceil(n / 2));
  const quantInHot = hot.flatMap(s => s.highlights)
    .filter(h => /\d/.test(h.text ?? h)).length;
  const techInHot = hot.some(s =>
    s.name.match(/技术|项目/));
  const painFirst = resume.sections.find(s =>
    s.highlights?.some(h => jd?.painKeywords?.some(k =>
      (h.text ?? h).includes(k))));
  const ranked = painFirst && posOf(painFirst.name) <= 1;
  return {
    hr: { pass: hrPass.length >= 3, found: hrPass,
      note: hrPass.length >= 3 ? '机筛要素前置✓' : '关键要素不在前1/3——重排' },
    tech: { pass: quantInHot >= 2 && techInHot,
      quantInHot, note: quantInHot >= 2 ? '热区量化✓'
      : '量化条目不在热区（上部+左侧）——上移' },
    manager: { pass: !!ranked,
      note: ranked ? 'JD痛点案例前置✓' : '痛点案例未前置——用人经理2分钟看不到匹配' },
    advice: [
      !hrPass.length >= 3 && '最强要素上移到前1/3',
      quantInHot < 2 && '量化条目移入上半区（F型热区 SOFT-863）',
      !ranked && '痛点案例提到第一屏',
    ].filter(Boolean) };
}
```

**评分点**:
- 三视角结构化检验（HR/技术官/经理各有判据 SOFT-863）。
- 热区量化检查（量化条目在上半区的 F 型热区）。
- 未通过项给重排建议（可执行）。

