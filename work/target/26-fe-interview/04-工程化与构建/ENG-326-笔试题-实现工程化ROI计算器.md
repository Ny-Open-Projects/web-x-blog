---
title: [ENG-326] 笔试题——实现工程化 ROI 计算器（工时折算 + 事故成本）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## ENG-326：手写工程化 ROI

**需求与边界**：
- 需求：输入基线与改进后指标（构建时长/CI 时长/事故率/上线时长），输出年度 ROI——① 效率节省（人时折算）；② 事故避免价值（事故数差 × 单次成本）；③ 建设成本（人月 × 薪当量）；④ ROI = (节省+避免) / 成本。
- 边界：① 效率节省要乘频率（构建提速 × 每日构建次数 × 人数）；② 事故成本分档（P0/P1/P2 不同单价）；③ 无基线数据时显式警告（ENG-226：没有 before 的 ROI 是编的）。

**答**：
```javascript
function engRoi({ baseline, after, teamSize, buildFreqPerDay, incidents, engMonths, salaryEq }) {
  if (!baseline) return { error: 'NO_BASELINE', note: '先采样基线，否则 ROI 无从谈起' };
  const buildSaved = (baseline.buildMin - after.buildMin) / 60
    * buildFreqPerDay * teamSize * 220;                // 年工作日 220
  const ciSaved = (baseline.ciMin - after.ciMin) / 60 * 220;
  const incidentsAvoided = Math.max(0, baseline.incidentRate - after.incidentRate) * 220;
  const incidentValue = incidentsAvoided
    * (incidents.p0.cost * incidents.p0.weight + incidents.p1.cost * incidents.p1.weight);
  const cost = engMonths * salaryEq;
  const gain = (buildSaved + ciSaved + incidentValue) * HOURLY_COST;
  return {
    efficiencyHours: buildSaved + ciSaved,
    incidentValue, cost,
    roi: +(gain / cost).toFixed(2),
    narrative: `构建+CI 节省 ${(buildSaved + ciSaved).toFixed(0)} 人时/年，避免 ${incidentsAvoided.toFixed(1)} 次事故`,
  };
}
```

**评分点**:
- 节省乘频率折算（提速×频次×人数——ENG-226 公式）。
- 事故价值分档加权（P0/P1 成本不同）。
- 无基线显式 error（数据诚实性）。
- narrative 输出（面向管理层的语言）。
