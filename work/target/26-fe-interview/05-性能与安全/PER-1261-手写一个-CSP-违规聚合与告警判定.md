---
title: [PER-1261] 手写一个 CSP 违规聚合与告警判定器
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1261：手写一个 CSP 违规聚合与告警判定器

**答**：
- 需求：实现 cspAlerts(reports, { windowMs = 3600_000, threshold = 10 } = {})。reports 为 [{ ts, directive, blockedURL, sourceFile }]；按 directive+host 聚合，窗口内 count > threshold 触发告警 { key, count, sample }；输出 alerts 按 count 降序；已知误报（sourceFile 含 extension）排除。
- 边界：blockedURL 相对路径按 location 归 host；空 reports 返回 []；sample 只留 1 条。
- 评分点：聚合 key；窗口过滤；扩展排除；阈值告警

```javascript
function cspAlerts(reports, { windowMs = 3600_000, threshold = 10 } = {}) {
  const now = Date.now();
  const groups = {};
  for (const r of reports) {
    if ((r.sourceFile ?? '').includes('extension')) continue;   // 浏览器扩展误报
    if (now - r.ts > windowMs) continue;
    let host;
    try { host = new URL(r.blockedURL, location.href).host; }
    catch { host = 'unknown'; }
    const key = `${r.directive}|${host}`;
    (groups[key] ??= { count: 0, sample: null }).count++;
    groups[key].sample ??= { source: r.sourceFile, url: r.blockedURL };
  }
  return Object.entries(groups)
    .filter(([, v]) => v.count > threshold)
    .map(([key, v]) => ({ key, count: v.count, sample: v.sample }))
    .sort((a, b) => b.count - a.count);
}
```
