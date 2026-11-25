---
title: [V3-207] Vue 3.5 新增的 onWatcherCleanup 怎么用？解决什么旧痛点？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-207：Vue 3.5 新增的 onWatcherCleanup 怎么用？解决什么旧痛点？
**答**：
- 旧痛点：清理逻辑只能写在 watch/watchEffect 回调的**第三个参数 onCleanup** 里，深层封装的 composable 拿不到这个参数。
- 新 API：`onWatcherCleanup(fn)` 在 watcher 回调作用域内任意位置注册清理函数，下次重跑或停止时自动执行，语义同 onCleanup。
- 价值：让 `useXxx` 组合式函数内部自带"上次未完成请求取消"逻辑，不用从外层穿透 onCleanup 参数。
- 注意：必须**同步**在 watcher 回调执行期间调用，异步 setTimeout 里调用会失效并告警。
- 同期 API：`pauseTracking/resumeTracking`（依赖收集暂停）、`useId`、watch 的 `deep` 支持数组、`pause/resume` watcher。

```javascript
import { watchEffect, onWatcherCleanup } from 'vue';
// 深层封装的 composable 也能自带清理
function useSearch(keyword) {
  watchEffect(() => {
    const kw = keyword.value;
    const controller = new AbortController();
    fetch(`/api/search?q=${kw}`, { signal: controller.signal })
      .then((r) => r.json())
      .then((data) => render(kw, data));
    // 3.5：任意位置注册清理，不必依赖 onCleanup 参数层层透传
    onWatcherCleanup(() => controller.abort());
  });
}
// 旧写法必须：watchEffect(async (val, old, onCleanup) => onCleanup(() => ...))
```
