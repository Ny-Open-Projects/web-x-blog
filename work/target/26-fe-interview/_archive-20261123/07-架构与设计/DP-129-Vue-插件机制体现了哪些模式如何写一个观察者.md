---
title: [DP-129] Vue 插件机制体现了哪些模式？如何写一个"观察者 + 外观"插件？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-129：Vue 插件机制体现了哪些模式？如何写一个"观察者 + 外观"插件？（高频）
**答**：
- 插件机制骨架：`app.use(plugin, options)` 调用插件的 `install(app)`，并支持 `app.config.globalProperties` 挂全局 API——外观模式给业务统一入口。
- 观察者体现：插件内部监听 app 级事件（router 钩子、全局错误、生命周期）代替业务手动埋点，业务无感接入。
- 典型实现：监控插件 = install 时订阅 onError/onUnhandledrejection（观察者）+ 暴露 `$monitor`（外观）。

```javascript
// monitor-plugin.js：观察者收事件，外观给业务
export default {
  install(app, options) {
    const events = [];
    // 观察者：替业务订阅全局异常（业务零侵入）
    app.config.errorHandler = (err, instance, info) => {
      events.push({ type: 'render-error', msg: err.message, info, at: Date.now() });
      options.onError?.(err);
    };
    window.addEventListener('unhandledrejection', (e) => events.push({ type: 'promise', msg: String(e.reason) }));
    // 外观：统一 API 收口，业务只认 $monitor
    const monitor = {
      track(event, props = {}) { events.push({ type: event, ...props }); },
      report() { return navigator.sendBeacon(options.endpoint, JSON.stringify(events.splice(0))); },
    };
    app.config.globalProperties.$monitor = monitor;             // 老写法入口
    app.provide('monitor', monitor);                            // 组合式入口（推荐）
    // 模板方法语义：router 存在则自动挂页面上报
    app.config.globalProperties.$router?.afterEach?.((to) => monitor.track('pv', { path: to.path }));
  },
};
// main.js：app.use(monitorPlugin, { endpoint: '/collect', onError: console.warn })
```
