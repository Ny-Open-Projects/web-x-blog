---
title: [SOFT-700] 手写 defenseChecklist：六环节检查项、完成状态追踪、关键缺失阻断提示？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-700：手写 defenseChecklist：六环节检查项、完成状态追踪、关键缺失阻断提示

**需求与边界**：
- 实现 defenseChecklist(state)：六环节（资格/材料/演练/临场/复盘预案/配合）检查项。
- 边界要求：① 每环节 3~5 项硬检查（资格确认/PPT三版本一致/致命问题清零/设备三备份/失败预案/领导过材料）；② 生成完成度（按环节加权——材料与演练权重最高）；③ 阻断提示：核心项（资格/致命清零/领导过材料）未完成则“不建议上场”；④ 输出可勾选清单（checkbox 格式）。

**答**：
```javascript
function defenseChecklist(state) {
  const CHECKS = {
    qualify: { w: 1, items: ['年限绩效门槛核对', '能力模型自评>80%', '时机四因素评估'], core: [0] },
    material: { w: 3, items: ['主线四段一致', '三版本数据同源', '自足性陌生人测试', '证据包索引+UNPROVEN清零', '口径三要素全标注'], core: [1, 4] },
    drill: { w: 3, items: ['mock×3（含严苛场）', '致命问题清零', '录像自查口头禅', '答案卡×10背熟'], core: [1] },
    live: { w: 2, items: ['15min时间轴排练', '设备三备份', '呼吸/锚定动作', '盲区三段式预案'], core: [1] },
    contingency: { w: 1, items: ['最坏预案写下来', '失败复盘模板备好'], core: [] },
    sync: { w: 2, items: ['材料过领导', '弹药包给足', '预审意见已改'], core: [0] },
  };
  const rows = Object.entries(CHECKS).map(([k, cfg]) => {
    const done = cfg.items.filter((it, i) =>
      state[k]?.[i] === true);
    const coreMiss = cfg.core.filter(i => !state[k]?.[i]);
    return { phase: k, done: done.length, total: cfg.items.length,
      weighted: (done.length / cfg.items.length) * cfg.w,
      coreMiss };
  });
  const totalW = Object.values(CHECKS).reduce((a, c) => a + c.w, 0);
  const doneW = rows.reduce((a, r) => a + r.weighted, 0);
  const blockers = rows.flatMap(r => r.coreMiss.map(i => ({
    phase: r.phase, item: CHECKS[r.phase].items[i] })));
  return { checklist: rows,
    readiness: Math.round(doneW / totalW * 100) + '%',
    verdict: blockers.length ? `不建议上场：核心缺失 ${blockers.map(b => b.item).join('；')}`
      : '核心项齐备，可上场' };
}
```

**评分点**:
- 六环节加权完成度（材料与演练权重最高——答辩成败主因）。
- 核心项阻断判定（资格/致命清零/领导过材料未完成禁止上场）。
- 输出直接可勾选（执行工具化）。

