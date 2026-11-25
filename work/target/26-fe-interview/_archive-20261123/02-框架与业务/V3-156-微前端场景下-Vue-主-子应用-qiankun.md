---
title: [V3-156] 微前端场景下 Vue 主/子应用（qiankun）如何实践？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-156：微前端场景下 Vue 主/子应用（qiankun）如何实践？
**答**：
- 主应用注册子应用（entry、activeRule、container），子应用导出 bootstrap/mount/unmount 三个生命周期。
- Vue3 子应用关键点：mount 里 createApp，unmount 里必须 app.unmount() 并清空容器 DOM，否则热更新与重复挂载会出鬼问题。
- 样式隔离：子应用配 scoped 或用实验性 strictStyleIsolation；运行时 JS 隔离 qiankun 默认提供。
- 共享依赖：公共的 vue/pinia/router 通过主应用 external + 子应用 webpack externals（或 Vite 用 vite-plugin-qiankun）避免多份实例；跨应用通信用 initGlobalState 或自定义事件。
- 路由注意：子应用 base 要与 activeRule 对齐，push 路由时带子应用前缀。

```typescript
// 主应用 main.ts —— 注册与共享
import { registerMicroApps, initGlobalState, start } from "qiankun";

registerMicroApps([
  {
    name: "sub-vue3",
    entry: "//localhost:7101",
    container: "#sub-app",
    activeRule: "/sub", // 命中前缀时挂载子应用
    props: { token: localStorage.getItem("token") }, // 下发登录态
  },
]);

// 跨应用通信：全局状态
const actions = initGlobalState({ user: null });
actions.onGlobalStateChange((state) => console.log("主应用收到：", state));

start({ prefetch: true }); // 预加载子应用资源

// ---------------- 子应用 ----------------
// sub-vue3/src/main.ts —— 三个生命周期
import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";
import App from "./App.vue";

let app: ReturnType<typeof createApp> | null = null;
let router: ReturnType<typeof createRouter> | null = null;

export async function bootstrap() {
  console.log("sub-vue3 bootstrap");
}

export async function mount(props: { container: HTMLElement; onGlobalStateChange: Function }) {
  app = createApp(App);
  router = createRouter({
    history: createWebHistory("/sub"), // base 与主应用 activeRule 对齐
    routes: [{ path: "/", component: () => import("./pages/Index.vue") }],
  });
  app.use(router);
  app.provide("globalState", props); // 把主应用 props 注入后代
  app.mount(props.container.querySelector("#sub-root")!);
}

export async function unmount() {
  app?.unmount();
  app = null;
  // 关键：清空容器 DOM，防止 qiankun 复用容器时出现重复节点
  document.querySelectorAll("#sub-root").forEach((el) => (el.innerHTML = ""));
}
```
