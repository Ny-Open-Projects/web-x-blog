---
title: [V3-114] FLIP 动画在 Vue 中如何实现？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-114：FLIP 动画在 Vue 中如何实现？
**答**：
- FLIP 四步：First 记录起始位置、Last 让 DOM 变更后的最终位置生效、Invert 用 transform 反向偏移回起点、Play 过渡到 0。
- Vue 的 TransitionGroup 内部就是 FLIP，简单列表移动动画直接用它。
- 自定义场景（如拖拽落位、瀑布流重排）用手写 useFlip：watch 数据变化，nextTick 后对比前后 getBoundingClientRect，用 Web Animations API 播放。
- 每个可移动元素需要稳定的 data-flip-id 作为身份标识。

```typescript
// composables/useFlip.ts —— 手写 FLIP
import { nextTick, watch, type Ref } from "vue";

export function useFlip(container: Ref<HTMLElement | null>, source: () => unknown) {
  watch(source, async () => {
    await nextTick(); // 等 Vue 把 DOM 更新到最终状态
    const els = container.value?.querySelectorAll<HTMLElement>("[data-flip-id]");
    if (!els?.length) return;

    // First：更新后的 DOM 上已拿不到旧位置，改为在 watch 前缓存
    // 实现技巧：读取"变更前"的位置需要在数据变更前执行，这里用微任务前钩子：
    // 简化实现——依赖 Vue 的 DOM 更新在 nextTick 前完成，First 用 MutationObserver
    // 之外的常见做法是数据变化前手动调用 recordFirst()，示例如下注释
    //
    // recordFirst(): els.forEach((el) => firstMap.set(el, el.getBoundingClientRect()));
    // 数据变化 → nextTick → Last：再次读取最终位置
    // Invert：dx = first.left - last.left
    // Play：animate 从 translate(dx, dy) 过渡到 translate(0, 0)

    els.forEach((el) => {
      const first = (el as HTMLElement & { _flip?: DOMRect })._flip;
      if (!first) return;
      const last = el.getBoundingClientRect();
      const dx = first.left - last.left;
      const dy = first.top - last.top;
      if (dx || dy) {
        el.animate(
          [
            { transform: `translate(${dx}px, ${dy}px)` }, // Invert：先回到旧位置
            { transform: "translate(0, 0)" }, // Play：平滑过渡到新位置
          ],
          { duration: 300, easing: "ease" }
        );
      }
      // 更新为当前位置，供下一轮 FLIP 使用
      (el as HTMLElement & { _flip?: DOMRect })._flip = last;
    });
  });

  // 在数据变更前调用，记录 First 位置
  function recordFirst() {
    container.value?.querySelectorAll<HTMLElement>("[data-flip-id]").forEach((el) => {
      (el as HTMLElement & { _flip?: DOMRect })._flip = el.getBoundingClientRect();
    });
  }

  return { recordFirst };
}
```
