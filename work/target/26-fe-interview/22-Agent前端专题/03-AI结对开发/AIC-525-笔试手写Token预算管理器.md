---
title: [AIC-525] 笔试：手写 Token 预算管理器
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-525：笔试：手写 Token 预算管理

**答**：实现 `createTokenBudget({ dailyLimit, outputMultiplier, now })`。方法：`checkAndDeduct(userId, inputTokens, outputTokens)` → `{ allowed, remaining, usagePct }`、`getUsage(userId)`、`reset(userId)`。规则：1) **成本计算**：cost = inputTokens + outputTokens × outputMultiplier（默认 3——output 更贵）；2) **日重置**：预算按 UTC 0 点重置（过期 → used=0）；3) 超预算 → `allowed: false`（不扣——拒绝请求）；4) **近似预算**（remaining 可以透支到 0——最后一次调用可以超过（不截断——完成当前请求））；5) reset(userId)：手动重置（管理员操作）。边界：userId 不存在（新用户——初始化）；outputTokens=0（纯 input——cost=input）；dailyLimit=0（全部拒绝——预算为 0）。

```javascript
function createTokenBudget({ dailyLimit = 2000000, outputMultiplier = 3, now = Date.now } = {}) {
  const budgets = new Map();
  function getBudget(userId) {
    let b = budgets.get(userId);
    const DAY = 86400000;
    if (!b || now() >= b.resetAt) {
      b = { used: 0, resetAt: now() + DAY - (now() % DAY) };
      budgets.set(userId, b);
    }
    return b;
  }
  return {
    checkAndDeduct(userId, inputTokens = 0, outputTokens = 0) {
      const b = getBudget(userId);
      const cost = inputTokens + outputTokens * outputMultiplier;
      const allowed = b.used < dailyLimit;               // 近似：当前 < limit 即可（可透支）
      if (allowed) b.used += cost;
      return { allowed, remaining: Math.max(0, dailyLimit - b.used),
        usagePct: +Math.min(100, (b.used / dailyLimit) * 100).toFixed(1) };
    },
    getUsage(userId) {
      const b = getBudget(userId);
      return { used: b.used, limit: dailyLimit,
        pct: +Math.min(100, (b.used / dailyLimit) * 100).toFixed(1) };
    },
    reset(userId) { budgets.delete(userId); },
  };
}

// 自测
let mockNow = 86400000000;                               // UTC 0 点
const budget = createTokenBudget({ dailyLimit: 1000, outputMultiplier: 3, now: () => mockNow });

// 正常扣减
let r = budget.checkAndDeduct('u1', 200, 50);           // cost = 200 + 150 = 350
console.log(r.allowed === true && r.usagePct === 35);
// 再扣
r = budget.checkAndDeduct('u1', 400, 50);               // cost = 400 + 150 = 550; total = 900
console.log(r.allowed === true && r.usagePct === 90);
// 超预算
r = budget.checkAndDeduct('u1', 200, 0);                // cost = 200; total = 1100 > 1000
console.log(r.allowed === false);                       // 拒绝
console.log(budget.getUsage('u1').used === 900);        // 未扣（拒绝不扣）

// 不同用户独立
r = budget.checkAndDeduct('u2', 500, 0);
console.log(r.allowed === true && r.usagePct === 50);

// 日重置
mockNow += 86400000;                                    // 第二天
r = budget.checkAndDeduct('u1', 100, 0);
console.log(r.allowed === true && r.usagePct === 10);   // 重置后重新计

// dailyLimit=0
const zero = createTokenBudget({ dailyLimit: 0, now: () => mockNow });
r = zero.checkAndDeduct('u3', 100, 0);
console.log(r.allowed === false);                       // 预算为 0 全拒

// output=0（纯 input）
r = budget.checkAndDeduct('u2', 100, 0);
console.log(r.allowed === true);                        // cost = 100
```

**评分点**：
- 成本公式：input + output × multiplier（output 3x——LLM 定价的非对称性）
- 日重置逻辑（UTC 0 点——过期重算）；拒绝不扣（超预算不部分扣——事务性）
- 边界（dailyLimit=0 全拒/不同用户独立/近似透支——最后一次可超）
- 能说清「LLM 成本的主要杠杆是 input 裁剪：input 占 97% 成本——上下文裁剪（RBL-502）是 ROI 最高的单项优化」属于加分
