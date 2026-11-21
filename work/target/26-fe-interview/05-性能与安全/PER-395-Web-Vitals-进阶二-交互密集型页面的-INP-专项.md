---
title: [PER-395] 表格编辑器/设计工具类交互密集页面的 INP 专项：高频输入下的响应预算分配？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-395：表格编辑器/设计工具类交互密集页面的 INP 专项：高频输入下的响应预算分配？

**答**：
- 场景特征：每秒多次输入（键盘/拖拽/快捷键），每次交互都触发数据计算 + 渲染——INP 口径下"最差交互"决定指标，任何一次 400ms 的卡顿都会毁掉整体。专项思路是把"最差交互"压到预算内，而不是平均提速。
- 响应预算分配（单次交互 200ms 上限）：视觉反馈 ≤ 30ms（active 态/光标移动，同步、最轻）；状态计算 ≤ 50ms（ diff 计算，必要时切片）；渲染 ≤ 80ms（增量渲染只更新受影响单元格）；余量 40ms（GC/调度抖动）。
- 关键手段：① 输入去抖分层——键入立即回显（受控输入零延迟），重计算用 useDeferredValue 延后；② 增量计算——编辑一个单元格只重算受影响的行列（依赖图），拒绝全表重算；③ 渲染增量——脏区域更新（单元格级更新而非整表重渲染）；④ 快捷键命令入队——命令模式把重操作排队，逐个执行并保持每帧 ≤ 预算。
- 度量：交互密集页面的 INP 分位数 + 按交互类型拆分（键入/拖拽/快捷键各自 p95），最差类型优先治理。

```javascript
// 增量计算：单元格编辑只触发受影响区域
class SheetEngine {
  constructor(cells) { this.cells = cells; this.dependents = buildDepGraph(cells); }  // 依赖图
  edit(id, value) {
    const t0 = performance.now();
    this.cells.set(id, value);
    const dirty = collectDependents(this.dependents, id);      // 只收集受影响单元格
    for (const d of dirty) recompute(this.cells, d);
    if (performance.now() - t0 > 50) queueMicrotask(() => renderDirty(dirry));  // 超预算：渲染延后一拍
    else renderDirty(dirry);
    // 全表重算 10000 格 ≈ 300ms（INP 爆炸）；依赖图增量 ≈ 5~20ms
  }
}
// 预算分配：反馈 30ms / 计算 50ms / 渲染 80ms / 余量 40ms = 200ms 上限
```
