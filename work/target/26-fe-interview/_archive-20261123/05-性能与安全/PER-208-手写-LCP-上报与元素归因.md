---
title: [PER-208] 笔试题：手写 LCP 采集上报，并附带元素与最终性判定（含 bfcache 与隐藏页处理）
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-208：手写 LCP 采集上报，并附带元素与最终性判定（含 bfcache 与隐藏页处理）

**题目**：实现 `trackLCP(report)`：① 取最后一次 LCP 候选作为最终值；② 上报时附带元素 tag、候选次数与是否页面隐藏后停止采集；③ 页面进入 hidden 后不再累计新候选；④ bfcache 恢复（pageshow persisted）时重置。

**答**：要点是"取最后候选"（LCP 是不断被更大元素取代的过程）、hidden 即冻结（后台页的 LCP 无意义）、`pagehide/pageshow` 生命周期兜底。

```javascript
function trackLCP(report) {
  let final = null, count = 0, frozen = false;

  const obs = new PerformanceObserver((list) => {
    if (frozen) return;
    const es = list.getEntries();
    const last = es[es.length - 1];
    if (!last) return;
    count++;
    final = {
      value: last.startTime,
      tag: last.element?.tagName ?? '',
      url: last.url || '',
      candidates: count,
    };
  });
  obs.observe({ type: 'largest-contentful-paint', buffered: true });

  const flush = (reason) => {
    if (final && !reported) report({ ...final, reason, type: 'LCP' });
    reported = !!final;
  };
  let reported = false;

  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'hidden') { frozen = true; flush('hidden'); }
  });
  addEventListener('pagehide', () => flush('pagehide'));
  addEventListener('pageshow', (e) => {          // bfcache 恢复：旧指标已上报过，重置采集
    if (e.persisted) { frozen = false; final = null; reported = false; count = 0; obs.takeRecords(); }
  });
}
```

**评分点**：
- 取"最后一次候选"而非第一条（误取首条会导致 LCP 严重偏低）。
- hidden 冻结 + 首次上报去重（reported 标记），避免重复或后台页污染数据。
- bfcache `pageshow persisted` 重新采集，否则恢复页沿用旧值。
- 上报附 element/url 便于归因，candidates 次数可判断 LCP 是否被反复替换。
