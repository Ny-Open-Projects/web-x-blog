---
title: [V3-305] watch 的 flush: 'sync' 适合什么场景？有哪些踩坑风险？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-305：watch 的 flush: 'sync' 适合什么场景？有哪些踩坑风险？
**答**：
- 默认 `flush: 'pre'`（组件更新前批量执行），`post` 在 DOM 更新后，`sync` 则**每次赋值立即执行**、不进队列。
- 合适场景：需要与源变化严格同步的低延迟联动，如 `v-model` 双向镜像到 URL hash、拖拽时同步 store、canvas 每帧重绘标记。
- 风险一：循环中多次改值会触发 N 次回调，回调里再写响应式数据容易造成死循环或性能雪崩（必须配合去重/节流）。
- 风险二：回调触发时 DOM 还是旧状态，回调里读 DOM 会拿到过期值；要用 DOM 就用 `post`。
- 建议：默认用 pre；只有「一致性要求 > 批量收益」时才用 sync，并保持回调幂等。
```javascript
watch(keyword, (v) => {
  history.replaceState(null, '', `?q=${encodeURIComponent(v)}`) // sync：地址栏与输入严格同步
}, { flush: 'sync' })
```
