---
title: [V3-169] Pinia store 怎么测试？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-169：Pinia store 怎么测试？
**答**：
- 用 createTestingPinia 替换真实插件：action 默认变 mock（vi.fn），可以断言"组件触发了某个 action"而不执行其实现。
- 测 state/getter：直接 setActivePinia(createPinia()) 裸用 store，绕开组件。
- 要测 action 真实逻辑时给 createTestingPinia 传 stubActions: false，并 mock 掉它调用的 api 模块。
- 分层策略：组件测试断言 action 被调用；store 单测验证 action 内部逻辑，两层各管一段。

```typescript
// stores/__tests__/cart.spec.ts
import { describe, it, expect, vi, beforeEach } from "vitest";
import { setActivePinia, createPinia } from "pinia";
import { createTestingPinia } from "@pinia/testing";
import { useCartStore } from "../cart";

// 模块 mock：store 的 action 依赖的 api
vi.mock("@/services/api", () => ({ api: { checkout: vi.fn().mockResolvedValue({ orderId: 1 }) } }));

describe("cart store（纯 store 单测）", () => {
  beforeEach(() => setActivePinia(createPinia()));

  it("addItem 累加数量并计算总价", () => {
    const cart = useCartStore();
    cart.addItem({ id: 1, price: 100, name: "A" });
    cart.addItem({ id: 1, price: 100, name: "A" });
    expect(cart.count).toBe(2);
    expect(cart.totalPrice).toBe(200); // getter 联动验证
  });

  it("removeItem 清空对应项", () => {
    const cart = useCartStore();
    cart.addItem({ id: 1, price: 100, name: "A" });
    cart.removeItem(1);
    expect(cart.count).toBe(0);
  });
});

// ---------- 组件层：断言 action 被触发 ----------
import { mount } from "@vue/test-utils";
import CartButton from "../CartButton.vue";

it("点击加购按钮触发 store 的 addItem", async () => {
  const wrapper = mount(CartButton, {
    props: { goods: { id: 1, price: 100, name: "A" } },
    global: { plugins: [createTestingPinia()] }, // action 默认被 stub 成 mock
  });
  await wrapper.find("button").trigger("click");
  const cart = useCartStore();
  expect(cart.addItem).toHaveBeenCalledTimes(1); // 只验证契约，不验证实现
});
```
