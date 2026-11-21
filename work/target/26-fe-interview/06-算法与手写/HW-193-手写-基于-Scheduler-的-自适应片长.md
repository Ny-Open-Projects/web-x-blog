---
title: [HW-193] 手写自适应切片调度器——按设备性能动态调整片长（快机 30ms/慢机 15ms）与实时校准
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：切片片长按设备自适应：基线（navigator.hardwareConcurrency + deviceMemory 初值）+ 实时校准（观察 yield 后到下次任务开始的间隙——间隙小 = 设备忙 = 缩短片长）。快机大切片（调度开销占比低），慢机小切片（保交互）。

```javascript
class AdaptiveSlicer {
  #budget = 30;                                           // 初始 30ms
  #adjuster;
  constructor(tasks) { this.tasks = tasks; }
  #calibrate() {                                          // 实时校准：yield 后实际让出时长
    const t0 = performance.now();
    return scheduler?.yield?.().then(() => {
      const gap = performance.now() - t0;
      if (gap > 60) this.#budget = Math.max(15, this.#budget - 5);      // 让出等待久（设备忙）：缩片
      else if (gap < 25) this.#budget = Math.min(40, this.#budget + 5);  // 让出即回（空闲）：扩片
    }) ?? Promise.resolve();
  }
  async run() {
    let i = 0;
    while (i < this.tasks.length) {
      const start = performance.now();
      do { this.tasks[i++](); } while (i < this.tasks.length && performance.now() - start < this.#budget);
      await this.#calibrate();                            // 每次让出时校准下片片长
    }
  }
}
// 初始值参考：deviceMemory <= 4 → 15ms；hardwareConcurrency >= 8 → 30ms
// 自适应效果：快机 40ms 片（调度次数少总耗时低），慢机 15ms 片（INP 保住）—— 单一固定片长两头不讨好
// 校准信号：yield 后"实际恢复执行"的间隔 = 设备繁忙度（其他任务/渲染占用了让出窗口）
```

**评分点**：
- 自适应校准信号（yield 后恢复间隔反映设备繁忙度）——本题核心。
- 片长边界（15~40ms）与初始值按设备分级。
- PER-283 的固定预算升级为动态预算的理由（快慢机单一片长两头不讨好）。
- 无 scheduler 环境降级（PER-215 链）。
