---
title: [SOFT-738] 手写 brandCheck：领域三交评估（业务需要×优势×趋势）、产出密度计分、心智占位调研设计？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-738：手写 brandCheck：领域三交评估（业务需要×优势×趋势）、产出密度计分、心智占位调研设计

**需求与边界**：
- 实现 brandCheck(myDomain)。
- 边界要求：① 三交打分：业务需要（痛点数据支撑）/我的优势（可验证产出）/长期趋势（5 年需求预测），各 1~5；② 总分 <9 建议换域或补维度；③ 产出密度 = 近 12 月域内产出（文档+工具+分享数）；④ 心智占位调研：生成 3 个调研问题（问同事“XX 类问题你会找谁”）验证占位；⑤ 输出品牌现状与差距行动。

**答**：
```javascript
function brandCheck(myDomain, { business, strength, trend, outputs }) {
  const tri = [
    { name: '业务需要', s: business.needScore, ev: business.painData },
    { name: '我的优势', s: strength.score, ev: `${strength.outputs}项可验证产出` },
    { name: '长期趋势', s: trend.score, ev: trend.reason },
  ];
  const total = tri.reduce((a, t) => a + t.s, 0);
  const density = outputs.docs + outputs.tools + outputs.shares;
  const weak = tri.filter(t => t.s <= 2);
  return {
    tri, total,
    verdict: total < 9 ? `品牌地基弱（${weak.map(w => w.name)}≤2分）——换域或补维度`
      : total >= 12 ? '品牌地基扎实' : '可用但需补强',
    density,
    densityVerdict: density >= 12 ? '产出密度足' : `产出密度不足（${density}/12）——每季度至少3项`,
    survey: ['遇到【域内】问题你第一反应找谁？',
      '过去半年你找我帮过什么忙？',
      '如果要推荐一位【域内】专家你写谁？'],
    actions: weak.map(w => `${w.name}补强：${w.ev ? '已有依据' : '缺依据——先补数据/产出'}`),
  };
}
```

**评分点**:
- 三交打分量化 + 低分维度定位（品牌地基诊断）。
- 产出密度计分（12 月产出可数）。
- 心智占位用真实调研验证（不是自以为“大家都知道我”）。

