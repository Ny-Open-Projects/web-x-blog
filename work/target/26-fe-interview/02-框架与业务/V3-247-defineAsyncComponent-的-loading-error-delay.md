---
title: [V3-247] defineAsyncComponent 的 loading/error/delay/timeout 选项如何配合使用？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-247：defineAsyncComponent 的 loading/error/delay/timeout 选项如何配合使用？
**答**：
- delay（默认 200ms）：加载耗时短于 delay 不显示 loadingComponent，防止骨架闪烁；超过才显示。
- timeout：加载超时后渲染 errorComponent，常配 `onError` 上报；不设置则无限等待。
- retry：loader 支持 `loadFailed` 重试——`retry()` 由 errorComponent 调用（`onError` 里传入），实现手写重试按钮。
- 与 Suspense 关系：defineAsyncComponent 的 loading/error 是**组件级**兜底；Suspense 是**树级**等待（async setup）。两者可叠用：chunk 加载走组件级，数据等待走树级。
- 选型：弹窗/懒挂小组件用 defineAsyncComponent（不影响主树渲染）；首屏主内容用 Suspense 统一编排。

```javascript
const Editor = defineAsyncComponent({
  loader: () => import('./Editor.vue'),          // chunk 拆分
  loadingComponent: EditorSkeleton,              // delay 后显示
  delay: 200,
  errorComponent: {                              // 超时/失败视图
    props: ['retry', 'error'],
    template: `<div>编辑器加载失败 <button @click="retry()">重试</button></div>`,
  },
  timeout: 8000,
  onError(err, retry, fail, attempts) {          // 自动重试 2 次
    if (attempts <= 2) retry(); else fail();
    report('chunk_error', err);
  },
});
```
