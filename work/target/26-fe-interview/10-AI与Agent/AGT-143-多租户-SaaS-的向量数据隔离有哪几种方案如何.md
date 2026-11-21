---
title: [AGT-143] 多租户 SaaS 的向量数据隔离有哪几种方案？如何选型？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-143：多租户 SaaS 的向量数据隔离有哪几种方案？如何选型？
**答**：
- 三档方案：命名空间/分区隔离（一个索引内用 tenant 前缀或 namespace，成本低、靠查询参数保证隔离）、索引级隔离（每租户一个 index/collection，隔离强、运维成本线性涨）、实例级隔离（独立向量库实例，金融级合规用）。
- 选型看合规等级与租户数量：中小 SaaS 用 namespace + 查询层强制 tenantId；大客户/强合规用独立索引；任何方案都要有「防串库」的统一数据访问层，禁止业务代码手拼过滤条件。
- 关键工程点：embedding 也要按租户维度考虑（自定义词表/领域微调是租户维度的资产）；删除租户时要级联清理向量与元数据（GDPR 被遗忘权）。
- 高频考点：namespace 方案的最大风险是「某处查询忘了带 tenantId」——用类型系统让无租户的查询编译不过。

```typescript
// 多租户向量访问层：类型系统强制 tenantId
type TenantScope = { readonly tenantId: string };

// 查询对象必须由 scope 构造，裸查询无类型可传——从根上防串库
export class TenantVectorStore {
  constructor(private mode: 'namespace' | 'index-per-tenant' = 'namespace') {}

  private target(scope: TenantScope): { namespace?: string; index: string } {
    switch (this.mode) {
      case 'namespace': return { namespace: `t-${scope.tenantId}`, index: 'main' };
      case 'index-per-tenant': return { index: `idx-${scope.tenantId}` };
    }
  }

  async upsert(scope: TenantScope, docs: { id: string; text: string }[]) {
    const { namespace, index } = this.target(scope);
    for (const d of docs) {
      await db.upsert({
        index, namespace, id: `${scope.tenantId}:${d.id}`, // id 再加租户前缀双保险
        values: await embed(d.text), metadata: { tenantId: scope.tenantId, text: d.text },
      });
    }
  }

  async search(scope: TenantScope, query: string, topK = 5) {
    const { namespace, index } = this.target(scope);
    const hits = await db.query({ index, namespace, vector: await embed(query), topK });
    // 出口断言：任何不带本租户前缀的命中一律视为事故
    const leaked = hits.filter((h) => !h.id.startsWith(`${scope.tenantId}:`));
    if (leaked.length) { audit.alert('cross-tenant hit', { tenantId: scope.tenantId }); return []; }
    return hits;
  }

  async purgeTenant(scope: TenantScope) { // 租户注销级联删除
    const { namespace, index } = this.target(scope);
    await db.deleteAll({ index, namespace, filter: { tenantId: scope.tenantId } });
  }
}

const db = { upsert: async (x: any) => { void x; }, query: async () => [] as any[], deleteAll: async (x: any) => { void x; } };
const audit = { alert: (m: string, x: unknown) => console.error(m, x) };
```
