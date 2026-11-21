---
title: [RBL-184] 笔试：手写 flaky 检测重试器（失败→重试→标记）
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-184：笔试：手写 flaky 检测重试器（失败重试与 flaky 标记）

**题目**：写 retry-flaky.mjs：1) 输入测试命令执行器（返回 {file, ok}）与文件列表；2) 首轮全量跑，失败的文件进入重试池；3) 重试至多 2 次：仍失败 → 真 failed；重试后通过 → 标记 flaky 并计入报告；4) 输出报告：failed/flaky/passed 文件清单；5) flaky 文件写入 .flaky-report.json（跨次构建累计，次数 ≥ 3 自动升级为 CI 失败，防 flaky 被永远容忍）。

```javascript
// retry-flaky.mjs
import { readFileSync, writeFileSync } from 'node:fs';

export async function runWithRetry(runner, files, { maxRetries = 2, flakyLimit = 3 } = {}) {
  const passed = [], flaky = [], failed = [];
  let pool = files;
  for (let round = 0; round <= maxRetries && pool.length; round++) {
    const results = await Promise.all(pool.map(f => runner(f))); // 每轮并发跑
    pool = results.filter(r => !r.ok).map(r => r.file);
    const ok = results.filter(r => r.ok).map(r => r.file);
    if (round === 0) passed.push(...ok);
    else { flaky.push(...ok); passed.push(...ok); }             // 重试才过的都是 flaky
  }
  failed.push(...pool);

  // 历史 flaky 追踪：连续/累计次数达阈值则升级为失败
  let history = {};
  try { history = JSON.parse(readFileSync('.flaky-report.json', 'utf8')); } catch {}
  const upgraded = [];
  for (const f of flaky) {
    history[f] = (history[f]?.count ?? 0) + 1;
    if (history[f].count >= flakyLimit) { upgraded.push(f); failed.push(f); }
  }
  for (const f of Object.keys(history))
    if (!flaky.includes(f) && !failed.includes(f)) delete history[f]; // 过关一次清零
  writeFileSync('.flaky-report.json', JSON.stringify(history, null, 2));

  return { passed, flaky, failed, upgraded };
}
// 报告输出示例：
// PASS 42 | FLAKY 2 (react-list.test.ts, search.test.ts) | FAIL 1 (checkout.test.ts)
// flaky 升级：search.test.ts 累计第 3 次 → 本轮按 FAIL 处理
```
**评分点**：
- 重试轮次有上限（默认 2），不是无限重试。
- flaky 判定语义正确：首轮失败、重试通过。
- 历史 flaky 计数 + 阈值升级（防 flaky 常态化），过关清零。
- 真 failed 不重试池残留错误（最终 failed 集完整）。
- 报告三类清单齐全，CI 可据此发飞书/Slack 通知。
