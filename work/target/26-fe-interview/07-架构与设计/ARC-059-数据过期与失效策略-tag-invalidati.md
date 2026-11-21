---
title: [ARC-059] 数据过期与失效策略（tag invalidation）如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-059：数据过期与失效策略（tag invalidation）如何设计？
**答**：
- 两种失效模型：TTL 过期（简单，适合列表/配置类）与 tag invalidation（写操作精确失效相关查询，适合关联密集的中后台）。
- tag 设计按实体粒度（`['order', id]`、`['orders', 'list', filters]`），写操作的 mutation 声明失效哪些 tag，代替到处手写 refetch。
- 面试要点：失效粒度太粗导致过多请求，太细导致漏失效；一般按"实体 + 列表"两层 tag。

```typescript
// tag 化的失效体系：mutation 声明影响，查询只管消费
const qc = new QueryClient();

// 读：tag 即 queryKey
useQuery({ queryKey: ['order', orderId], queryFn: () => fetchOrder(orderId) });
useQuery({ queryKey: ['orders', 'list', filter], queryFn: () => fetchOrders(filter) });

// 写：集中声明失效面
qc.setMutationDefaults(['createOrder'], {
  mutationFn: (dto: CreateOrderDto) => api.post('/orders', dto),
  onSuccess: () => {
    qc.invalidateQueries({ queryKey: ['orders'] });   // 列表全失效（粗粒度）
    qc.invalidateQueries({ queryKey: ['dashboard'] }); // 跨实体关联也用 tag 声明
  },
});
qc.setMutationDefaults(['updateOrder'], {
  mutationFn: ({ id, patch }: { id: string; patch: Partial<Order> }) => api.patch(`/orders/${id}`, patch),
  onSuccess: (_r, { id }) => {
    qc.invalidateQueries({ queryKey: ['order', id] }); // 只失效该单（细粒度）
  },
});
// TTL 兜底：staleTime 30s + refetchOnWindowFocus，漏失效的 tag 也有机会自愈
```

---

## 七、渲染与 BFF 架构（ARC-060 ~ ARC-067）
