---
title: [PER-892] 手写一个 CDN 质量对比器：多 CDN 分域名统计耗时与失败率输出调度建议
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-892：手写一个 CDN 质量对比器：多 CDN 分域名统计耗时与失败率输出调度建议

**答**：
- 需求：实现 cdnCompare(records)：records 为 [{cdn, path, ms, ok, ts}]；按 CDN 聚合输出：请求量、成功率、耗时 p50/p75、最近 1 小时失败率；输出调度建议：成功率 < 99% 且样本 >= 50 的 CDN 标记 avoid；耗时 p75 最低且成功率 >= 99% 的标记 preferred。
- 边界：无请求样本的 CDN 输出 no-data；失败率按滑动 1 小时窗计算；建议输出含依据数据。
- 评分点：滑动窗口失败率；条件判定完整；建议带依据。

```javascript
function cdnCompare(records, { minSample = 50 } = {}) {
  const now = Date.now();
  const by = {};
  for (const r of records) {
    const s = by[r.cdn] ??= { n: 0, ok: 0, ms: [], recent: [] };
    s.n++; if (r.ok) s.ok++;
    if (r.ok) s.ms.push(r.ms);
    if (now - r.ts < 3600000) s.recent.push(r);                // 最近 1 小时
  }
  const rows = Object.entries(by).map(([cdn, s]) => ({
    cdn, n: s.n,
    successRate: +(s.ok / s.n).toFixed(4),
    failRecent: s.recent.length ? +(s.recent.filter(r => !r.ok).length / s.recent.length).toFixed(4) : 0,
    p50: p(pct(s.ms, 0.5)), p75: p(pct(s.ms, 0.75)),
  }));
  const preferred = rows.filter(r => r.successRate >= 0.99).sort((a, b) => a.p75 - b.p75)[0];
  return { rows,
    advice: rows.map(r => ({
      cdn: r.cdn,
      tag: r.n < minSample ? 'no-data' : r.successRate < 0.99 ? 'avoid' :
        preferred?.cdn === r.cdn ? 'preferred' : 'ok',
      basis: `成功率 ${r.successRate} / p75 ${r.p75}ms / 近1h失败率 ${r.failRecent}`,
    })) };
}
function pct(a, q) { if (!a?.length) return null; const s = [...a].sort((x, y) => x - y);
  return s[Math.floor(s.length * q)]; }
function p(v) { return v == null ? null : +v.toFixed(1); }
```
