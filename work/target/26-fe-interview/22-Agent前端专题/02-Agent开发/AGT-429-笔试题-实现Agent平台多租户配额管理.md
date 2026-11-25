---
title: [AGT-429] 笔试题——实现多租户配额管理（三级配额+超额降级+计费归因）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-429：手写租户配额：月/日/任务三级、超额先降级后暂停、用量记账

**需求与边界**：
- 输入：请求 {tenantId, userId}、配额配置、用量存储；每请求前检查；输出：允许+模型档 或 拒绝。
- 边界要求：① 三级检查（任务内成本在 AGT-415，此处月/日/任务级）；② 超额策略分级：软超（90%）降模型、硬超（100%）暂停新任务但不动进行中任务；③ 用量记账原子（并发不超卖）；④ 归因字段完整（租户/用户/任务/模型）。

**答**：
```javascript
class TenantQuota {
  constructor({ quotas, usage }) { this.quotas = quotas; this.usage = usage; }
  async check({ tenantId, userId, taskId }) {
    const q = this.quotas[tenantId];
    // 1. 租户月配额
    const month = await this.usage.tenantMonth(tenantId);
    if (month.cost >= q.monthCap) return this.deny(tenantId,
      'tenant_month_cap', { renewAt: q.renewAt });
    // 2. 用户日配额
    const day = await this.usage.userDay(tenantId, userId);
    if (day.cost >= q.userDailyCap) return this.deny(tenantId,
      'user_daily_cap');
    // 3. 档位决定：软超降级模型，未超默认
    const ratio = month.cost / q.monthCap;
    const model = ratio > 0.9 ? CHEAP_MODEL : q.preferredModel;
    return { allow: true, model, tenantId, userId, taskId };
  }
  async record({ tenantId, userId, taskId, model,
                 inputTok, outputTok, toolFee = 0 }) {
    const cost = price(model, inputTok, outputTok) + toolFee;
    // 原子记账（Lua/事务防并发超卖）
    await this.usage.incr({ tenantId, userId, taskId },
      { cost, tokens: inputTok + outputTok });
    return cost;
  }
  deny(tenantId, reason, extra = {}) {
    return { allow: false, reason, tenantId, ...extra,
      hint: reason.includes('daily') || reason.includes('month')
        ? '请联系管理员升级配额' : null };
  }
}
// usage.incr 原子性：Redis INCRBYFLOAT / SQL UPDATE ... SET x = x + ? 
// 而非先读后写；租户隔离：所有 key 前缀带 tenantId。
```

**评分点**:
- 三级配额检查（月→日→档位）顺序合理，超额策略分级（90% 降级 / 100% 暂停）。
- 记账原子性意识（防并发超卖）且所有 key 带租户前缀（隔离）。
- 拒绝响应带 hint 与续期信息（体验层考虑）。
- 归因字段完整（tenant/user/task/model），可接计费与成本分析。
