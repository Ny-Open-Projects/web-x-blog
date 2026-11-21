---
title: [PER-238] 笔试题：手写 CrUX 多 origin 巡检脚本（批量查询、达标判定、失败重试与限速）
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-238：手写 CrUX 多 origin 巡检脚本（批量查询、达标判定、失败重试与限速）

**题目**：写一个 Node 脚本 `auditCrUX(origins, apiKey)`：① 并发查 CrUX API（限速：最多 3 并发，429 退避重试最多 3 次）；② 对 LCP/INP/CLS 按 p75 判定 good/ni/poor；③ 输出巡检报表数组 `{ origin, lcp, inp, cls, verdict }`；④ 单个 origin 失败不中断整体，错误记录在 results 里。

**答**：要点是并发池 + 指数退避 + 单项隔离。判定阈值：LCP≤2500、INP≤200、CLS≤0.1 为 good。

```javascript
const THRESH = { largest_contentful_paint: 2500, interaction_to_next_paint: 200, cumulative_layout_shift: 0.1 };

async function fetchWithRetry(url, body, retries = 3) {
  for (let i = 0; i <= retries; i++) {
    const res = await fetch(url, { method: 'POST', body: JSON.stringify(body) });
    if (res.status === 429) {                       // 限速退避：2^n 秒
      await new Promise(r => setTimeout(r, 2 ** i * 1000));
      continue;
    }
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return res.json();
  }
  throw new Error('重试耗尽');
}

async function pooled(origins, limit, worker) {     // 并发池
  const results = []; let i = 0;
  await Promise.all(Array.from({ length: limit }, async () => {
    while (i < origins.length) { const idx = i++; results[idx] = await worker(origins[idx]).catch(e => ({ origin: origins[idx], error: e.message })); }
  }));
  return results;
}

async function auditCrUX(origins, apiKey) {
  const url = `https://chromeuxreport.googleapis.com/v1/records:queryRecord?key=${apiKey}`;
  return pooled(origins, 3, async (origin) => {
    const rec = await fetchWithRetry(url, { origin, formFactor: 'PHONE' });
    const metrics = {};
    for (const [m, limit] of Object.entries(THRESH)) {
      const p75 = Number(rec.record.metrics[m]?.percentiles.p75 ?? NaN);
      metrics[m] = { p75, verdict: p75 <= limit ? 'good' : p75 <= limit * 2 ? 'ni' : 'poor' };
    }
    return { origin, ...metrics,
      verdict: Object.values(metrics).every(v => v.verdict === 'good') ? 'PASS' : 'FAIL' };
  });
}
```

**评分点**：
- 并发池实现正确（固定 worker 数循环取任务），不一次性打满并发。
- 429 指数退避重试，上限 3 次，重试耗尽抛错而非死循环。
- 单 origin 失败隔离（catch 记录 error，整体不中断）。
- 判定阈值与 CWV 官方口径一致（2500/200/0.1，三档划分）。
