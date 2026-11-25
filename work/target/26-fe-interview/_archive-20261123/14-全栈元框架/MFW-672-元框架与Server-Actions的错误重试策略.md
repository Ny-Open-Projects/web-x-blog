---
title: [MFW-672] Server Actions 的错误重试策略
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-672：Server Actions 的重试策略

**答**:
- Action 错误的重试分类（RBL-856 的 Action 版）：1) **瞬态错误**（网络超时/503——幂等 action 可重试 RBL-567 幂等前提）；2) **业务错误**（校验失败/库存不足——重试无意义：返回值 error 处理 RBL-513）；3) **非幂等的瞬态错误**（网络断但 server 已执行——重试 = 重复执行：幂等键防 RBL-567；「非幂等 action 的网络错误」不能盲重试（不知道 server 是否已执行）。
- 重试的实现：client 侧 retry（指数退避 + 幂等键——RBL-856 的 client 版）；「重试的用户反馈」（重试中 UI 提示——静默重试 vs 可见重试：静默的次数限制（3 次）后转人工）；「重试与新提交的区分」（重试用同 idempotencyKey——新提交用新 key）。
- 重试的熔断：连续 N 次失败 → 熔断（停止重试——提示用户稍后再试/反馈上报）；熔断的恢复（时间窗过后重置——半开状态 RBL-687）。
- 追问钩子：为什么「非幂等 Action 的网络错误」不能自动重试？——网络错误 = 「不知道 server 是否执行」（超时可能已执行）——重试 = 可能重复下单（资损）；幂等键（RBL-567）解决：重试带同 key → server 去重返回原结果；「非幂等 + 无键」的组合 = 必须人工确认（UI 提示「请检查是否已提交再重试」）——重试策略的决策树：幂等有键 → 自动重试；非幂等无键 → 人工确认；非幂等有键 → 自动重试（键防重复）。

```typescript
// Action 重试策略
async function submitWithRetry(action, fd, { idempotencyKey, maxRetries = 3 } = {}) {
  let lastError;
  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      if (attempt > 0) await sleep(1000 * 2 ** (attempt - 1));   // 退避
      return await action(fd, idempotencyKey);         // 幂等键随重试
    } catch (e) {
      lastError = e;
      if (isBusinessError(e)) throw e;                 // 业务错误不重试（RBL-856 分类）
      if (attempt === maxRetries) break;               // 熔断
    }
  }
  // 熔断后：人工确认提示
  return { error: '提交失败，请检查是否已成功再重试', requiresManualCheck: !idempotencyKey };
}
// client 侧幂等键管理
const idemKey = useRef(crypto.randomUUID()).current;     // 同表单生命周期稳定
// 重试 = 同 key（server 去重）
// 新提交 = 新 key（新表单/重置后）
```
