---
title: [MFW-673] 笔试：手写 Action 重试决策器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-673：笔试：手写 Action 重试决策器

**答**：实现 `retryDecision(error, { idempotencyKey, attempt, maxRetries })`。error: `{ type: 'network'|'business'|'server', code }`. 规则（RBL-672 决策树）：1) attempt ≥ maxRetries → 'circuit-break'（人工确认提示）；2) business 类型 → 'no-retry'（返回值处理——RBL-513）；3) network/server 类型 + 有幂等键 → 'auto-retry'（退避）；4) network/server + 无键 → 'manual-check'（人工确认——不知 server 是否执行）；5) 返回 `{ action: 'auto-retry'|'no-retry'|'manual-check'|'circuit-break', backoffMs? }`。边界：maxRetries=0（首次即 break——manual-check）；error 为 null（成功——不重试）。

```javascript
function retryDecision(error, { idempotencyKey, attempt = 0, maxRetries = 3 } = {}) {
  if (!error) return { action: 'no-retry' };
  if (attempt >= maxRetries)
    return { action: 'circuit-break',
      detail: `重试 ${attempt} 次失败——请人工确认是否已提交` };
  if (error.type === 'business')
    return { action: 'no-retry', detail: '业务错误——请根据返回信息处理' };
  // network/server：瞬态
  if (idempotencyKey)
    return { action: 'auto-retry', backoffMs: 1000 * 2 ** attempt };
  return { action: 'manual-check',
    detail: '网络异常且无法确认是否已提交——请检查后再试' };
}

// 自测
// 幂等有键：自动重试（退避递增）
console.log(retryDecision({ type: 'network' }, { idempotencyKey: 'k1', attempt: 0 }))
  .action === 'auto-retry'));
console.log(retryDecision({ type: 'network' }, { idempotencyKey: 'k1', attempt: 1 }).backoffMs === 2000);
// 无键：人工确认
console.log(retryDecision({ type: 'network' }, {}).action === 'manual-check');
console.log(retryDecision({ type: 'server' }, { attempt: 0 }).action === 'manual-check');
// 业务错误
console.log(retryDecision({ type: 'business', code: 'OUT_OF_STOCK' }, { idempotencyKey: 'k' }).action === 'no-retry');
// 熔断
console.log(retryDecision({ type: 'network' }, { idempotencyKey: 'k', attempt: 3, maxRetries: 3 }).action === 'circuit-break');
console.log(retryDecision({ type: 'network' }, { idempotencyKey: 'k', attempt: 2, maxRetries: 3 }).action === 'auto-retry');
// maxRetries=0
console.log(retryDecision({ type: 'network' }, { attempt: 0, maxRetries: 0 }).action === 'circuit-break');
// null（成功）
console.log(retryDecision(null, {}).action === 'no-retry');
```

**评分点**：
- 决策树完整：熔断 > 业务不重试 > 幂等自动 > 无键人工（优先级链清晰）
- 退避递增（2^attempt）；manual-check 的用户反馈文案（「无法确认是否已提交」——诚实）
- 边界（maxRetries=0/null）；business 的理由（返回值处理 RBL-513）
- 能说清「非幂等 Action 的网络错误不能盲重试——不知 server 是否已执行，幂等键是自动重试的前提」属于加分
