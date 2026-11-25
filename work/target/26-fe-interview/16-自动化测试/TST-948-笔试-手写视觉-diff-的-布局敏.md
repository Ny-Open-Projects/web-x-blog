---
title: [TST-948] 笔试：手写视觉 diff 的「布局敏感分级器」——区分位移/尺寸变化与纯颜色变化
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-948：笔试：手写视觉 diff 的「布局敏感分级器」——区分位移/尺寸变化与纯颜色变化
**答**：
- 需求：实现 classifyDiff(diffs)，diffs = [{ type:'bbox'|'color', delta, element }][]。
- 规则：含 bbox 变化（位置/尺寸）判为 layout-shift 级（高优先级）；仅 color 变化且 delta<阈值判为 cosmetic（低优先级）；两者都有取最高级。
- 边界：delta 为相对变化比例；纯文本颜色变化也算 cosmetic；返回 { level, blockers, cosmetics }。

```javascript
function classifyDiff(diffs, colorThreshold = 0.3) {
  const blockers = [], cosmetics = [];
  for (const d of diffs) {
    if (d.type === 'bbox') blockers.push({ element: d.element, delta: d.delta });
    else if (d.type === 'color' && d.delta >= colorThreshold)
      blockers.push({ element: d.element, delta: d.delta, note: '颜色变化超阈值' });
    else cosmetics.push({ element: d.element, delta: d.delta });
  }
  return {
    level: blockers.length ? 'layout-shift' : (cosmetics.length ? 'cosmetic' : 'none'),
    blockers, cosmetics,
  };
}
console.log(classifyDiff([
  { type: 'bbox', delta: 0.02, element: '#buy' },
  { type: 'color', delta: 0.1, element: '.title' },
]).level); // 'layout-shift' → 高优先级，阻塞
```
**评分点**：
- bbox 变化（位置/尺寸）判为 layout-shift 高优先级。
- 仅颜色且 delta 低于阈值判为 cosmetic 低优先级。
- 颜色变化超阈值升级为 blocker，规则准确。
- 返回 blockers/cosmetics 分组，便于门禁分流。
