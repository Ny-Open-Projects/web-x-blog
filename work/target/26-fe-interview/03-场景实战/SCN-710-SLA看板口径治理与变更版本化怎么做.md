---
title: [SCN-710] SLA 口径治理怎么做？口径一变趋势全断怎么办？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-710：SLA 口径治理怎么做？
**答**：
- 口准字典：每个指标一份口径卡（定义/计算公式/采样率/数据源/排除项/owner），看板图表点击「口径」可查——口径不透明是争议根源。
- 版本化：口径变更产生新版本（v2），历史数据保留 v1；趋势图支持「双版本拼接 + 断点标注」，禁止悄悄覆盖历史口径。
- 变更流程：口径变更需评审（影响所有相关 SLO/告警阈值联动更新）+ 双跑两周（新旧口径并行对比）+ 公告。
- 一致性校验：定期对账任务验证「SDK 口径 = 流侧口径 = 看板展示口径」，漂移即告警。
- 追问钩子：为什么要双跑——直接切换时你不知道差异是真实变化还是口径变化，双跑两周拿到映射关系后切换才有信心。

```javascript
const metricRegistry = {
  'ux.core_page.lcp_p95': {
    v1: { formula: 'p95(lcp)', sample: 0.1, exclude: ['bot'] },
    v2: { formula: 'p95(lcp where navigation_type=navigate)', sample: 0.2,    // v2 排除 bfcache
          since: '2026-11-01', dualRunUntil: '2026-11-15' },
  },
};
function renderSeries(metric, range) {
  const segments = splitByVersion(metric, range);    // 版本分段
  return segments.map((s, i) => ({
    data: query(s), breakAt: i > 0,                  // 断点标注口径切换
    note: `${s.v}：${metricRegistry[metric][s.v].formula}`,
  }));
}
```
