---
title: [VIZ-285] 手写图表缩略轴（Overview + Detail）：minimap 联动
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-285：手写图表缩略轴（Overview + Detail）：minimap 联动

**答**：
- 题目：缩略轴（overview+detail）——底部全量缩略图 + 主图窗口；缩略图上拖动/捏合窗口改变主图 domain。
- 思路：缩略图：全量数据降采样画一遍；窗口刷子：可拖拽矩形（左右柄调整宽度）；联动：窗口 → 主图 domain。
- 评分点：缩略图降采样（M4 复用）；窗口柄拖拽；双端联动防环。

```javascript
class MiniMapBrush {
  constructor(fullDomain, viewEl) { this.full = fullDomain; this.window = [...fullDomain]; }
  dragHandle(handle, dx) {                                  // 左右柄
    const span = this.full[1] - this.full[0];
    const dv = dx / viewEl.width * span;
    if (handle === 'left') this.window[0] = clamp(this.window[0] + dv, this.full[0], this.window[1] - span * 0.05);   // 最小窗口
    else this.window[1] = clamp(this.window[1] + dv, this.window[0] + span * 0.05, this.full[1]);
    this.onChange(this.window);
  }
  dragBody(dx) {                                            // 整体平移
    const dv = dx / viewEl.width * (this.full[1] - this.full[0]);
    const width = this.window[1] - this.window[0];
    let start = this.window[0] + dv;
    start = clamp(start, this.full[0], this.full[1] - width);
    this.window = [start, start + width];
    this.onChange(this.window);
  }
}
```
