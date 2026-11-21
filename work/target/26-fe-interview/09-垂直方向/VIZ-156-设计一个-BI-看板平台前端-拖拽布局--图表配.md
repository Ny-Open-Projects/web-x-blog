---
title: [VIZ-156] 设计一个 BI 看板平台前端（拖拽布局 + 图表配置 + 联动）。（压轴）
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-156：设计一个 BI 看板平台前端（拖拽布局 + 图表配置 + 联动）。（压轴）
**答**：五个模块：① **拖拽布局**——12/24 栅格吸附引擎，widget 存 x/y/w/h，拖拽改坐标不重排 DOM，ResizeObserver 联动图表 resize；② **图表配置**——属性面板由 schema 驱动（VIZ-133），数据源选择器 + 字段映射；③ **数据层**——dataset 抽象（SQL/接口/Excel 上传统一为数据集），缓存 + 变更通知；④ **联动**——filterStore 总线（VIZ-139）；⑤ **持久化**——看板 JSON 序列化（布局 + 配置 + 数据源引用）+ 版本历史。性能：折叠 tab 不渲染、批量刷新节流、组件懒挂载。

```javascript
// 拖拽布局引擎：栅格吸附 + widget 状态
const GRID = 12, CELL = 100;
function snap(x, y) {                       // 像素 -> 栅格坐标
  return { gx: Math.round(x / CELL), gy: Math.round(y / (CELL / 2)) };
}
class Dashboard {
  #widgets = new Map();                     // id -> { x, y, w, h, chartId, option }
  onDragEnd(id, px, py) {
    const wgt = this.#widgets.get(id);
    const { gx, gy } = snap(px, py);
    if (this.collides({ ...wgt, x: gx, y: gy }, id)) return bounceBack(id); // 碰撞回弹
    Object.assign(wgt, { x: gx, y: gy });
    persistLayout(this.serialize());        // 布局防抖持久化
  }
  serialize() {                             // 看板 JSON：布局 + 配置 + 数据源引用
    return JSON.stringify({ widgets: [...this.#widgets.values()] });
  }
  collides(a, exceptId) {
    for (const [id, b] of this.#widgets)
      if (id !== exceptId && a.x < b.x + b.w && b.x < a.x + a.w &&
          a.y < b.y + b.h && b.y < a.y + a.h) return true;
    return false;
  }
}
```
