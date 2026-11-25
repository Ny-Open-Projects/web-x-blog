---
title: [ZSM-709] 状态 mock 场景库：把「测试数据构造」从用例里抽出来共享
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-709：状态 mock 场景库：把「测试数据构造」从用例里抽出来共享

**答**：
- 痛点：每个测试用例手写「三个商品 + 一张券 + 半填充地址」——重复、漂移（一处改字段全测试崩）。**场景库（fixture factory）**：按业务语义命名的构造器集合（`givenCartWithThreeItems()`、`givenExpiredCoupon()`），单点维护数据 schema。
- 分层：1) **原子工厂**（`makeProduct({...overrides})`——defaults + 展开，深合并）；2) **场景组装**（原子组合成业务场景，返回完整 store patch 或 API mock 响应）；3) **场景参数**（场景可变体：`givenCartWithThreeItems({ expiredCoupon: true })`）。
- 双出口：同一场景既产「store patch」（Storybook/单测）也产「API mock 响应」（MSW/E2E）——保证两条测试路径的数据一致（同一个工厂函数，两个 adapter）。
- schema 变更的收敛：工厂是「类型变化的第一反应面」——TS 类型改了，工厂先报错，全部用例引用工厂所以一处修全绿；直接手写对象的用例是散点炸弹。
- 追问钩子：场景库与「真实数据脱敏」——生产导出的数据（ZSM-561 快照）脱敏后进场景库作为「真实形状」参考，混入 faker 生成边界值（超长字符串/特殊字符/极值金额）。

```javascript
// 原子工厂：defaults + overrides 深合并
const makeProduct = (o = {}) => ({
  id: o.id ?? faker.string.uuid(),
  title: o.title ?? '测试商品',
  price: o.price ?? 1000,          // 单位：分
  stock: o.stock ?? 100,
  priceVersion: 1,
  ...pick(o, ['title', 'price', 'stock']),   // 显式覆盖
})

// 场景组装：业务语义命名
export const givenCartWithThreeItems = (o = {}) => {
  const items = [1, 2, 3].map((i) => ({ ...makeProduct({ price: 1000 * i }), qty: 1 }))
  return {
    storePatch: {
      items: o.expiredCoupon ? items : items,
      coupon: o.expiredCoupon ? { type: 'flat', amount: 500, expiredAt: Date.now() - 1000 } : null,
      address: givenAddress(),
    },
    apiResponse: { code: 0, data: { items, coupon: o.expiredCoupon ?? null } },
  }
}

// 测试消费（两个出口共享同一场景）
test('过期券不参与结算', () => {
  const { storePatch } = givenCartWithThreeItems({ expiredCoupon: true })
  const store = createCheckoutStore(storePatch.storePatch)
  expect(store.getState().total).toBe(6000)     // 券过期：原价
})

// Storybook
export const ExpiredCoupon = {
  parameters: { store: givenCartWithThreeItems({ expiredCoupon: true }).storePatch },
}

// 边界值混入（faker）
const edgeProducts = [
  makeProduct({ title: 'x'.repeat(500) }),      // 超长标题
  makeProduct({ price: 0 }),                    // 零元
  makeProduct({ stock: 0 }),                    // 无库存
]
```
