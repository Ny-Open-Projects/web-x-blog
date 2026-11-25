---
title: [SOFT-534] 手写 genMatrix：输入维度权重与候选评分，输出加权矩阵与前提化结论？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-534：手写 genMatrix：输入维度权重与候选评分，输出加权矩阵与前提化结论

**需求与边界**：
- 实现 genMatrix(dims, options)。
- 边界要求：① dims 含 { name, weight }，权重和必须=1（否则抛错）；② 每个评分必须带 evidence 字段（缺证据的评分标 warning 不参与加权——防拍脑袋分）；③ 输出矩阵行+总分+前提化结论占位（"在【前提】下选X"）；④ 并列最高分时提示需要 tie-break 维度。

**答**：
```javascript
function genMatrix(dims, options) {
  const wSum = dims.reduce((a, d) => a + d.weight, 0);
  if (Math.abs(wSum - 1) > 1e-9) throw new Error('权重和须为1');
  const rows = options.map(o => {
    let score = 0; const warns = [];
    for (const d of dims) {
      const c = o.scores[d.name];
      if (!c?.evidence) warns.push(d.name);      // 缺证据
      else score += c.value * d.weight;
    }
    return { name: o.name, score: +score.toFixed(2), warns,
      missing: warns.length };
  });
  const valid = rows.filter(r => !r.missing);
  const max = Math.max(...valid.map(r => r.score));
  const top = valid.filter(r => r.score === max);
  return { rows,
    conclusion: top.length > 1
      ? `并列（${top.map(t => t.name)}），需补 tie-break 维度`
      : `在【填写前提】下选 ${top[0]?.name}；若前提变化重评`,
    warnings: rows.filter(r => r.missing) };
}
```

**评分点**:
- 权重和校验；缺证据评分排除加权并 warning（防拍脑袋分污染结论）。
- 并列时提示 tie-break 而非硬选；结论强制前提化占位。

