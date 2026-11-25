---
title: [NODE-980] 笔试题——实现降级预案回归测试（预案生效的自动验证）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-980：手写预案回归

**需求与边界**：
- 需求：预案回归（SCN-联想-890/980）——① 预案的自动验证（SCN-联想-890 探活）；② 预案的回归套件（CI——SCN-OPS-269）；③ 预案的失效告警（SCN-联想-890 P0）；④ 套件的覆盖度（SCN-OPS-279）。
- 边界：① 注入器联动（SCN-OPS-281）；② 合成标记（SCN-NODE-717）；③ 套件的 flaky 隔离（SCN-TST-218）。

**答**：
```javascript
async function degradeRegressionSuite() {
  const results = [];
  for (const card of playbookCards()) {                // 预案卡片（SCN-OPS-932）
    const r = await executeCardWithInjection(card, { synthetic: true, pct: 10 });   // 注入 + 合成（SCN-OPS-281/717）
    results.push({ card: card.id, pass: r.verified, flaky: r.flaky });
  }
  const broken = results.filter(r => !r.pass && !r.flaky);   // flaky 隔离（SCN-TST-218）
  if (broken.length) alert({ type: 'PLAYBOOK_BROKEN', cards: broken, level: 'block' });   // P0（SCN-联想-890）
  return { results, coverage: coverageCalc(results) };   // SCN-OPS-279
}
```

**评分点**:
- 预案卡片回归（SCN-OPS-932/联想-890）。
- 注入 + 合成标记（SCN-OPS-281/717）。
- flaky 隔离（SCN-TST-218）。
- 覆盖度（SCN-OPS-279）。
