---
title: [RBL-430] 笔试：手写发布前 Checklist 执行器
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-430：手写发布前 Checklist 执行器
**答**：实现 `runChecklist(items, { manifest, ci })`：1) items：`[{ name, run: async (ctx) => { ok, detail }, blocking, timeoutMs }]`；2) 并行执行 + 各自超时（超时=失败防挂死）；3) blocking 分级：blocking 失败 → 拒绝发布；非 blocking 失败 → 警告收集；4) 白名单豁免：`{ check, issue, until }`——过期豁免无效；5) 结果持久化（发布记录关联 checklist 结果——审计链）；6) 输出人类报告（PASS/FAIL/WARN 表格）。

```javascript
async function withTimeout(promise, ms, name) {
  let timer
  try {
    return await Promise.race([promise, new Promise((_, rej) =>
      timer = setTimeout(() => rej(new Error(`${name} timeout ${ms}ms`)), ms))])
  } finally { clearTimeout(timer) }
}

export async function runChecklist(items, ctx, { whitelist = [], timeoutMs = 30_000 } = {}) {
  const now = Date.now()
  const results = await Promise.all(items.map(async (item) => {
    try {
      const r = await withTimeout(item.run(ctx), item.timeoutMs ?? timeoutMs, item.name)
      const exempt = whitelist.find((w) => w.check === item.name && new Date(w.until) > now)
      return { name: item.name, ...r, blocking: item.blocking ?? true,
        status: r.ok ? 'PASS' : exempt ? 'EXEMPT' : 'FAIL', exempt }
    } catch (e) {
      return { name: item.name, ok: false, detail: String(e), blocking: item.blocking ?? true, status: 'FAIL' }
    }
  }))
  const failures = results.filter((r) => r.status === 'FAIL' && r.blocking)
  const report = results.map((r) =>
    `| ${r.name} | ${r.status} | ${r.detail ?? ''} |${r.exempt ? ` issue:${r.exempt.issue}` : ''}`)
  return {
    pass: failures.length === 0,
    results,
    md: ['| 检查 | 结果 | 详情 |', '|---|---|---|', ...report].join('\n'),
  }
}
```
**评分点**：
- 并行 + 独立超时（超时=失败防挂死流水线）
- 三态结果（PASS/FAIL/EXEMPT）+ 豁免过期判定（until 过期无效）
- blocking 分级（阻断 vs 警告——不是所有失败都拦发布）
- 审计关联（结果随发布记录持久化）
