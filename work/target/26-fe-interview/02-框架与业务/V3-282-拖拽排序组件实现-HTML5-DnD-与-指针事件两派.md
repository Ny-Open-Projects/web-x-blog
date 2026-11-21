---
title: [V3-282] 拖拽排序组件的实现：HTML5 DnD 与指针事件两派怎么选？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-282：拖拽排序组件的实现：HTML5 DnD 与指针事件两派怎么选？
**答**：
- HTML5 DnD（draggable）：浏览器原生事件流（dragstart/dragover/drop），免手写捕捉；缺点：移动端不支持、幽灵图不可控、插入位置计算依赖 drop 位置事件、触发节流不定。
- 指针事件派（pointerdown/move/up + setPointerCapture）：全平台一致、可自定义占位/预览、支持触屏与键盘（可加键盘排序适配 a11y）；成本是要自己处理滚动容器边缘自动滚动。
- 选型：C 端移动项目必须指针派；中后台桌面项目 HTML5 DnD 快速落地；跨端一致或需要精细视觉反馈用指针派或 dnd-kit 类库。
- 排序核心：move 时计算目标索引（比较指针与各 item 中点），本地先**乐观交换**（数据驱动 UI），drop 后再提交给后端；失败回滚顺序。
- 性能：move 中只更新 transform 的预览层，不重排列表 DOM（列表用 fixed 定位 + translateY）。

```typescript
function useDragSort(items, onCommit) {
  const draggingIndex = ref(-1), overIndex = ref(-1);
  function onPointerDown(e, i) {
    draggingIndex.value = i; (e.target).setPointerCapture(e.pointerId);
  }
  function onPointerMove(e) {
    if (draggingIndex.value < 0) return;
    const idx = findIndexByY(e.clientY);              // 遍历各 item 中点
    if (idx !== overIndex.value) overIndex.value = idx; // 视觉：目标位高亮
  }
  function onPointerUp() {
    if (draggingIndex.value < 0) return;
    const from = draggingIndex.value, to = overIndex.value;
    if (to > -1 && to !== from) {
      const next = [...items.value];
      next.splice(to, 0, ...next.splice(from, 1));    // 乐观交换
      onCommit(next).catch(() => items.value = [...items.value]); // 失败回滚
      items.value = next;
    }
    draggingIndex.value = overIndex.value = -1;
  }
  return { draggingIndex, overIndex, onPointerDown, onPointerMove, onPointerUp };
}
```
