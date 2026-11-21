---
title: [V3-127] 如何用 @vue/test-utils 做 Vue 组件单元测试？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-127：如何用 @vue/test-utils 做 Vue 组件单元测试？
**答**：
- mount 挂载完整组件，shallowMount 只渲染一层（子组件 stub），按测试粒度选择。
- 断言三板斧：wrapper.text/props 查渲染结果、trigger 触发事件后 await nextTick、emitted 查事件 payload。
- 全局依赖（router/pinia/i18n）用 global.plugins 注入，第三方组件用 stubs 替换。
- 测试用户行为而非实现细节：点按钮、输文字、看输出，重构内部时测试不碎。

```typescript
// components/__tests__/Counter.spec.ts
import { describe, expect, it } from "vitest";
import { mount } from "@vue/test-utils";
import Counter from "../Counter.vue";

describe("Counter", () => {
  it("点击按钮后计数加一并发出 change 事件", async () => {
    const wrapper = mount(Counter, { props: { initial: 1 } });

    await wrapper.find("button").trigger("click"); // 模拟用户点击
    expect(wrapper.text()).toContain("2"); // 断言渲染结果
    expect(wrapper.emitted("change")?.[0]).toEqual([2]); // 断言事件 payload
  });

  it("渲染插槽内容", () => {
    const wrapper = mount(Counter, {
      slots: { default: "自定义标题" },
    });
    expect(wrapper.text()).toContain("自定义标题");
  });

  it("全局依赖用 plugins 注入、子组件用 stubs 替换", () => {
    mount(Counter, {
      global: {
        plugins: [], // createTestingPinia() 等测试替身
        stubs: { ElDialog: true }, // 弹窗类组件替换为空壳
      },
    });
  });
});
```
