---
title: [V3-540] 笔试：手写 useIntervalFn / useTimeoutFn（可暂停生命周期版）
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 并发]
type: 笔试题
---

## V3-540：笔试：手写 useIntervalFn

**答**：实现：① `useIntervalFn(cb, interval, { immediate })`：返回 { start, stop, pause, resume, isActive }——pause 停止但可 resume 续跑（与 stop 区别：stop 重置）；② useTimeoutFn(cb, ms, opts)：同构；③ 组件卸载自动 stop；④ immediate：创建时立即开始；⑤ pause/resume 的语义：pause 只清定时器保留状态，resume 重新调度。写出实现。

```javascript
export function useIntervalFn(cb, interval = 1000, { immediate = true } = {}) {
  let timer = null;
  const isActive = ref(false);

  function start() {
    if (isActive.value) return;
    isActive.value = true;
    timer = setInterval(cb, interval);
  }
  function stop() {
    clearInterval(timer); timer = null;
    isActive.value = false;
  }
  function pause() { clearInterval(timer); timer = null; }   // 保留 isActive, resume 续跑
  function resume() { if (isActive.value && !timer) timer = setInterval(cb, interval); }

  if (immediate) start();
  onScopeDispose(stop);          // 卸载彻底停止
  return { start, stop, pause, resume, isActive };
}
// useTimeoutFn 同构: setTimeout + 自动 isActive=false
export function useTimeoutFn(cb, ms, { immediate = true } = {}) {
  let timer = null;
  const isActive = ref(false);
  function start() { stop(); isActive.value = true; timer = setTimeout(() => { isActive.value = false; cb(); }, ms); }
  function stop() { clearTimeout(timer); timer = null; isActive.value = false; }
  if (immediate) start();
  onScopeDispose(stop);
  return { start, stop, isActive };
}
// 用法: 轮询/倒计时
const { pause, resume } = useIntervalFn(poll, 3000);
document.addEventListener('visibilitychange', () =>
  document.hidden ? pause() : resume());        // 页面隐藏暂停轮询
```

**评分点**：
- pause/resume 与 start/stop 的语义区分
- onScopeDispose 自动清理（composable 核心价值）
- isActive 响应式状态供 UI 绑定
- timeout 版的自动失活
