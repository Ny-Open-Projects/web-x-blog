---
title: [PER-805] 小程序长列表的 recycle-view 方案：节点回收原理与接入要点
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-805：小程序长列表的 recycle-view 方案：节点回收原理与接入要点

**答**：
- 原理：只渲染可视区 + 前后缓冲区的节点（通常 20~30 个），滚动时把离场节点"回收"（隐藏/复用）给新进入的行，配合首尾占位（撑出真实滚动高度）避免滚动条跳动。
- 与 H5 虚拟列表的差异：小程序回收要靠 fixed 定位或 transform 摆位（无 absolute 大容器方案更稳），且回收节点要重置组件状态（订阅/定时器），否则状态残留。
- 接入要点：行高固定用固定高度模式（性能最好）；不定高用占位测量（先渲染测高再入缓存）。触底加载与回收边界要防抖（加载中禁止回收）。
- 度量收益：页面节点数从 1 万级降到几百级，setData 数据量按可视行裁剪，低端机滚动帧率提升明显。

```javascript
// recycle-view 核心摆位逻辑（简化）
class Recycler {
  constructor({ itemH = 88, buffer = 5, total }) {
    this.itemH = itemH; this.buffer = buffer; this.total = total;
  }
  onScroll(scrollTop) {                          // 计算当前应渲染区间
    const start = Math.max(0, Math.floor(scrollTop / this.itemH) - this.buffer);
    const end = Math.min(this.total,
      Math.ceil((scrollTop + VIEWPORT_H) / this.itemH) + this.buffer);
    return { start, end,
      topPad: start * this.itemH,                // 头部占位撑高度
      bottomPad: Math.max(0, (this.total - end) * this.itemH),
    };
  }
  recycle(leavingNodes) {                        // 回收：重置状态再复用
    leavingNodes.forEach(n => { n.reset(); n.detach(); POOL.push(n); });
  }
}
```
