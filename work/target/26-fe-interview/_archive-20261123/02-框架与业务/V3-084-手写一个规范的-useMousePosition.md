---
title: [V3-084] 手写一个规范的 useMousePosition（rAF 节流 + 卸载清理）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-084：手写一个规范的 useMousePosition（rAF 节流 + 卸载清理）？
**答**：
- 在 V3-023 基础版上强化两点工程规范：高频事件用 rAF 节流、副作用完整清理。
- mousemove 每秒可触发上百次，用 pending 标记把写入压缩到每帧一次，rAF 回调里才真正更新 ref。
- passive: true 声明监听器不调用 preventDefault，滚动性能更好。
- 卸载清理必须做三件事：removeEventListener、cancelAnimationFrame、复位 pending。

```typescript
// composables/useMouse.ts
import { onScopeDispose, ref } from "vue";

export function useMouse() {
  const x = ref(0);
  const y = ref(0);

  let rafId = 0;
  let pending = false;
  let lastEvent: MouseEvent | null = null;

  function onMove(e: MouseEvent) {
    lastEvent = e;
    if (pending) return; // 这一帧已排入队列，合并后续事件
    pending = true;
    rafId = requestAnimationFrame(() => {
      if (lastEvent) {
        x.value = lastEvent.clientX;
        y.value = lastEvent.clientY;
      }
      pending = false;
    });
  }

  window.addEventListener("mousemove", onMove, { passive: true });

  onScopeDispose(() => {
    window.removeEventListener("mousemove", onMove);
    cancelAnimationFrame(rafId); // 取消尚未执行的帧
    pending = false;
    lastEvent = null;
  });

  return { x, y };
}
```

## 第二十三章 状态管理实战

Pinia 在大型项目里的组织方式、循环依赖、持久化插件、与路由和 TanStack Query 的配合，是状态管理方向的进阶高频题。
