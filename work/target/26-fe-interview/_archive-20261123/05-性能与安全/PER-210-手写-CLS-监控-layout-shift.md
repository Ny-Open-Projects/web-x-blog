---
title: [PER-210] 笔试题：手写 CLS 监控（layout-shift 事件聚合、hadRecentInput 过滤与会话窗口）
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-210：手写 CLS 监控（layout-shift 事件聚合、hadRecentInput 过滤与会话窗口）

**题目**：实现 `trackCLS(report)`：① 过滤 `hadRecentInput === true` 的位移；② 按会话窗口聚合：窗口内位移连续间隔 < 1s 且窗口总时长 ≤ 5s，取所有窗口中累计最大值；③ 页面 hidden 时上报。

**答**：CLS 不是所有位移之和，而是"最大会话窗口 burst"。需要维护当前窗口（startTime/累计值/上次位移时间），窗口断开时与最大值比较替换。

```javascript
function trackCLS(report) {
  let sessionValue = 0, sessionStart = 0, lastShift = 0, maxSession = 0, reported = false;
  let sourcesOfMax = [];

  new PerformanceObserver((list) => {
    for (const e of list.getEntries()) {
      if (e.hadRecentInput) continue;              // 用户输入后 500ms 内不计
      const t = e.startTime;
      if (sessionValue === 0 || t - lastShift > 1000 || t - sessionStart > 5000) {
        if (sessionValue > maxSession) maxSession = sessionValue;   // 收口旧窗口
        sessionValue = 0; sessionStart = t; sourcesOfMax = [];
      }
      sessionValue += e.value; lastShift = t;
      if (sessionValue > maxSession) sourcesOfMax = (e.sources || []).map(s => s.node?.nodeName).filter(Boolean);
    }
    if (sessionValue > maxSession) maxSession = sessionValue;
  }).observe({ type: 'layout-shift', buffered: true });

  const flush = () => { if (!reported && maxSession > 0) { reported = true;
    report({ type: 'CLS', value: maxSession, sources: sourcesOfMax }); } };
  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'hidden') flush();
  });
  addEventListener('pagehide', flush);
}
```

**评分点**：
- `hadRecentInput` 过滤正确（不过滤会把用户主动触发的展开当成抖动）。
- 会话窗口逻辑正确：1s 间隔断开、5s 上限，取最大 burst 而非总和。
- 带位移来源（`sources[].node`）上报，能直接定位抖动元素。
- hidden/pagehide 兜底上报，避免卸载丢数。
