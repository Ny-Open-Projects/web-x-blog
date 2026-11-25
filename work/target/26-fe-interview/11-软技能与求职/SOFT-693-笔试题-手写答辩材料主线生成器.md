---
title: [SOFT-693] 手写答辩主线设计器：从证据池选主线类型、四段一致性校验、电梯陈述生成？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-693：手写答辩主线设计器：从证据池选主线类型、四段一致性校验、电梯陈述生成

**需求与边界**：
- 实现 genNarrative(evidences, targetLevel)：evidences 每条含 { domain, text, metric }。
- 边界要求：① 主线三选一（能力成长/价值创造/问题解决）按证据分布自动推荐（某类型证据占比 >50% 即推荐）；② 四段一致性校验（开场/案例/影响面/总结是否同线——非主线证据标 DANGLE）；③ 电梯陈述一句话生成（≤40 字含量纲数字）；④ 证据不足 3 条抛错。

**答**：
```javascript
function genNarrative(evidences, targetLevel) {
  if (evidences.length < 3) throw new Error('证据不足3条');
  const dist = countBy(evidences, e => e.domain);
  const types = {
    '体系化': '问题解决型：识别并补齐关键断层',
    '业务价值': '价值创造型：创造不可替代的业务价值',
    '成长': '能力成长型：完成X到Y的能力跃迁',
  };
  const top = maxBy(Object.entries(dist), ([, v]) => v);
  const narrative = types[top[0]] ?? '价值创造型';
  const dangling = evidences.filter(e => e.domain !== top[0]);
  const headline = evidences.filter(e => e.metric)
    .sort((a, b) => b.metric.importance - a.metric.importance)[0];
  return {
    narrative,
    headline: headline
      ? `一句话：${narrative.split('：')[1]}——${headline.text}（${headline.metric.value}）`
      : '缺量纲数字，无法生成电梯陈述',
    dangling: dangling.map(e => e.text),            // 不在主线的证据
    check: dangling.length === 0 ? '四段一致 ✓'
      : `${dangling.length}条证据脱离主线（删或改造）`,
  };
}
```

**评分点**:
- 主线按证据分布自动推荐（材料从事实出发而非空想主题）。
- 脱离主线的证据显式标出（一致性校验可执行）。
- 电梯陈述强制带量纲数字；证据不足抛错。

