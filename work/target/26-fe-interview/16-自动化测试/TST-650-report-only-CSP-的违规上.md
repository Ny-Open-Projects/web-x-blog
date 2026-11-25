---
title: [TST-650] report-only CSP 的违规上报链路怎么测？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-650：report-only CSP 的违规上报链路怎么测？

**答**：
- 结论：report-only 模式不拦截只上报，测试重点是「违规事件能否完整送达收集端」。
- 构造受控违规（内联脚本/非白名单图片），断言上报体含 directive、blocked-uri、source-file。
- 验证采样率与去重：同一违规短时间内只上报一次。
- 追问钩子：上报端点挂了，业务会有感知吗？怎么设计降级？

```javascript
function collectReports(reports, { dedupeMs = 1000 } = {}) {
  const seen = new Map(), out = [];
  reports.forEach(r => {
    const key = `${r.directive}|${r['blocked-uri']}`;
    const prev = seen.get(key);
    if (prev && r.ts - prev < dedupeMs) return;
    seen.set(key, r.ts);
    out.push({
      directive: r.directive,
      blockedUri: r['blocked-uri'],
      source: r['source-file'],
      complete: !!(r.directive && r['blocked-uri']),
    });
  });
  return out;
}
```
