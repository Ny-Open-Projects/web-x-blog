---
title: [AIC-691] AI 平台怎么做「成本中心」和配额管理？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-691：AI 平台怎么做成本中心和配额管理？

**答**：
- 结论先行：**成本中心 =「谁用谁付」——按团队/项目核算 AI 消耗，配额是预算的硬约束**。不核算成本，AI 支出就是笔糊涂账，无法回答「这笔投入值不值」（AIC-119 成本分摊 / AIC-172 计费）。
- 核算机制：1) **归因**：每笔 AI 调用打上 team/project/user 标签（网关层完成，AIC-684）；2) **计费**：按模型单价 × token 计费，汇总到成本中心；3) **分摊**：共享成本（平台团队、基础设施）按合理规则分摊（按用量/按人头）；4) **可视化**：各成本中心的消耗看板，让团队看到自己花了多少。
- 配额管理：1) **分级配额**：按团队预算分配月度 token 配额；2) **熔断**：配额用尽自动降级（便宜模型）或停止（AIC-415 成本熔断）；3) **预警**：用量达 80% 告警；4) **弹性**：允许临时申请加配额，但要审批——让成本有约束又有弹性。
- 行为引导：成本可见性本身就是治理——团队看到自己烧了多少钱，会自然减少无意义的重试和滥用（AIC-087 成本核算）。
- 追问钩子：为什么「成本可见」能改变行为？——因为不可见时，工程师没有动力优化 token 使用（反正不是他付钱）；可见后，「这个任务跑了 10 次重试烧了 5 块钱」会促使他检查 prompt——把「外部性」内部化，是成本治理的根本。

```typescript
type Usage = { team: string; tokens: number; model: string };
const PRICES: Record<string, number> = { 'strong': 0.01, 'fast': 0.001 }; // 每千token

function costCenters(usages: Usage[], quotas: Record<string, number>) {
  const report: Record<string, { cost: number; quota: number; usagePct: number; status: string }> = {};
  for (const u of usages) {
    const c = report[u.team] || (report[u.team] = { cost: 0, quota: quotas[u.team] || 0, usagePct: 0, status: 'ok' });
    c.cost += (PRICES[u.model] || 0) * u.tokens / 1000;
  }
  for (const c of Object.values(report)) {
    c.usagePct = c.quota ? c.cost / c.quota : 1;
    c.status = c.usagePct >= 1 ? 'exceeded' : c.usagePct >= 0.8 ? 'warning' : 'ok';
  }
  return report;
}

const usages = [
  { team: 'fe', tokens: 80000, model: 'strong' }, // 0.8
  { team: 'be', tokens: 10000, model: 'fast' },   // 0.01
];
const r = costCenters(usages, { fe: 1.0, be: 1.0 });
console.log(r.fe.status === 'warning' && r.be.status === 'ok');
```
