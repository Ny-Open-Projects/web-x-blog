---
title: [AIC-524] LLM API 的 Token 预算管理
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-524：LLM API Token 预算管理

**答**:
- LLM API 的成本结构：1) **按 token 计费**（input tokens + output tokens——input = 上下文（prompt + 代码）+ output = 生成；GPT-4 约 $10/M input + $30/M output（output 是 input 的 3 倍——生成比阅读贵）；2) **上下文的成本占比**：Cursor 每次补全 = 当前文件上下文（~2000 tokens input）+ 补全输出（~50 tokens output）——input 占成本的 97%（上下文的裁剪 = 成本的主要杠杆 RBL-502）；3) **团队成本**：每人每天 ~1000 次 AI 调用 × 2000 tokens = 2M tokens/人/天 × 10 人 = 20M tokens/天 = $200/天 = $4400/月——团队的 AI 成本可预算化。
- Token 预算的管理：1) **per-user 预算**（每人每天 N tokens——超预算限流 RBL-690）；2) **per-project 预算**（项目级成本中心——项目预算= M tokens/月）；3) **缓存复用**（相同上下文的缓存命中——不重复计费（prompt caching——OpenAI/Anthropic 的缓存 API））；4) **模型分级**（简单补全用便宜模型（GPT-3.5）/复杂生成用贵模型（GPT-4）——模型路由 RBL-528 AIC 目录）。
- 追问钩子：为什么「上下文裁剪」（RBL-502）是 LLM 成本控制的主要杠杆？——input 占总成本的 97%（output 只占 3%）；上下文裁剪（符号级/语义级）= input tokens 减少 50~90% → 成本同比例下降；「裁剪的 ROI」：裁剪的开发成本（实现符号提取/语义检索）≈ 2 周，节省成本 50% → 月省 $2000（10 人团队）→ 回本 3 天——上下文裁剪是「AI 成本控制 ROI 最高的单项优化」。

```typescript
// Token 预算管理器
interface TokenBudget { userId: string; dailyLimit: number; used: number; resetAt: number; }
class TokenBudgetManager {
  private budgets = new Map<string, TokenBudget>();
  constructor(private dailyLimit = 2_000_000) {}       // 默认 2M tokens/人/天
  async checkAndDeduct(userId: string, inputTokens: number, outputTokens: number): Promise<boolean> {
    const now = Date.now();
    let budget = this.budgets.get(userId);
    if (!budget || now > budget.resetAt) {
      budget = { userId, dailyLimit: this.dailyLimit, used: 0, resetAt: now + 86400000 };
      this.budgets.set(userId, budget);
    }
    const cost = inputTokens + outputTokens * 3;       // output 3x cost
    if (budget.used + cost > budget.dailyLimit) return false;   // 超预算拒绝
    budget.used += cost;
    return true;
  }
  getUsage(userId: string) {
    const b = this.budgets.get(userId);
    return b ? { used: b.used, limit: b.dailyLimit, pct: +(b.used / b.dailyLimit * 100).toFixed(1) } : { used: 0, limit: this.dailyLimit, pct: 0 };
  }
}
```
