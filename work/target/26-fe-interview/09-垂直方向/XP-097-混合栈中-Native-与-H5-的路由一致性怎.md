---
title: [XP-097] 混合栈中 Native 与 H5 的路由一致性怎么保证？返回键怎么处理？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-097：混合栈中 Native 与 H5 的路由一致性怎么保证？返回键怎么处理？
**答**：
- 核心矛盾：H5 内部 `history` 栈与原生页面栈是两套栈，直接返回会"跳过 H5 内层页"或"白屏兜底失败"。
- 统一回退协议：H5 弹层/内层页先拦截——`popstate`/`hashchange` 监听；无可回退历史时经桥调 `page.canGoBack` 询问原生，由**原生统一执行 close/pop**，栈语义唯一。
- Android 物理返回：容器 Activity `onBackPressed` 转发给 WebView（`dispatchEvent` 触发 H5 的 popstate），H5 消费则不透传，未消费再走原生回退。
- iOS 侧滑手势：容器禁用系统全屏侧滑或做"先 H5 后退再容器 pop"的两段式，避免手势直接 pop 容器丢掉 H5 内层页。
- 栈同步纪律：H5 push 内层页必须 `history.pushState`（产生可回退记录）；容器销毁前清空回调注册；深链打开的 H5 页需 seed 一条基础栈保证返回有归属。

```javascript
// hybrid/back-handler.js —— 统一回退协议：H5 优先消费，原生兜底
let bridge, popConsumers = new Set();      // 页面注册的弹层关闭器（Dialog/Drawer）

export function installBackHandler(ctx) {
  bridge = ctx.bridge;
  history.pushState({ seed: true }, '');   // seed 栈：保证容器内始终有一条可回退记录
  window.addEventListener('popstate', onPopState);
  document.addEventListener('visibilitychange', syncSeed);
}

function onPopState() {
  // 1) H5 内部弹层优先关闭（最后注册先关闭，模拟栈行为）
  if (popConsumers.size) {
    const closer = [...popConsumers].pop();
    closer(); history.pushState({ guard: true }, '');   // 重新压栈，保持回退不透传
    return;
  }
  // 2) H5 还有内层页历史：已被本次 popstate 消费，通知原生栈无需动作
  if (history.state?.seed !== true) {
    bridge.call('page.h5ConsumedBack', {});
    return;
  }
  // 3) 只剩 seed 栈：回退权交给原生（容器 close/pop）
  bridge.call('page.requestNativeBack', {});
}

export function registerPopConsumer(closer) {
  popConsumers.add(closer);
  return () => popConsumers.delete(closer);  // 弹层卸载时注销，防内存泄漏
}
// 原生侧（Android onBackPressed / iOS 转场手势）：
//   先调 evaluateJavascript 触发 history.back()；收到 page.h5ConsumedBack 则吞掉本次返回
//   收到 page.requestNativeBack 或超时（H5 未响应 100ms）→ 执行容器回退
```
