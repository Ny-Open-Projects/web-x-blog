---
title: [SOFT-660] 手写 impressionCheck：五维周检（靠谱/响应/会议/沉淀/情绪）、负面信号当周修复项生成？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-660：手写 impressionCheck：五维周检（靠谱/响应/会议/沉淀/情绪）、负面信号当周修复项生成

**需求与边界**：
- 实现 impressionCheck(week)。
- 边界要求：① 五维数据源：承诺账本（兑现率）/消息样本（三要素齐全率）/会议记录（有准备发言次数）/文档产出（署名数）/压力事件（自评）；② 每维 0~2 分（0=需修复/1=及格/2=良好），总分 <6 触发修复项；③ 修复项生成具体动作（如靠谱度 0 → "补齐逾期承诺+本周零新承诺"）；④ 周对比（环比改善/恶化）。

**答**：
```javascript
function impressionCheck(week, data) {
  const scores = {
    reliable: data.promises.kept / Math.max(data.promises.total, 1) >= 0.95 ? 2
      : data.promises.kept / Math.max(data.promises.total, 1) >= 0.8 ? 1 : 0,
    response: data.messages.complete / Math.max(data.messages.total, 1) >= 0.8 ? 2
      : data.messages.total > 0 ? 1 : 2,
    meeting: data.preparedSpeeches >= 1 ? 2 : data.meetings > 0 ? 1 : 2,
    docs: data.signedDocs >= 2 ? 2 : data.signedDocs >= 1 ? 1 : 0,
    composure: data.pressureEvents.filter(e => e.handled).length
      === data.pressureEvents.length ? 2 : 0,
  };
  const total = Object.values(scores).reduce((a, b) => a + b, 0);
  const fixes = [];
  if (scores.reliable === 0)
    fixes.push('补齐逾期承诺并主动同步；本周只接确定性承诺');
  if (scores.response <= 1)
    fixes.push('消息用三要素模板（事+动作+截止）');
  if (scores.meeting <= 1)
    fixes.push('下次会前准备1个有数据的发言点');
  if (scores.docs === 0)
    fixes.push('本周沉淀1篇署名文档');
  if (scores.composure === 0)
    fixes.push('复盘压力事件应对；重大沟通前冷却24h');
  return { week, scores, total,
    verdict: total < 6 ? '需修复' : total >= 8 ? '良好' : '及格',
    fixes, prev: comparePrev(week) };               // 环比
}
```

**评分点**:
- 五维数据源客观（从账本/消息/记录取数而非自评主观分）。
- 修复项具体可执行（每条是动作不是口号）。
- 环比对比（趋势可见，负面当周修复）。

