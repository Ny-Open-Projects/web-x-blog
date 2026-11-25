---
title: [V3-537] 笔试：手写 useIntersectionObserver 与曝光埋点
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 性能]
type: 笔试题
---

## V3-537：笔试：手写 useIntersectionObserver

**答**：实现 `useIntersectionObserver(targetRef, cb, options)`：① 返回 { stop, isActive }——stop 停止观察、isActive 标记当前可见；② options 透传（root/rootMargin/threshold）；③ 自动生命周期（scope 内自动 stop）；④ 在其上实现 `useExposure(trackFn, { dwellMs = 1000 })`：元素可见持续 dwellMs 后触发一次曝光上报（会话内去重）；⑤ 快速划过不计。写出实现。

```javascript
import { ref, onScopeDispose, getCurrentScope } from 'vue';

export function useIntersectionObserver(targetRef, cb, options = {}) {
  const isActive = ref(false);
  let io = null;
  function start() {
    io = new IntersectionObserver((ents) => {
      isActive.value = ents[0].isIntersecting;
      cb(ents[0], io);
    }, options);
    if (targetRef.value) io.observe(targetRef.value);
  }
  start();
  const stop = () => { io?.disconnect(); io = null; };
  if (getCurrentScope()) onScopeDispose(stop);
  return { stop, isActive };
}

export function useExposure(targetRef, trackFn, { dwellMs = 1000, threshold = 0.5 } = {}) {
  let timer = null;
  const reported = new Set();
  const slot = targetRef.value?.dataset?.slotId ?? crypto.randomUUID();

  useIntersectionObserver(targetRef, ({ isIntersecting }) => {
    if (isIntersecting) {
      if (sessionStorage.getItem(`exp:${slot}`)) return;   // 会话去重
      timer = setTimeout(() => {
        sessionStorage.setItem(`exp:${slot}`, '1');
        reported.add(slot);
        trackFn(slot);                                     // 达到停留时长才上报
      }, dwellMs);
    } else {
      clearTimeout(timer);                                 // 快速划过取消
    }
  }, { threshold });
  return { reported };
}
```

**评分点**：
- IO 包装的生命周期管理（scope 自动 stop）
- 停留时长判定 + 离开取消（防刷量）
- 会话去重（slotId 级）
- threshold 透传（可见比例门槛）
