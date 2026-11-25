---
title: [ALG-235] 长列表拖拽排序：拖动超过一屏的目标定位（二分查找可视区 + 滚动联动）
date: 2026-11-19
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---
## ALG-235：长列表拖拽排序：拖动超过一屏的目标定位（二分查找可视区 + 滚动联动）
**答**：1000 行列表拖拽排序：拖到可视区外要自动滚动，落点目标在远处时不能用 O(n) 遍历找目标行——定高列表用二分（index = (y - top) / rowH），动态高度用前缀和二分（ALG-066 横向化）。

**思路**：pointermove 时按 y 二分定位目标行 index（O(logn)）；接近容器边缘触发自动滚动（rAF 每帧滚 fixed 步长）；落点用半线判定（HW-106）。

```javascript
function rowAt(y, { top, rowH, count }) {
  const idx = Math.floor((y - top) / rowH);
  return Math.min(count - 1, Math.max(0, idx));      // 定高：O(1)；动态高度用前缀和二分 O(logn)
}
class DragScroller {
  constructor(container, rowH, count) { Object.assign(this, { container, rowH, count }); this.autoScrolling = false; }
  onMove(y) {
    const rect = this.container.getBoundingClientRect();
    const edge = 40;                                  // 距边缘 40px 触发自动滚动
    const speed = y - rect.top < edge ? -12 : y - rect.top > rect.height - edge ? 12 : 0;
    if (speed) this.#autoScroll(speed); else this.#stopAuto();
    return rowAt(y, { top: rect.top + this.container.scrollTop, rowH: this.rowH, count: this.count });
  }
  #autoScroll(speed) {
    if (this.autoScrolling) return;
    this.autoScrolling = true;
    const step = () => {
      this.container.scrollTop += speed;
      if (this.autoScrolling) requestAnimationFrame(step);    // 每帧匀速滚动
    };
    requestAnimationFrame(step);
  }
  #stopAuto() { this.autoScrolling = false; }
}
// 落点目标定位 O(1)/O(logn)，1000 行列表拖拽无卡顿
// 自动滚动在 pointerup 或离开边缘时停止（#stopAuto 必须，防滚动失控）
```

**评分点**：
- 定高 O(1) / 动态高度前缀和二分 O(logn) 的目标行定位（拒绝 O(n) 遍历）。
- 边缘自动滚动：rAF 匀速 + 停止条件完整（up/离边缘）——防滚动失控是关键边界。
- 落点半线判定与 1000 行场景的复杂度说明。
- 滚动中坐标换算（rect.top + scrollTop）。
