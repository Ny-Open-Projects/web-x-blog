---
title: [V3-311] 响应式系统怎么调试？debug 钩子与 onTriggerRef 怎么用？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-311：响应式系统怎么调试？debug 钩子与 onTriggerRef 怎么用？
**答**：
- watch/watchEffect 支持 `onTrack` / `onTrigger` 调试钩子：onTrack 记录「谁读了这个数据」，onTrigger 记录「哪个数据变化引发了本次重新执行」。
- `triggerRef(ref)`：手动强制触发 shallowRef 的订阅者——当整对象被替换但引用比较跳过时救急用。
- `markRaw` 排除不需要响应的第三方实例（地图、图表），防止 Proxy 包装导致的「怎么改都不更新」或性能损耗。
- devtools 的 Inspector 面板可视化组件依赖关系；配合 `__VUE_PROD_DEVTOOLS__` 控制生产关闭。
- 排查套路：先确认变更路径被 trigger（onTrigger 打日志），再确认订阅者未被清理（scope/keep-alive 缓存），最后确认调度队列（nextTick 时机）。
```javascript
watchEffect(() => list.value.join(), {
  onTrigger(e) { console.log('triggered by:', e.key, e.type, e.target) },
  onTrack(e) { /* 依赖收集日志 */ }
})
```
