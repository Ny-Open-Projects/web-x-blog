---
title: [SOFT-887] 手写 assetForms：单个案例素材的三形态维护（简历 STAR-Q/90秒话术/深挖问答卡）、一致性检查？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-887：手写 assetForms：单个案例素材的三形态维护（简历 STAR-Q/90秒话术/深挖问答卡）、一致性检查

**需求与边界**：
- 实现 assetForms(asset)。
- 边界要求：① asset 含 { starQ, pitch, qaCards } 三形态（SOFT-874）；② 一致性检查：三形态的事实字段（数字/口径/角色）必须一致（不一致列差异——SOFT-876 防注水与不一致）；③ qaCards 覆盖检查：≥3 张（设计取舍/贡献边界/数据口径——高频三问 SOFT-667）；④ 缺形态标 MISSING 生成补齐任务；⑤ 输出三形态可用状态。

**答**：
```javascript
function assetForms(asset) {
  const forms = ['starQ', 'pitch', 'qaCards'];
  const missing = forms.filter(f => !asset[f])
    .map(f => ({ form: f,
      task: { starQ: '从证据库生成STAR-Q条目（SOFT-862）',
        pitch: '写90秒话术版（框架+要点 SOFT-867）',
        qaCards: '生成≥3张问答卡（取舍/边界/口径 SOFT-700）' }[f] }));
  const diffs = [];
  if (asset.starQ && asset.pitch) {
    for (const k of ['metric', 'role']) {
      if (asset.starQ[k] !== asset.pitch[k])
        diffs.push({ field: k, starQ: asset.starQ[k],
          pitch: asset.pitch[k] });                 // 事实字段不一致
    }
  }
  const qaCount = asset.qaCards?.length ?? 0;
  const needQa = ['设计取舍', '贡献边界', '数据口径'];
  const qaGap = qaCount < 3
    ? `问答卡${qaCount}/3——补齐高频三问：${needQa.join('/')}（SOFT-667）`
    : null;
  return { missing, diffs,
    consistent: diffs.length === 0,
    qaGap,
    status: missing.length === 0 && diffs.length === 0 && !qaGap
      ? '三形态完备可用' : '补齐后再用于面试' };
}
```

**评分点**:
- 三形态结构（STAR-Q/90 秒/问答卡——SOFT-874 闭环的资产单元）。
- 跨形态事实一致性检查（数字/口径/角色不一致=注水信号）。
- 问答卡覆盖三问（设计取舍/贡献边界/数据口径——SOFT-667 高频）。

