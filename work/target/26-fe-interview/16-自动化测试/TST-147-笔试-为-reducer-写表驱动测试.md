---
title: [TST-147] 笔试：为 reducer（购物车状态机）写表驱动测试
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-147：笔试：为 reducer（购物车状态机）写表驱动测试
**答**：
- 场景：购物车 reducer——加购/改数量/删除/清空，约束：数量上限 99、数量减到 0 自动移除、重复加购合并。reducer 是纯函数，测试不需要 render，重点是**表驱动**覆盖状态转移矩阵。
- 表驱动模式：`cases = [{ name, state, action, expected }]` + 一个 it 遍历——新增分支只加一行，可读且防止「测试代码比业务代码还长」。
- 边界：不可变性（reducer 返回新对象不改入参——额外断言 `result !== state` 且原对象未变）；非法 action 返回原 state；数量边界 0/99。

```javascript
import cartReducer from './cartReducer'; // (state, action) => state

const base = { items: [{ skuId: 'A', count: 1, price: 100 }] };

const cases = [
  {
    name: '加购新商品：追加并初始化数量',
    state: { items: [] },
    action: { type: 'add', skuId: 'B', price: 50 },
    expected: { items: [{ skuId: 'B', count: 1, price: 50 }] },
  },
  {
    name: '重复加购：合并数量',
    state: base,
    action: { type: 'add', skuId: 'A', price: 100 },
    expected: { items: [{ skuId: 'A', count: 2, price: 100 }] },
  },
  {
    name: '数量减到 0：自动移除',
    state: base,
    action: { type: 'dec', skuId: 'A' },
    expected: { items: [] },
  },
  {
    name: '数量加到上限 99：不再增加',
    state: { items: [{ skuId: 'A', count: 99, price: 100 }] },
    action: { type: 'inc', skuId: 'A' },
    expected: { items: [{ skuId: 'A', count: 99, price: 100 }] },
  },
  {
    name: '非法 action：返回原 state',
    state: base,
    action: { type: 'hack' },
    expected: base,
  },
];

test.each(cases)('$name', ({ state, action, expected }) => {
  expect(cartReducer(state, action)).toEqual(expected);
});

test('纯函数：不修改入参', () => {
  const state = { items: [{ skuId: 'A', count: 1 }] };
  const frozen = Object.freeze(state);                 // 冻结后修改会抛错
  const result = cartReducer(frozen, { type: 'inc', skuId: 'A' });
  expect(result).not.toBe(state);                      // 返回新引用
  expect(state.items[0].count).toBe(1);                // 原对象未变
});
```

**评分点**：
1. test.each 表驱动组织，用例即数据（可维护性）。
2. 覆盖 0/99 边界、合并、非法 action、自动移除。
3. 纯函数验证：不可变性与入参不被修改（冻结法很加分）。
4. 期望值完整写出而非用快照偷懒。
