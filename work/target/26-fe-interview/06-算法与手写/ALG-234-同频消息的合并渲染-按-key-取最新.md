---
title: [ALG-234] 行情列表：一帧内 200 条 tick 按 key 取最新渲染（Map 合帧聚合）
date: 2026-11-19
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

**场景**：行情 WS 每秒 200 条 tick，同标的多次更新——逐条渲染 200 次 = INP 爆炸。合帧：一帧内的 tick 按 symbol 收敛为最新一条，每帧渲染一次。

**思路**：tick 入 Map（symbol → 最新 tick），rAF flush 一次渲染 Map 值；变价颜色动画用 CSS transition（合成器）避免逐条 class 切换卡顿。

```javascript
class TickAggregator {
  constructor(render) { this.map = new Map(); this.render = render; this.scheduled = false; }
  push(tick) {
    const prev = this.map.get(tick.symbol);
    this.map.set(tick.symbol, tick);                 // 同 key：只留最新（中间价无所谓）
    if (!this.scheduled) {
      this.scheduled = true;
      requestAnimationFrame(() => {
        this.scheduled = false;
        this.render([...this.map.values()]);         // 每帧一次，渲染净状态
        this.map.clear();
      });
    }
  }
}
const agg = new TickAggregator((ticks) => {
  for (const t of ticks) {
    const row = rows[t.symbol];
    row.textContent = t.price.toFixed(2);
    row.classList.toggle('up', t.delta > 0);         // 颜色动画交给 CSS transition（合成器）
  }
});
// 200 tick/秒 → 每帧（60fps）约 3~4 条聚合渲染，主线程占用 < 2%
// 关键语义：同 symbol 中间价丢弃（用户只关心最新价）——丢中间不丢最新
```

**评分点**：
- Map 按 key 合帧取最新（200 条/秒 → 每帧一次渲染）——本题核心。
- rAF 调度一次 flush（scheduled 防重复）。
- "丢中间价不丢最新"的业务语义说明（行情 vs 消息的差异）。
- 颜色变化走 CSS transition（合成器路径）。
