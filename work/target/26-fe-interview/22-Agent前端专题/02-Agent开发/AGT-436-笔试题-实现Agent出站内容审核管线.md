---
title: [AGT-436] 笔试题——实现生成内容审核管线（规则+模型双层+人审分流）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-436：手写内容审核：规则快筛、模型细审、置信分流、申诉标记

**需求与边界**：
- 输入：生成文本、审核配置（词表/规则/模型）；输出：{decision: pass/reject/review, reasons}。
- 边界要求：① 规则层先行（禁词/正则，零成本毫秒级）；② 模型层只审规则漏掉的（降低调用量）；③ 双高置信直判，灰区分流人审；④ reject 必须带可定位的原因（供申诉与改进）。

**答**：
```javascript
async function contentReview(text, { rules, modelJudge, thresholds }) {
  // 1. 规则层快筛
  const ruleHits = rules.flatMap(r => {
    const m = text.match(r.re);
    return m ? [{ rule: r.id, pos: m.index,
      snippet: m[0], severity: r.severity }] : [];
  });
  const hardBlock = ruleHits.some(h => h.severity === 'high');
  if (hardBlock) return { decision: 'reject',
    reasons: ruleHits.filter(h => h.severity === 'high') };
  // 2. 模型层细审（规则有命中或不发果断置信低时才调）
  const needsModel = ruleHits.length > 0 ||
    await cheapSuspicion(text);                 // 轻量预筛
  let modelResult = null;
  if (needsModel) {
    modelResult = await modelJudge(text);       // {risk, category, conf}
    if (modelResult.risk >= thresholds.high &&
        modelResult.conf >= 0.9)
      return { decision: 'reject', reasons: [modelResult] };
  }
  // 3. 分流：灰区 → 人审；其余 → pass
  const gray = modelResult &&
    modelResult.risk >= thresholds.low &&
    modelResult.conf < 0.9;
  return gray
    ? { decision: 'review', reasons: [modelResult, ...ruleHits],
        appealable: true }
    : { decision: 'pass', reasons: [] };
}
// 命中位置（pos）+ 片段（snippet）支持前端高亮与申诉定位。
```

**评分点**:
- 双层架构：规则快筛先行（高严重度直拒零成本），模型层按需调用。
- 分流正确：双高置信直判、灰区（低置信+中风险）进人审队列。
- 原因带位置与片段（可定位、可申诉）。
- cheapSuspicion 预筛降低模型审核量的成本意识。
