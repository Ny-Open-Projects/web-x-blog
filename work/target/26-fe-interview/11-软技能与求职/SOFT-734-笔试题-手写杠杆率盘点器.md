---
title: [SOFT-734] 手写 leverageAudit：四类杠杆盘点（工具/机制/知识/决策）、系数估算、休假测试？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-734：手写 leverageAudit：四类杠杆盘点（工具/机制/知识/决策）、系数估算、休假测试

**需求与边界**：
- 实现 leverageAudit(myAssets)：盘点四类杠杆，估算杠杆系数。
- 边界要求：① 工具杠杆系数 = 使用人数（每资产：工具名/使用团队数）；② 机制杠杆 = 资产是否“不在场仍被执行”（inPlace: bool）；③ 知识杠杆 = 文档引用数+带出独立人数；④ 决策杠杆 = 季度关键决策参与数；⑤ 总杠杆系数输出+休假测试判定（工具+机制系数 ≥5 判杠杆健康）。

**答**：
```javascript
function leverageAudit(myAssets) {
  const toolK = myAssets.tools.reduce((a, t) => a + t.teamsUsing, 0);
  const mechK = myAssets.mechanisms.filter(m => m.inPlace).length;
  const knowK = myAssets.docs.reduce((a, d) => a + d.citations, 0)
    + myAssets.menteesGrown;
  const decisionK = myAssets.quarterlyDecisions;
  const total = toolK + mechK + knowK + decisionK;
  const rows = [
    { type: '工具', k: toolK, note: `${myAssets.tools.length}个工具被${toolK}团队次使用` },
    { type: '机制', k: mechK, note: `${mechK}个机制不在场仍执行` },
    { type: '知识', k: knowK, note: `文档引用${knowK - myAssets.menteesGrown}+带出${myAssets.menteesGrown}人` },
    { type: '决策', k: decisionK, note: `季度关键决策参与${decisionK}次` },
  ];
  return { rows, total,
    vacationTest: (toolK + mechK) >= 5
      ? '休假测试通过：工具+机制杠杆健康'
      : `休假测试不通过（${toolK + mechK}/5）——产出全依赖在场`,
    weakest: rows.sort((a, b) => a.k - b.k)[0] };   // 最弱杠杆=优先补
}
```

**评分点**:
- 四类杠杆系数化（影响面被量化成数字——答辩素材直接生成）。
- 休假测试量化判定（在场依赖度可测）。
- 最弱杠杆识别（优先补齐方向）。

