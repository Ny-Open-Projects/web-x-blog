---
title: [V3-170] 路由相关的组件测试如何 mock router？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-170：路由相关的组件测试如何 mock router？
**答**：
- 不真正装 vue-router：用 global.mocks.$route/$router 提供 stub，测"组件对路由的读取与跳转调用"。
- 需要 useRoute/useRouter 组合式 API 时，vi.mock("vue-router") 返回固定对象，粒度最小、最快。
- 依赖真实路由结构的（面包屑、tab 组件）用 createMemoryHistory + createRouter 搭真路由，history 用内存模式避免污染地址栏。
- 断言跳转用 expect($router.push).toHaveBeenCalledWith(...)，不关心真实导航结果。

```typescript
// views/__tests__/UserDetail.spec.ts
import { describe, it, expect, vi } from "vitest";
import { mount } from "@vue/test-utils";
import UserDetail from "../UserDetail.vue";

// 方式一：mock 组合式 API（最常用、最快）
const pushMock = vi.fn();
vi.mock("vue-router", () => ({
  useRoute: () => ({ params: { id: "42" }, query: { tab: "profile" } }),
  useRouter: () => ({ push: pushMock }),
}));

describe("UserDetail", () => {
  it("从路由参数读取用户 id", () => {
    const wrapper = mount(UserDetail);
    expect(wrapper.text()).toContain("42");
  });

  it("点击编辑跳转到编辑页", async () => {
    const wrapper = mount(UserDetail);
    await wrapper.find("[data-test=edit]").trigger("click");
    expect(pushMock).toHaveBeenCalledWith("/users/42/edit");
  });
});

// ---------- 方式二：内存路由（适合依赖真实路由结构的组件） ----------
import { createRouter, createMemoryHistory } from "vue-router";

it("面包屑组件根据路由 matched 生成", async () => {
  const router = createRouter({
    history: createMemoryHistory(), // 内存模式：不操作真实地址栏
    routes: [
      { path: "/", component: { template: "<div>home</div>" } },
      {
        path: "/system",
        component: { template: "<router-view />" },
        children: [{ path: "user", component: { template: "<div>user</div>" } }],
      },
    ],
  });
  router.push("/system/user");
  await router.isReady();

  const wrapper = mount(Breadcrumb, { global: { plugins: [router] } });
  expect(wrapper.findAll("li").map((li) => li.text())).toEqual(["首页", "system", "user"]);
});
```
