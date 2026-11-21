---
title: [TST-109] E2E 的测试数据怎么管理？造数、清理、隔离方案
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-109：E2E 的测试数据怎么管理？造数、清理、隔离方案
**答**：
- 造数三条路：① UI 造数（慢且脆，只适合本身测 UI 录入的场景）；② API 造数（首选——直接调后端接口建订单/用户，秒级且稳定，封装成 `factories` 模块）；③ 数据库直插/快照（最快但要懂表结构，更新风险高，适合大型基线数据）。原则：测试经由 API 造数、经由 UI 验证。
- 清理策略三选：用例后清理（fixture teardown，最干净）、全局清扫（定时任务删除超过 N 天的 `e2e-` 前缀数据，兜底）、一次性环境（每个 CI job 一个新数据库或 schema，天然隔离，成本是环境基建）。
- 隔离：用例数据全部带唯一前缀（时间戳/worker id），账号池按 worker 分配；避免「A 用例改了商品库存，B 用例刚好要买最后一件」这种隐式耦合。
- 基线数据：登录账号、商品、地址等只读基础数据用 migration/seed 脚本维护，所有用例共享（只读不写），写操作一律新建自己的数据。
- 追问钩子：时间敏感数据怎么造？——后端造数接口传相对时间（"3 天前过期"），别用绝对时间戳，避免跨日运行翻车。

```javascript
// factories/order.ts —— API 造数工厂
import { api } from './client';

export async function createOrder(overrides = {}) {
  const { data } = await api.post('/test/orders', {
    buyer: `e2e-${process.env.TEST_WORKER_INDEX}`,
    items: [{ skuId: 'SKU-001', count: 1 }],
    createdAtOffsetMin: -5,      // 相对时间：5 分钟前
    ...overrides,
  });
  return data;
}

// 用例内组合：fixture 造数 + teardown 清理
export const test = base.extend({
  paidOrder: async ({}, use) => {
    const order = await createOrder({ status: 'paid' });
    await use(order);
    await api.delete(`/test/orders/${order.id}`); // 清理自己的数据
  },
});
```
