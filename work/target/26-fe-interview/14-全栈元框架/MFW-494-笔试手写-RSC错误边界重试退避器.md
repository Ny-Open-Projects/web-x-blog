---
title: [MFW-494] 笔试：手写 RSC 错误边界重试退避器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-494：RSC 段错误重试退避器
**答**：实现 `retryWithBackoff(fn, { tries = 3, base = 200, signal })`：1) 指数退避重试：base × 2^i + 抖动（±20%——同时重试的请求会同步风暴，抖动打散）；2) 错误分类：网络类/5xx 可重试，4xx（除 429）不重试直接抛（重试不可恢复错误是浪费）；3) 429/503 尊重 Retry-After 头（有的话按头等，没有按退避）；4) signal 取消贯穿：每轮 await 前检查 aborted，取消立即抛（流式渲染取消传播，重试不能违反）。

```javascript
const RETRYABLE = /ECONNRESET|ETIMEDOUT|fetch failed/

export async function retryWithBackoff(fn, { tries = 3, base = 200, signal } = {}) {
  let lastErr
  for (let i = 0; i < tries; i++) {
    if (signal?.aborted) throw new DOMException('aborted', 'AbortError')
    try { return await fn() } catch (e) {
      lastErr = e
      const status = e.status || e.response?.status
      const unretryable = status && status >= 400 && status < 500 && status !== 429
      if (unretryable || i === tries - 1) throw e
      let wait = base * 2 ** i + base * 2 ** i * (Math.random() * 0.4 - 0.2) // 指数+抖动
      const ra = e.headers?.get?.('retry-after')
      if (status === 429 && ra) wait = Number(ra) * 1000 // 尊重服务端节流指令
      await sleep(Math.min(wait, 5000), signal)
    }
  }
  throw lastErr
}

function sleep(ms, signal) {
  return new Promise((res, rej) => {
    const t = setTimeout(res, ms)
    signal?.addEventListener('abort', () => { clearTimeout(t); rej(new DOMException('aborted', 'AbortError')) }, { once: true })
  })
}
```

**评分点**：
- 4xx（除 429）不重试（错误分类是重试器的正确性前提）
- 退避带 ±20% 抖动（防同步重试风暴打垮已故障依赖）
- Retry-After 优先于本地退避（429 语义尊重）
- signal 贯穿等待期（取消发生在 sleep 中也要立即退出）
