---
title: [AGT-496] 笔试题——实现分层归因报告（端到端差→定位层→修复建议）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-496：手写分层归因：指标逐层拆解、瓶颈定位、修复建议排期

**需求与边界**：
- 输入：各层指标（检索/生成/端到端）；输出：归因报告。
- 边界要求：① 端到端指标差→逐层拆解定位瓶颈层；② 层间关系建模（检索好+答案差→生成层；检索差→检索层优先）；③ 每层给修复建议与预期收益排序；④ 趋势对比（本次 vs 上次各层变化）。

**答**：
```javascript
function attributeReport(m, prev) {
  const layers = [
    { name: 'retrieval', metrics: { recall: m.retrieval.recall,
      mrr: m.retrieval.mrr } },
    { name: 'generation', metrics: { faithfulness: m.gen.faithfulness,
      relevance: m.gen.relevance } },
    { name: 'e2e', metrics: { success: m.e2e.success,
      userAccept: m.e2e.accept } }];
  // 瓶颈定位规则链
  let bottleneck;
  if (m.retrieval.recall < 0.7)
    bottleneck = { layer: 'retrieval',
      why: `recall ${m.retrieval.recall} 过低，生成层无米下锅`,
      fixes: [['加 rerank', '+8% 预期'],
        ['检查分块/金标集', '数据层'],
        ['换 embedding 或查询改写', '+5% 预期']],
      order: 1 };
  else if (m.gen.faithfulness < 3.5)
    bottleneck = { layer: 'generation',
      why: '检索达标但忠实性低：prompt 对齐/资料冲突未处理',
      fixes: [['引用强制+资料优先指令', '+10% 预期'],
        ['CRAG 质量门', '拦截低质召回'],
        ['忠实性 badcase 聚类', '找具体模式']],
      order: 2 };
  else if (m.e2e.success < m.gen.relevance)
    bottleneck = { layer: 'assembly',
      why: '各层达标但端到端差：上下文装配/压缩丢信息',
      fixes: [['检查压缩忠实性', 'AGT-451 校验'],
        ['上下文回放定位', 'AGT-369']],
      order: 3 };
  else bottleneck = { layer: 'none',
    why: '各层达标，端到端差源于任务难度或评测集偏差',
    fixes: [['分析失败样本', '非系统问题']] };
  // 趋势对比
  const trend = prev ? Object.fromEntries(
    layers.map(l => [l.name,
      delta(m[l.name], prev[l.name])])) : null;
  return { bottleneck, trend,
    nextAction: bottleneck.fixes[0] };
}
```

**评分点**:
- 层间关系建模正确：检索低优先修检索（无米下锅）、检索好答案差修生成、各层好端到端差查装配。
- 修复建议带预期收益与优先级排序（可排期）。
- 趋势对比（vs 上次各层 delta）。
- 承认"各层达标仍差"的可能（任务难度/评测集偏差）——归因不武断。
