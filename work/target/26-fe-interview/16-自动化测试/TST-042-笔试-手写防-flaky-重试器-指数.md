---
title: [TST-042] 笔试：手写防 flaky 重试器（次数上限 + 退避 + 结果记录）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-042：笔试：手写防 flaky 重试器（次数上限 + 退避 + 结果记录）
**答**：
- 需求：实现 `retry(task, { retries, backoff })`：失败按指数退避重试（1s→2s→4s…上限封顶），全部失败抛最后一次错误；返回值带 attempt 记录供 flaky 报告使用。
- 核心：循环尝试 + await sleep(backoff * 2^n)；成功提前返回并带 attempts 计数；每次失败记录耗时与错误。
- 边界：retries=0 只跑一次；task 抛非可重试错误（如断言失败 Error 标记 `err.fatal`）应立即中止；重试期间要清理前次残留（由 task 自己保证幂等，文档注明）。

```javascript
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function retry(task, { retries = 3, backoff = 1000, cap = 8000 } = {}) {
  const log = [];
  let attempt = 0;
  while (true) {
    const start = Date.now();
    try {
      const result = await task(attempt);
      log.push({ attempt, ms: Date.now() - start, ok: true });
      return { result, attempts: attempt + 1, log };
    } catch (e) {
      log.push({ attempt, ms: Date.now() - start, ok: false, err: e.message });
      if (e.fatal) throw e;                                   // 断言类错误不重试
      if (attempt >= retries) { e.log = log; throw e; }       // 耗尽抛最后错误
      await sleep(Math.min(backoff * 2 ** attempt, cap));     // 1s 2s 4s… 封顶
      attempt++;
    }
  }
}

// ---- 用法 ----
let flakyCount = 0;
const { result, attempts, log } = await retry(async (n) => {
  if (n < 2) throw new Error('timeout of 30000ms exceeded'); // 前两次失败
  return 'ok';
}, { retries: 3, backoff: 100 });
console.log(result, attempts);   // ok 3
console.log(log.length);         // 3 条记录，含每次耗时 —— 供 flaky 看板消费

try {
  await retry(async () => { const e = new Error('assert failed'); e.fatal = true; throw e; });
} catch (e) {
  console.log('fatal 不重试：', e.message);
}
```
**评分点**：
- 指数退避 + 上限封顶（裸 sleep 循环不给满分）。
- fatal 错误短路：知道「断言失败不该重试」是关键工程判断。
- attempts/log 记录支持 flaky 治理（重试后通过的用例要进清单）。
- 提到重试要求 task 幂等。
