---
title: [WCN-196] 笔试：手写组件级 Long Task 归因监控器（PerformanceObserver + 组件归因）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, 选型与工程落地]
type: 笔试题
---

## WCN-196：笔试：手写组件级 Long Task 归因监控器

**题目**：实现 `startWcLongTaskMonitor(report)`：① PerformanceObserver 监听 longtask（>50ms）；② 归因：用 task attribution（PerformanceLongTaskTiming 的 containerName/containerSrc）尽力映射到组件；③ 组件主动标记：提供 `markWcWork(tag)` / `clearWcWork(tag)` 包裹重计算（重计算期间的 longtask 归因给该组件——用"最近标记栈"策略）；④ 汇总：每组件 longtask 总时长/次数，超阈值（组件累计 >500ms/分钟）告警；⑤ 返回 stop。

**答**：

```javascript
export function startWcLongTaskMonitor(report) {
  const stats = new Map();              // tag -> { count, totalMs }
  const markStack = [];                 // 最近标记栈（LIFO 归因）

  const po = new PerformanceObserver((list) => {
    for (const t of list.getEntries()) {
      const tag = markStack.at(-1) ?? guessFromAttribution(t);
      const s = stats.get(tag) ?? { count: 0, totalMs: 0 };
      s.count++; s.totalMs += t.duration;
      stats.set(tag, s);
      if (s.totalMs > 500) {
        report({ tag, ...s, level: 'warn' });  // 累计超阈值告警
        s.totalMs = 0; s.count = 0;            // 触发后重置窗口（1 分钟窗口近似）
      }
    }
  });
  po.observe({ type: 'longtask', buffered: true });

  function guessFromAttribution(t) {
    // containerType/name 常为 'window'；尝试从 attr 数据推断（尽力归因）
    const a = t.attribution?.[0];
    return a?.containerName || 'unknown';
  }

  return {
    markWcWork(tag) { markStack.push(tag); },
    clearWcWork(tag) { const i = markStack.lastIndexOf(tag); if (i >= 0) markStack.splice(i, 1); },
    stats,
    stop() { po.disconnect(); },
  };
}
// 组件用法：
// this.#m.markWcWork('acme-table');
// try { heavyRender(); } finally { this.#m.clearWcWork('acme-table'); }
```

**评分点**：
- PerformanceObserver longtask 口径（>50ms）；buffered 捕获早于监听的任务。
- 归因双层：主动标记栈（准确）+ attribution 尽力推断（兜底）。
- 窗口累计阈值告警 + 重置（避免误报循环）。
- mark/clear 配对语义（lastIndexOf 处理嵌套同名）。
