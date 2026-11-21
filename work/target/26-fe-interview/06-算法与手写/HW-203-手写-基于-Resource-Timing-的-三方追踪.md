---
title: [HW-203] 手写三方资源追踪——按域归类三方资源（体积/阻塞/发现延迟），输出三方审计报表
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：三方资源审计自动化：Resource Timing 全量 → 按域归类（self/first-party 域集合之外）→ 每域聚合（体积/请求数/总时长/render-blocking 判定）→ 三方排行报表（PER-316 审计的自动化数据源）。

```javascript
function auditThirdParty(thresholds = {}) {
  const own = new Set([location.host, 'cdn.own.example.com']);   // 自有域白名单
  const byHost = new Map();
  for (const r of performance.getEntriesByType('resource')) {
    const host = new URL(r.name).host;
    if (own.has(host)) continue;
    const t = byHost.get(host) ?? { requests: 0, bytes: 0, duration: 0, blocking: 0 };
    t.requests++;
    t.bytes += r.transferSize ?? 0;
    t.duration += r.duration;
    // render-blocking 近似：initiatorType 为 script/css 且在首帧前完成
    if ((r.initiatorType === 'script' || r.initiatorType === 'css') && r.responseEnd < 3000) {
      t.blocking += r.duration;
    }
    byHost.set(host, t);
  }
  const rows = [...byHost].map(([host, t]) => ({ host, ...t,
    avg: Math.round(t.duration / t.requests) }))
    .sort((a, b) => b.bytes - a.bytes);
  report({ type: 'third-party-audit', rows });
  return rows;
}
// 输出示例：
// [{ host: 'chat.biz.io', requests: 3, bytes: 220000, blocking: 180, avg: 400 }, ...]
// 审计联动：bytes 排行 → facade 候选；blocking 排行 → 加载方式治理（PER-316 裁决表的数据源）
// 定期跑（周级）对比趋势：新三方域出现即告警（白名单外新增域检测，PER-316 CI 卡口的服务端版）
```

**评分点**：
- 域归类（own 白名单排除）+ 多维聚合（体积/时长/blocking）——本题核心。
- render-blocking 近似判定（initiatorType + 首帧前完成）。
- 排行输出直接对接审计裁决表（PER-316）。
- 周级趋势对比 + 新域出现告警的联动。
