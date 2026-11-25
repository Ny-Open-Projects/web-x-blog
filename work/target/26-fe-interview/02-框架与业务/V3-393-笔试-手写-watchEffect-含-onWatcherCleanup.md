---
title: [V3-393] 笔试：手写 watchEffect（依赖收集 + onWatcherCleanup）
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-393：笔试：手写 watchEffect（依赖收集 + onWatcherCleanup）
**答**：实现 `watchEffect(fn)`：自动收集 fn 内用到的响应式数据；依赖变化时先执行上轮注册的 cleanup 再重跑；组件卸载（手动 stop）时也执行 cleanup；重复触发需去重调度（一次微任务）。

```javascript
let activeEffect = null
const targetMap = new WeakMap()
function track(target, key) {
  if (!activeEffect) return
  let deps = targetMap.get(target); if (!deps) targetMap.set(target, deps = new Map())
  let set = deps.get(key); if (!set) deps.set(key, set = new Set())
  set.add(activeEffect)
  activeEffect.deps.add(set)          // 反向记录，便于清理
}
function trigger(target, key) {
  (targetMap.get(target)?.get(key) || []).forEach(e => schedule(e))
}
function watchEffect(fn) {
  const e = { deps: new Set(), cleanups: [], stop: () => runCleanups() }
  const runCleanups = () => { e.cleanups.forEach(fn => fn()); e.cleanups = [] }
  const run = () => {
    runCleanups()
    e.deps.forEach(set => set.delete(e)); e.deps.clear() // 清旧依赖
    const prev = activeEffect; activeEffect = e
    fn(cleanupFn => e.cleanups.push(cleanupFn))          // 注册清理
    activeEffect = prev
  }
  const schedule = () => { if (e.scheduled) return; e.scheduled = true; Promise.resolve().then(() => { e.scheduled = false; run() }) }
  run()
  return e.stop
}
```
**评分点**：
- 依赖先清理再收集，防止条件分支残留旧依赖。
- cleanup 在重跑前与 stop 时都执行。
- 微任务调度去重（scheduled 标记）。
- activeEffect 保存/恢复（嵌套安全）。
