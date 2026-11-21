---
title: [V3-195] 设计一个埋点 SDK 的 Vue 插件（指令 + 路由自动埋点）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-195：设计一个埋点 SDK 的 Vue 插件（指令 + 路由自动埋点）？
**答**：
- 插件形态：app.use(tracker) 注入全局配置（上报地址、采样率、用户态），并挂 $track 与 v-track 指令。
- 两类采集：代码埋点（v-track 指令声明事件与参数）+ 自动埋点（router afterEach 采集 PV/停留时长）。
- 上报管道：批量聚合（队列 + 定时/定量 flush）、sendBeacon 兜底（页面卸载不丢）、失败重试与采样。
- 通用参数自动附带：路由、userId、版本、设备信息，业务只声明差异字段。

```typescript
// src/plugins/tracker.ts —— 埋点插件
import type { App } from "vue";
import type { Router } from "vue-router";

interface TrackPayload { event: string; [k: string]: unknown }

export function createTracker(options: { endpoint: string; sampleRate?: number }) {
  const buffer: TrackPayload[] = [];

  function send(list: TrackPayload[]) {
    // sendBeacon：页面卸载也可靠；不支持时降级 fetch keepalive
    const body = JSON.stringify(list);
    if (navigator.sendBeacon) navigator.sendBeacon(options.endpoint, body);
    else fetch(options.endpoint, { method: "POST", body, keepalive: true });
  }

  function track(event: string, params: Record<string, unknown> = {}) {
    if (Math.random() > (options.sampleRate ?? 1)) return; // 采样
    buffer.push({
      event,
      userId: localStorage.getItem("uid"),
      route: location.pathname,
      version: __APP_VERSION__,
      ts: Date.now(),
      ...params,
    });
    if (buffer.length >= 10) { send(buffer.splice(0)); } // 定量 flush
  }
  // 定时 flush 兜底
  setInterval(() => buffer.length && send(buffer.splice(0)), 10_000);

  return {
    track,
    // 路由自动埋点：PV + 停留时长
    installRouter(router: Router) {
      let enterAt = Date.now();
      router.afterEach((to) => track("page_view", { path: to.fullPath }));
      router.beforeEach((to, from) => {
        if (from.matched.length) {
          track("page_stay", { path: from.fullPath, duration: Date.now() - enterAt });
        }
        enterAt = Date.now();
      });
    },
    install(app: App) {
      app.config.globalProperties.$track = track;
      app.provide("track", track);
      // 点击埋点指令：v-track="{ event: 'click_buy', sku: 1 }"
      app.directive("track", {
        mounted(el: HTMLElement, binding) {
          const handler = () => track(binding.value.event, binding.value);
          el.addEventListener("click", handler);
          (el as any)._track = handler;
        },
        unmounted(el: HTMLElement) {
          el.removeEventListener("click", (el as any)._track);
        },
      });
    },
  };
}

// main.ts：
// const tracker = createTracker({ endpoint: "/api/track", sampleRate: 0.5 });
// app.use(tracker).use(router);
// tracker.installRouter(router);
// 模板：<button v-track="{ event: 'click_buy', skuId: 1 }">购买</button>
```
