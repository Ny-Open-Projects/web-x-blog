---
title: [AGT-507] 用户配额（次数/token）将耗尽时，前端如何做预警、限流提示与升级引导？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-507：用户配额（次数/token）将耗尽时，前端如何做预警、限流提示与升级引导

**答**：
- 配额分三层展示：实时余量（每次请求后同步）、月度趋势（预测还能用几天）、单次消耗明细（这次提问花了多少）。
- 限流触发时区分错误语义：429 是"稍后再试"（展示重试倒计时），配额耗尽是"升级或等待重置"（引导付费/管理员），文案与按钮完全不同。
- 高消耗动作（长任务/批量）执行前做预估消耗确认，避免用户一觉醒来配额清零。

```javascript
function guardQuota(action, est) {
  const q = store.quota;
  if (q.remaining < est) {
    return ui.confirmUpgrade({ need: est, have: q.remaining,
      resetAt: q.resetAt }); // 配额不足→升级引导
  }
  if (q.rateLimited) {
    return ui.toast(`触发限流，${q.retryAfter}s 后自动重试`,
      { action: () => countdownRetry(action) }); // 限流→重试
  }
  if (est > q.remaining * 0.3) {
    return ui.confirm(`本次预计消耗 ${est} tokens（剩余 ${q.remaining}），继续？`);
  }
  return action();
}
```

