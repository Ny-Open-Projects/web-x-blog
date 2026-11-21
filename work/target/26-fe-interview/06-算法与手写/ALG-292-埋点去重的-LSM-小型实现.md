---
title: [ALG-292] 埋点去重的 LSM 小型实现：内存表 + 定期合并到 IDB（高吞吐去重的存储分层）？
date: 2026-11-19
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

**场景**：埋点去重（事件 id 是否已上报）高吞吐：每秒 50 事件 × IDB 逐条查询 = 压力大——LSM 思路：内存表（Set）吸收写与查询，攒批合并刷入 IDB（持久层），查询两级（内存→IDB）。

**思路**：memTable Set + size 上限 → flush（IDB 批量 put + memTable 清空）→ has 查两级 → flush 后旧 memTable 数据已持久。

```javascript
class LSMSet {
  #mem = new Set();
  #threshold = 500;
  constructor(store) { this.store = store; }
  async add(id) {
    this.#mem.add(id);
    if (this.#mem.size >= this.#threshold) await this.#flush();
  }
  async has(id) {
    if (this.#mem.has(id)) return true;                   // L1：内存表
    return this.store.has(id);                            // L2：持久层（IDB 批量预载或按需查）
  }
  async #flush() {
    const ids = [...this.#mem];
    await this.store.putBatch(ids);                       // 批量写（500 条一次事务，PER-324）
    this.#mem.clear();                                    // 清内存表（数据已在持久层）
  }
  async destroy() { await this.#flush(); }                // 页面卸载兜底：内存未刷的刷下去
}
// 读写放大控制：500 条一批 → IDB 事务数 -99%（对比逐条）
// 两级查询：内存 O(1) 命中大部分（近期事件），持久层兜底（历史事件）
// flush 边界：flush 后 mem 清空但数据在 L2——has 两级查不漏
// 页面卸载：visibilitychange/pagehide 触发 destroy（内存数据不丢，PER-252 兜底纪律）
```

**评分点**：
- LSM 两级分层（memTable 吸收 + 批量刷盘）——本题核心。
- 批量事务的写放大控制（-99% 事务数）。
- 两级查询语义（内存命中/持久兜底）不漏。
- 卸载兜底 flush（内存不丢）。
