---
title: [RBL-191] 笔试：手写 PR 构建报告生成器（聚合多 job 结果为一条评论）
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-191：笔试：手写 PR 构建报告生成器（聚合多 job 结果为一条评论）

**题目**：写 pr-report.mjs：1) 输入多 job 结果数组（{job, status, durationSec, cacheHit, failedFiles?, sizeDelta?}）；2) 生成 markdown：状态总览表（图标 ✅/❌/⏭️）、总墙钟时间、缓存命中情况、产物体积变化、失败文件清单（可折叠 `<details>`）；3) 幂等：同一 PR 重复运行应更新而非追加（输出 signature 供查找已有评论）；4) 顶部摘要行：全绿或"3 个 job 失败"一句话；5) 数据缺失的 job 显示 skipped。

```javascript
// pr-report.mjs
const ICON = { success: '✅', failed: '❌', cancelled: '🚫', skipped: '⏭️' };
const fmtS = s => s >= 60 ? `${Math.floor(s / 60)}m${s % 60}s` : `${s}s`;

export function prReport(results, extra = {}) {
  const ran = results.filter(r => r.status !== 'skipped');
  const failedJobs = ran.filter(r => r.status === 'failed');
  const head = failedJobs.length
    ? `## ❌ 构建报告：${failedJobs.length} 个 job 失败`
    : `## ✅ 构建报告：全部通过`;

  const wallClock = Math.max(...ran.map(r => r.durationSec)); // 并行墙钟取 max
  const hit = ran.filter(r => r.cacheHit).length;

  const rows = results.map(r => [
    `| ${r.job} | ${ICON[r.status] ?? '❔'} ${r.status} | ${r.status === 'skipped' ? '-' : fmtS(r.durationSec)} |`,
  ].join(''));

  const parts = [
    head,
    '',
    `**墙钟** ${fmtS(wallClock)}（并行 max）· **缓存命中** ${hit}/${ran.length}`,
    '',
    '| Job | 状态 | 耗时 |', '|---|---|---|',
    ...rows,
  ];
  if (extra.sizeDelta != null)
    parts.push('', `**产物 gzip 体积**：${extra.sizeDelta >= 0 ? '+' : ''}${(extra.sizeDelta / 1024).toFixed(1)}KB`);
  const fails = results.filter(r => r.failedFiles?.length);
  if (fails.length) {
    parts.push('', '<details><summary>失败文件清单</summary>', '');
    for (const f of fails) parts.push(`- ${f.job}: ${f.failedFiles.map(x => '`' + x + '`').join(', ')}`);
    parts.push('', '</details>');
  }
  // 幂等签名：job 集合 + PR 号 → 用于查找/更新已有评论而非新增
  const signature = `build-report:${extra.pr ?? 0}:${ran.map(r => r.job).sort().join(',')}`;
  return { markdown: parts.join('\n'), signature, failed: failedJobs.length };
}

const results = [
  { job: 'lint', status: 'success', durationSec: 42, cacheHit: true },
  { job: 'build', status: 'failed', durationSec: 180, cacheHit: false, failedFiles: ['src/pay.tsx'] },
  { job: 'e2e', status: 'skipped', durationSec: 0, cacheHit: false },
];
console.log(prReport(results, { pr: 1234, sizeDelta: 8192 }).markdown);
```
**评分点**：
- 墙钟用 max（并行），不是求和。
- 状态图标映射含 skipped/cancelled。
- 失败清单用 details 折叠（评论可读性）。
- signature 幂等更新（防同一 PR 刷屏）。
- 摘要行结论先行。
