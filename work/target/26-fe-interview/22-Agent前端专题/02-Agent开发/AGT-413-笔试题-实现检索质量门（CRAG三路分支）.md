---
title: [AGT-413] 笔试题——实现检索质量门（correct/ambiguous/incorrect 三分支）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-413：手写 CRAG 质量门：评分判级、精炼、回退重检与拒答

**需求与边界**：
- 输入：query、召回文档（含 score）、评估函数（打分 correct/ambiguous/incorrect）、重检与拒答出口；输出：最终证据或拒答。
- 边界要求：① 精炼只保留与 query 相关句子；② 回退 ≤2 次（改写重检+补充检索）；③ 全失败走诚实拒答（带部分已知信息）；④ 低分段子阈值判级（分数+语义双判据）。

**答**：
```javascript
async function cragRetrieve(query, { retrieve, judge, rewrite, webSearch }) {
  let attempt = 0;
  let docs = await retrieve(query, 10);
  while (attempt <= 2) {
    const verdict = await judge(query, docs);   // {grade, reasons}
    if (verdict.grade === 'correct')
      return { docs: refine(docs, query), quality: 'high' };
    if (verdict.grade === 'ambiguous') {
      // 精炼 + 补充检索（换写法）
      const q2 = attempt === 0 ? query : await rewrite(query);
      const extra = await retrieve(q2, 5);
      docs = dedupe([...refine(docs, query), ...extra]);
      attempt++;
      continue;
    }
    // incorrect：外部补充 + 重检
    const web = attempt < 2 ? await webSearch(query) : [];
    docs = dedupe([...docs.slice(0, 3), ...web]);
    attempt++;
  }
  // 全失败：诚实拒答 + 部分已知信息
  return {
    refusal: true,
    message: '知识库中未找到足够可靠的依据，以下为可能相关的片段（未经充分验证）：',
    partial: docs.filter(d => d.score > 0.3).slice(0, 2),
  };
}
function refine(docs, query) {                   // 相关句抽取
  return docs.map(d => ({ ...d,
    text: d.text.split(/(?<=[。；])/)
      .filter(s => relevance(s, query) > 0.5).join('') }));
}
```

**评分点**:
- 三分支完整：correct 精炼、ambiguous 精炼+补充重检、incorrect 外部回退。
- 回退次数上限 2 且改写递进（首次原词，二次改写）。
- 拒答非裸拒：带低分相关片段并明确标注"未经充分验证"。
- refine 句级相关过滤（证据净化）与 dedupe（多轮合并去重）。
