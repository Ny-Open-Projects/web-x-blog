---
title: [SOFT-800] 手写 influenceAudit：四层影响力证据盘点、层级映射、跳级预警、年度对比？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-800：手写 influenceAudit：四层影响力证据盘点、层级映射、跳级预警、年度对比

**需求与边界**：
- 实现 influenceAudit(evidence)。
- 边界要求：① evidence 按四层组织（team/dept/company/industry），每层条目含 { desc, verifiable }（可验证性字段——不可验证的证据不计入）；② 层级完整度：每层 ≥1 条可验证证据才算“立住”；③ 跳级预警：下层为空但上层有证据（industry 有而 team 空——空中楼阁警告 SOFT-781）；④ 年度对比：与去年数据对比增量；⑤ 输出映射目标等级的建议。

**答**：
```javascript
function influenceAudit(evidence, { targetLevel = 'P7', lastYear } = {}) {
  const LAYERS = ['team', 'dept', 'company', 'industry'];
  const LEVEL_MAP = { P6: 1, P7: 2, P8: 3 };        // 需要立住的层数
  const needed = LEVEL_MAP[targetLevel] ?? 2;
  const rows = LAYERS.map(layer => {
    const items = (evidence[layer] ?? []).filter(e => e.verifiable);
    return { layer, count: items.length,
      established: items.length >= 1 };             // ≥1条可验证=立住
  });
  const establishedCount = rows.filter(r => r.established).length;
  const skip = LAYERS.findIndex(l => !rows.find(r => r.layer === l).established);
  const jumpRisk = skip >= 0 && rows.slice(skip + 1)
    .some(r => r.established)
    ? `跳级预警：「${LAYERS[skip]}」层空但更高层有证据——空中楼阁（SOFT-781）`
    : null;
  const delta = lastYear ? LAYERS.map(l => {
    const cur = rows.find(r => r.layer === l).count;
    return { layer: l, delta: cur - (lastYear[l] ?? 0) };
  }) : null;
  const establishedLayers = rows.slice(0, needed)
    .filter(r => r.established).length;
  return { rows,
    readyForTarget: establishedLayers >= needed
      ? `目标${targetLevel}影响力层级达标（${establishedLayers}/${needed}层）`
      : `未达标：${needed - establishedLayers}层缺口——先立低层`,
    jumpRisk, delta };
}
```

**评分点**:
- 可验证性过滤（不可验证的证据不计——SOFT-799 反虚荣）。
- 跳级预警（下层空上层有=空中楼阁检测）。
- 层级映射目标等级（影响力层级与晋升标尺对齐 SOFT-781）。

