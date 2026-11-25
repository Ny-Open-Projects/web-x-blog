---
title: [AIC-364] 多租户 SaaS 产品中用 AI 做租户隔离相关的开发辅助，有什么特殊注意点？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-364：多租户 SaaS 产品中用 AI 做租户隔离相关的开发辅助，有什么特殊注意点？
**答**：
- 数据边界即最高约束：Agent 读取租户数据必须走脱敏视图，提示词里禁止出现真实租户 ID。
- 隔离逻辑重点评审：tenant_id 过滤是否存在于每个查询——AI 评审把「缺租户过滤」列为高危。
- 测试要求：每个数据访问层测试必须包含「跨租户访问拒绝」用例，AI 生成测试的固定模板项。
- 多租户规则独立成 rules 文件，glob 锁定数据层目录。

```javascript
const multiTenantRules = {
  review: { critical: '查询缺 tenant_id 过滤', auto: 'blocked' },
  testTemplate: '每个 DAL 测试必须含 cross-tenant 拒绝用例',
  ctx: 'Agent 读租户数据 → 脱敏视图（假 ID）',
};
r
```
