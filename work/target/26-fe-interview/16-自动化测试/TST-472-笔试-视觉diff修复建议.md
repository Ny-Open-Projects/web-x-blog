---
title: [TST-472] 笔试：视觉 diff 后自动生成「修复建议」（基于差异区域特征）。
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-472：笔试：视觉 diff 后自动生成「修复建议」（基于差异区域特征）。
**题目**：diff 结果 `{regions: [{x, y, w, h, kind: 'shift'|'color'|'missing'}]}`。规则：shift → 建议查布局/间距 token；color → 查主题 token 映射；missing → 查条件渲染/加载失败。输出建议清单（按区域面积降序）。

```javascript
const SUGGEST = {
  shift: '检查布局（margin/padding token 或 flex 容器变化）',
  color: '检查颜色 token 映射（主题切换遗漏）',
  missing: '检查条件渲染/图片加载（资源 404？）',
};
function visualAdvice(diff) {
  if (!diff.regions.length) return { clean: true };
  return { clean: false,
    advice: [...diff.regions].sort((a, b) => b.w * b.h - a.w * a.h)
      .map(r => `区域(${r.x},${r.y},${r.w}x${r.h}) ${r.kind} → ${SUGGEST[r.kind]}`) };
}

```

**评分点**：
- kind→建议映射表。
- 面积加权排序（大差异优先）。
- 区域坐标保留（定位到组件）。
- 无差异输出 clean。
