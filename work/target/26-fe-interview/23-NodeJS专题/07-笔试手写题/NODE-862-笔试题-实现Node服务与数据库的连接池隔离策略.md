---
title: [NODE-862] 笔试题——实现连接池隔离策略（快慢池 + 动态调整）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-862：手写池隔离

**需求与边界**：
- 需求：池隔离（SCN-NODE-643）——① 快慢池分离（快接口/慢查询独立池——SCN-NODE-643）；② 动态池大小（慢池压力 → 快池扩容——SCN-NODE-834 弹性）；③ 池间借用（快池空闲时借给慢池——资源利用率）；④ 全局容量校验（SCN-NODE-699）。
- 边界：① 池间借用的归还（借出连接归还原池——不永久迁移）；② 慢池饱和的降级（慢查询排队——SCN-NODE-639 快速失败）；③ 池配置热更（SCN-NODE-663）。

**答**：
```javascript
class IsolatedPools {
  constructor({ fast: { max: 20 }, slow: { max: 5 } }) {}
  async query(sql, { kind = classify(sql) } = {}) {    // 分类路由（SCN-NODE-643）
    const pool = kind === 'fast' ? this.fast : this.slow;
    try { return await pool.acquireWithTimeout(sql, 2000); }   // SCN-NODE-639 快速失败
    catch (e) {
      if (kind === 'slow' && this.fast.idle > 5)       // 快池空闲借用（资源利用）
        return this.fast.borrowTo(this.slow, { returnAfter: 'query' });   // 归还原池
      throw e;
    }
  }
  rebalance() {                                        // 动态调整（SCN-NODE-834）
    const pressure = this.slow.waiting / this.slow.max;
    if (pressure > 0.8) this.expand(this.slow, { by: 2, within: dbCapCheck() });   // SCN-NODE-699 校验
  }
}
```

**评分点**:
- 快慢池分类路由（SCN-NODE-643 池隔离）。
- 池间借用 + 归还（资源利用率——不永久迁移）。
- 动态扩容 + 全局校验（SCN-NODE-699/834）。
- 快速失败语义（SCN-NODE-639）。
