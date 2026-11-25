---
title: [AGT-635] 手写 TraceTree：span 开闭、树构建、关键路径、耗时聚合（并行取max）？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-635：手写 TraceTree：span 开闭、树构建、关键路径、耗时聚合（并行取max）

**需求与边界**：
- 实现 TraceTree：startSpan(name, parent)/endSpan(id)/criticalPath()/summary()。
- 边界要求：① span 带开始/结束时间，未关闭的 span 在 summary 标记 open（视为异常）；② 关键路径 = 决定总时长的链路（并行子 span 取 max 而非相加）；③ summary 含总时长/成本（可加）/open 数；④ 空树与单 span 正常。

**答**：
```javascript
class TraceTree {
  constructor() { this.spans = new Map(); this.roots = []; }
  startSpan(name, parent = null, attrs = {}) {
    const s = { id: genId(), name, parent, attrs,
      t0: Date.now(), t1: null };
    this.spans.set(s.id, s);
    if (!parent) this.roots.push(s.id);
    return s.id;
  }
  endSpan(id) {
    const s = this.spans.get(id);
    if (!s) throw new Error('span not found');
    s.t1 = Date.now();
  }
  duration(s) { return (s.t1 ?? Date.now()) - s.t0; }
  criticalPath(node = this.roots[0]) {          // 关键路径：并行取max
    const s = this.spans.get(node);
    const kids = [...this.spans.values()].filter(x => x.parent === node);
    if (!kids.length) return [node];
    let best = null, bestDur = -1;
    for (const k of kids) {
      const d = this.pathDur(k);
      if (d > bestDur) { bestDur = d; best = k; }
    }
    return [node, ...this.criticalPath(best.id)];
  }
  pathDur(id) {                                 // 子树关键时长
    const s = this.spans.get(id);
    const kids = [...this.spans.values()].filter(x => x.parent === id);
    const childMax = kids.length
      ? Math.max(...kids.map(k => this.pathDur(k.id))) : 0;
    return Math.max(this.duration(s), childMax); // 并行取max
  }
  summary() {
    const spans = [...this.spans.values()];
    return {
      totalMs: this.pathDur(this.roots[0]),
      cost: spans.reduce((a, s) => a + (s.attrs['cost.usd'] ?? 0), 0),
      open: spans.filter(s => !s.t1).length,     // 未关闭=异常信号
    };
  }
}
```

**评分点**:
- 关键路径正确（并行子 span 取 max，串行链路累加），非简单求和。
- summary 成本可加总、open span 计数（异常信号）。
- 未关闭 span 用当前时间兜底 duration（不崩）。

