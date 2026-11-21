---
title: [V3-133] 微前端场景下 Vue 子应用接入 qiankun 有哪些要点？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-133：微前端场景下 Vue 子应用接入 qiankun 有哪些要点？
**答**：
- 子应用导出 bootstrap/mount/unmount 三个生命周期；mount 时在主应用给的 container 里 createApp，unmount 时必须完整卸载实例与路由。
- 路由 base 要按是否运行在 qiankun 下切换（window.__POWERED_BY_QIANKUN__），避免与主应用路由冲突。
- 样式隔离：子应用样式加前缀或开启 strictStyleIsolation（Shadow DOM，注意弹窗 Teleport 挂 body 会逃逸）。
- 全局对象污染：避免直接改 window；公共依赖可用 externals/Webpack Module Federation 共享。

```typescript
// src/main.ts —— qiankun 子应用生命周期
import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";
import App from "./App.vue";
import { routes } from "./router/routes";

declare global {
  interface Window {
    __POWERED_BY_QIANKUN__?: boolean;
    __INJECTED_PUBLIC_PATH_BY_QIANKUN__?: string;
  }
}

let app: ReturnType<typeof createApp> | null = null;
let router: ReturnType<typeof createRouter> | null = null;

function render(container?: HTMLElement) {
  app = createApp(App);
  // 运行在 qiankun 下时路由 base 必须是子应用注册的 activeRule
  const base = window.__POWERED_BY_QIANKUN__ ? "/sub-vue/" : "/";
  router = createRouter({ history: createWebHistory(base), routes });
  app.use(router);
  app.mount(container ?? "#app"); // qiankun 模式挂到主应用的容器节点
}

export async function bootstrap() {
  // 一次性初始化：一般留空
}

export async function mount(props: { container: HTMLElement }) {
  render(props.container);
}

export async function unmount() {
  // 必须完整卸载，否则再次进入子应用会重复挂载、内存泄漏
  app?.unmount();
  app = null;
  router = null;
}

// 独立运行（开发调试）时直接渲染
if (!window.__POWERED_BY_QIANKUN__) render();
```
