---
title: [950] 笔试手写：实现带重试、超时、降级链的任务执行器
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, 多Agent, 容错]
type: 笔试题
---

## 950：笔试手写：实现带重试、超时、降级链的任务执行器

**答**：实现 runWithFallback(fn, opts)：{ retries=2, backoffBase=300, timeoutMs=5000, fallbacks=[fn2, fn3] }。主函数按 retries 指数退避重试；单次尝试受 timeoutMs 约束（超时算失败）；全部失败后依次尝试 fallbacks（每个也受超时约束）；所有路径失败抛 AggregateError 收集各次错误。要求不留下悬挂的定时器泄漏。

```js
async function attempt(fn, timeoutMs) {
  let timer;
  const t = new Promise((_, rej) => { timer = setTimeout(() => rej(new Error('timeout')), timeoutMs); });
  try {
    return await Promise.race([fn(), t]);
  } finally { clearTimeout(timer); }          // 防定时器泄漏
}
async function runWithFallback(fn, opts = {}) {
  const { retries = 2, backoffBase = 300, timeoutMs = 5000, fallbacks = [] } = opts;
  const errors = [];
  const fns = [fn, ...fallbacks];
  for (let fi = 0; fi < fns.length; fi++) {
    for (let i = 0; i <= retries; i++) {
      try { return await attempt(fns[fi], timeoutMs); }
      catch (e) {
        errors.push(new Error(`fn${fi}#try${i}: ${e.message}`));
        if (i < retries) await new Promise(r => setTimeout(r, backoffBase * 2 ** i));
      }
    }
  }
  throw new AggregateError(errors, 'all attempts failed');
}
const r = await runWithFallback(() => Promise.reject(new Error('x')), {
  retries: 1, timeoutMs: 100, fallbacks: [async () => 'fallback-ok'],
});
console.log(r); // 'fallback-ok'
```

**评分点**：
- 超时用 Promise.race 且 clearTimeout 防泄漏（漏 clear 是高频扣分点）
- 指数退避公式 backoffBase * 2^i，最后一次失败后不等待
- 降级链语义正确：主函数耗尽重试才走 fallback，每个 fallback 独立享受超时
- AggregateError 收集全路径错误，可观测性好；能说出为什么不用 Promise.any（需要对每次失败记录重试上下文）

