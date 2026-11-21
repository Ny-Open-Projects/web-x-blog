---
title: [WEB-493] 笔试：手写 CSP 违规收集器与治理面板
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 笔试题, 安全]
type: 笔试题
---

## WEB-493：笔试：手写 CSP 违规收集器与治理面板

**题目**：前端监听 CSP 违规事件（SecurityPolicyViolationEvent），按 `violatedDirective + blockedURL` 去重聚合并上报；提供本地 console 汇总方法。

**答**：
```javascript
const cspAgg = new Map();

document.addEventListener('securitypolicyviolation', (e) => {
  const key = `${e.violatedDirective}|${e.blockedURL || e.sourceFile || 'inline'}`;
  const rec = cspAgg.get(key) || { count: 0, sample: null };
  rec.count++;
  rec.sample ??= { file: e.sourceFile, line: e.lineNumber, disposition: e.disposition };
  cspAgg.set(key, rec);
  if (rec.count === 1 || rec.count % 10 === 0) { // 首次与每 10 次上报，控量
    navigator.sendBeacon('/api/csp-report', JSON.stringify({
      directive: e.violatedDirective, url: key, count: rec.count,
      page: location.pathname,
    }));
  }
});

// 本地排查用：控制台一键汇总
window.cspSummary = () =>
  [...cspAgg.entries()].sort((a, b) => b[1].count - a[1].count)
    .forEach(([k, v]) => console.log(v.count, k));
```

**评分点**：
- 用 Map 按 directive+URL 去重聚合，避免高频违规打爆上报接口
- 上报控量策略（首次 + 每 N 次）
- disposition 字段（enforce/report）区分拦截与仅上报
- 能讲清 Report-Only 灰度 → 治理 → enforce 的落地顺序（加分）
