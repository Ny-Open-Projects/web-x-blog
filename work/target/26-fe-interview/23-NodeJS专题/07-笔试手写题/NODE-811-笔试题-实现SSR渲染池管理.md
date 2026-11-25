---
title: [NODE-811] 笔试题——实现 SSR 渲染池（isolate 复用 + 排队）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-811：手写渲染池

**需求与边界**：
- 需求：渲染 isolate 池（SCN-NODE-711）——① isolate 复用（V8 context 重置——不重建实例）；② 池满排队（渲染并发上限——SCN-NODE-639 池语义）；③ 渲染超时隔离（卡死 isolate 销毁重建——SCN-NODE-724 worker 超时同构）；④ 内存监控（isolate 内存上限——泄漏哨兵 SCN-NODE-672）。
- 边界：① 重置与新建的权衡（重置快但残留风险——模块级状态泄漏；新建干净但慢——按内存压力选择）；② 排队超时快速失败（SCN-NODE-639）；③ 渲染池水位遥测（SCN-NODE-726）。

**答**：
```javascript
class RenderPool {
  constructor({ size = 4, acquireTimeout = 1000 } = {}) {
    this.idle = Array.from({ length: size }, () => ({ iso: createIsolate(), renders: 0 }));
  }
  async render(fn) {
    const slot = this.acquire();                       // 排队（SCN-NODE-639 池语义）
    if (!slot) throw new Error('POOL_BUSY');           // 快速失败
    try {
      const result = await withTimeout(fn(slot.iso), 200);   // 渲染预算（SCN-NODE-756）
      slot.renders++;
      if (slot.iso.memoryUsed > 500e6 || slot.renders > 1000) {   // 内存/次数阈值
        this.recycle(slot);                            // 重置或新建（泄漏防御——SCN-NODE-672）
      }
      return result;
    } catch (e) { this.recycle(slot); throw e; }       // 异常 isolate 重建（状态可能损坏）
    finally { this.release(slot); }
  }
}
```

**评分点**:
- isolate 复用 + 池满快速失败（SCN-NODE-639 池语义）。
- 超时/异常 isolate 销毁重建（状态损坏防御——SCN-NODE-724 同构）。
- 内存与次数阈值双触发回收（SCN-NODE-672 泄漏哨兵）。
- 水位遥测（SCN-NODE-726 联动）。
