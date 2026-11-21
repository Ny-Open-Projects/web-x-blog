---
title: [DP-272] 源码识别：在线表格源码中的单元格状态与协同？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-272：源码识别：在线表格源码中的单元格状态与协同？
**答**:
- 备忘录（快照+增量）：全量快照定期落盘 + 增量 op 流（setCell/insertRow），打开时"快照+回放增量"快速就绪。
- 状态机：单元格状态（idle/editing/computing/formula-error），公式依赖图驱动级联重算（拓扑排序）。
- 策略：协同锁策略——单元格级锁（编辑中他人置灰）或 CRDT 合并（数字单元格 last-write-wins）。
- 识别要点：公式引擎 = 解释器（DP-267 同款）+ 依赖图（DAG）+ 惰性重算（脏标记，改 A 只重算下游）。

```javascript
// 在线表格核心（源码级简化）
class Sheet {
  cells = new Map();           // 'A1' → { value, formula?, dirty }
  deps = new Map();            // 'A1' → Set<依赖 A1 的单元格>（反向依赖图）
  setCell(addr, formula) {
    this.cells.set(addr, { formula, dirty: true });
    rebuildDeps(addr, parseRefs(formula));       // 更新依赖边
    this.markDirtyDownstream(addr);              // 级联脏标记
  }
  recompute() {
    const order = topoSort(this.deps);           // 拓扑序：先算被依赖的
    for (const addr of order) {
      const c = this.cells.get(addr);
      if (!c?.dirty) continue;                   // 惰性：非脏跳过
      c.value = this.evalFormula(c.formula);     // 解释器求值
      c.dirty = false;
    }
  }
}
// 协同：编辑中单元格广播 cell-lock（他人渲染为锁定态）；提交后 op 广播 → 各端 markDirtyDownstream + recompute
```
