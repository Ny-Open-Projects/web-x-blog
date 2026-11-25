---
title: [SOFT-537] 手写 onePager：将完整方案压缩成一页纸（决策人 3 分钟版），字段截断与完整性守恒？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-537：手写 onePager：将完整方案压缩成一页纸（决策人 3 分钟版），字段截断与完整性守恒

**需求与边界**：
- 实现 onePager(doc)。
- 边界要求：① 必含字段：一句话方案/3个关键数字/风险top2/需决策点/时间线；② 每字段限长（一句话≤80字，数字≤3个取最重要）；③ 关键数字必须带出处标记；④ 决策点选项式（A/B/C）；⑤ 压缩不删事实（数字截取时保留量纲）。

**答**：
```javascript
function onePager(doc) {
  const cut = (s, n) => s.length <= n ? s : s.slice(0, n - 1) + '…';
  const nums = doc.metrics
    .filter(m => m.source)
    .sort((a, b) => b.importance - a.importance)
    .slice(0, 3)
    .map(m => `${m.name} ${m.value}（${m.source.slice(0, 12)}）`);
  if (nums.length < 3)
    throw new Error('带出处的关键数字不足3个');     // 完整性守恒
  return [
    `方案：${cut(doc.oneline, 80)}`,
    `关键数字：\n- ${nums.join('\n- ')}`,
    `风险top2：\n- ${doc.risks.slice(0, 2).map(r =>
      cut(`${r.name}｜兜底：${r.fallback}`, 80)).join('\n- ')}`,
    `需决策：${doc.decisionPoints.map(d =>
      `${d.q}（A:${d.a}/B:${d.b}）`).join('；')}`,
    `时间线：${doc.milestones.map(m =>
      `${m.name}@${m.date}`).join(' → ')}`,
  ].join('\n');
}
```

**评分点**:
- 必含五字段（方案/数字/风险/决策/时间线）；数字不足 3 个抛错（防空壳一页纸）。
- 截断保量纲（cut 留省略号）；决策点选项式（降低拍板摩擦）。

