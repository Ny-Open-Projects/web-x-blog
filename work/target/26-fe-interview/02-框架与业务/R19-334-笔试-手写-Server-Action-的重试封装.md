---
title: [R19-334] 笔试：手写 Server Action 的重试封装（幂等 + 退避 + 上限）
date: 2026-11-19
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-334：笔试：手写 Server Action 的重试封装
**答**：实现 `retryAction(action, args, { retries = 2, backoff = 500 })`：网络错误（fetch failed / 5xx）重试带指数退避；业务错误（返回 ok:false）不重试；每次重试用新 requestId（幂等键固定为首次生成的，保证服务端去重）；最终失败抛出。

```javascript
async function retryAction(action, args, { retries = 2, backoff = 500 } = {}) {
  const requestId = args.requestId // 幂等键：所有重试共用
  let lastErr
  for (let i = 0; i <= retries; i++) {
    try {
      const res = await action({ ...args, requestId })
      if (!res.ok) return res          // 业务错误不重试，直接返回给 UI 处理
      return res
    } catch (e) {
      lastErr = e                      // 网络/5xx 错误才重试
      if (i < retries) await new Promise(r => setTimeout(r, backoff * 2 ** i))
    }
  }
  throw lastErr
}
```
**评分点**：
- 幂等键跨重试固定（服务端去重依赖）。
- 业务错误与网络错误的分类（前者不重试）。
- 指数退避。
- 最终抛出而非吞错。
