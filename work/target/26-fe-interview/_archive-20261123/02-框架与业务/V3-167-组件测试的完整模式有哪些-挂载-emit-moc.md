---
title: [V3-167] 组件测试的完整模式有哪些（挂载、emit、mock 依赖）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-167：组件测试的完整模式有哪些（挂载、emit、mock 依赖）？
**答**：
- 三层验证：渲染结果（find + text）、交互行为（trigger + emitted）、Props 契约（setProps 后的响应）。
- mock 分级：子组件用 shallow stub 掉；模块依赖（api）用 vi.mock；pinia 用 createTestingPinia 替换真实 store。
- 异步交互用 flushPromises 等微任务清空，避免"改了状态断言还是旧的"。
- 原则：测组件的对外契约（props/emit/slot），不测内部实现细节，否则重构即全红。

```typescript
// components/__tests__/Counter.spec.ts —— Vitest + @vue/test-utils
import { describe, it, expect, vi } from "vitest";
import { mount, flushPromises } from "@vue/test-utils";
import Counter from "../Counter.vue";
import { api } from "@/services/api";

// 1. 模块级 mock：拦截 api 依赖
vi.mock("@/services/api", () => ({
  api: { saveCount: vi.fn().mockResolvedValue({ ok: true }) },
}));

describe("Counter", () => {
  it("初始渲染 props 传入的值", () => {
    const wrapper = mount(Counter, { props: { init: 5 } });
    expect(wrapper.find("[data-test=count]").text()).toBe("5");
  });

  it("点击按钮后 emit increment 并更新显示", async () => {
    const wrapper = mount(Counter, { props: { init: 0 } });
    await wrapper.find("button").trigger("click"); // trigger 自动等 nextTick
    expect(wrapper.emitted("increment")).toHaveLength(1);
    expect(wrapper.find("[data-test=count]").text()).toBe("1");
  });

  it("异步保存后调用 api.saveCount", async () => {
    const wrapper = mount(Counter, { props: { init: 1 } });
    await wrapper.find("[data-test=save]").trigger("click");
    await flushPromises(); // 清空微任务：等 mock 的 Promise resolve
    expect(api.saveCount).toHaveBeenCalledWith(1);
  });

  it("props 变化时视图响应", async () => {
    const wrapper = mount(Counter, { props: { init: 0 } });
    await wrapper.setProps({ init: 10 });
    expect(wrapper.find("[data-test=count]").text()).toBe("10");
  });

  it("子组件被 stub 时只测自身逻辑", () => {
    const wrapper = mount(Counter, {
      props: { init: 0 },
      shallow: true, // shallow stub 掉所有子组件
      global: {
        stubs: { FancyBadge: true }, // 或单独指定
      },
    });
    expect(wrapper.findComponent({ name: "FancyBadge" }).exists()).toBe(true);
  });
});
```
