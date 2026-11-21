---
title: [ARC-008] CAP 定理在前端有哪些具体表现？一致性 vs 可用性如何取舍？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-008：CAP 定理在前端有哪些具体表现？一致性 vs 可用性如何取舍？
**答**：
- 前端天然处于"分区"常态（弱网、接口失败），必须选 AP：宁可展示稍旧数据，也不能白屏。
- 典型权衡：缓存旧数据 + 后台刷新（stale-while-revalidate）= 选可用性；下单页价格强校验 = 关键路径选一致性。
- 好的前端架构是"分层取舍"：列表页容忍不一致，交易页强一致，用状态分类学把策略显性化。

```typescript
// 列表页：AP 策略 —— 先展示缓存旧数据，后台刷新，失败降级
const { data } = useQuery({
  queryKey: ['goods-list'],
  queryFn: fetchGoods,
  staleTime: 60_000,
  gcTime: 24 * 60 * 60_000,          // 离线也能读到旧数据（可用性）
  placeholderData: keepPreviousData,  // 翻页不闪空（体验一致性让位可用性）
});

// 下单页：CP 策略 —— 提交前强制拉最新价格做服务端校验
async function submitOrder(skuId: string) {
  const latest = await fetchPrice(skuId, { cache: 'no-store' }); // 舍弃可用性换一致性
  if (latest.price !== cartCache.getPrice(skuId)) {
    throw new PriceChangedError(latest.price); // 弹窗让用户二次确认
  }
  return createOrder(skuId, latest.price);
}
```

---

## 二、应用分层与模块化（ARC-009 ~ ARC-018）
