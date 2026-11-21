---
title: [V3-303] Vue 3.5 响应式重构后 ref 内部实现做了哪些优化？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-303：Vue 3.5 响应式重构后 ref 内部实现做了哪些优化？
**答**：
- ref 本体仍是一个带 `value` getter/setter 的对象，但内部 `dep` 换成了新的链表 Dep，trigger 只打版本号 + 调度。
- getter 首次读取时才创建 Dep 并建立链接（惰性依赖收集），未被读取的 ref 完全不产生依赖结构。
- setter 里用 `hasChanged`（`Object.is`）短路同值写入，避免无意义调度；对象值写入时对旧值做 `pauseTracking`/stop 防泄漏。
- 数组 ref 依赖同样走链表：`ref([])` push 时索引与 length 的依赖增量更新，不再像旧实现那样触发大范围 cleanup。
- 实务影响：`shallowRef` 与普通 ref 的性能差距在 3.5 明显缩小，深层数据也可放心用 reactive，只有超大集合才需要 shallow 策略。
```javascript
function ref(value) {
  const dep = null // 惰性创建
  return {
    get value() {
      const d = dep ??= new Dep()
      d.track()                 // 首次读取才收集
      return value
    },
    set value(nv) {
      if (Object.is(nv, value)) return
      value = nv
      dep?.version = ++globalVersion  // 只打版本
      notify(dep)
    }
  }
}
```
