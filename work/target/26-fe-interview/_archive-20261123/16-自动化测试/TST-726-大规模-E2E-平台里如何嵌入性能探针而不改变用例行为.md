---
title: [TST-726] 大规模 E2E 平台里如何嵌入性能探针而不改变用例行为
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-726：大规模 E2E 平台里如何嵌入性能探针而不改变用例行为

**答**：
- 结论：性能探针要「无侵入采集」——通过浏览器 CDP/Performance API 旁路采集，不修改页面 DOM 与用例步骤。
- 采集 Point：导航时长、LCP、长任务、资源瀑布，用 Observer + 事件监听，避免主动注入脚本改变时序。
- 探针本身有开销，要做 A/B 校验：开关探针对比确认对功能用例通过率无影响。
- 追问钩子：探针采集到的数据与专项性能工具差异大，如何取舍？

```javascript
// 旁路性能探针：PerformanceObserver 采集 LCP
function startProbe(onMetric) {
  const po = new PerformanceObserver(list => {
    for (const e of list.getEntries()) {
      onMetric({ name: e.name, start: e.startTime, dur: e.duration });
    }
  });
  po.observe({ type: 'largest-contentful-paint', buffered: true });
  return () => po.disconnect(); // 用例结束断开，避免跨用例污染
}
const stop = startProbe(m => console.log('LCP', m.start));
// stop();
```
