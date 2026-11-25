---
title: [ZSM-591] 简化 CRDT 的两种思路：计数器类与序列类分别怎么收敛
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-591：简化 CRDT 的两种思路：计数器类与序列类分别怎么收敛

**答**：
- CRDT 的本质：设计一种数据结构使得「任意顺序合并各副本的变更，最终状态一致」——不需要中心服务器仲裁。前端场景两大家族：
- **计数器类**：G-Counter（每副本一个分片计数，合并取逐分片 max/sum——增量永不丢失）；PN-Counter 支持「增减」（增集合与减集合分开，合并各自求和）。适合点赞数、统计。
- **序列类**（文本/列表）：RGA / Logoot 思路——每个字符/元素有全局唯一 id（`副本id+本地序号`），插入以「左邻居 id」定位；删除是墓碑标记（不物理移除，合并后统一清理）。两副本并发插入同一位置时按 id 排序决胜——两端顺序一致。
- 前端简化建议：完整 CRDT 库（Yjs、automerge）很重，业务上「计数器类 CRDT + 字段 LWW + 服务端兜底」覆盖 90% 需求；真正需要并发文本编辑才上 Yjs（自带 y-websocket 同步层）。
- 收敛验证：CRDT 正确性的金标准测试是「随机乱序投递两副本的全部操作，最终 fingerprint 相等」（ZSM-559 的指纹工具正好用来做验证）。

```javascript
// PN-Counter：增减分片合并
class PNCounter {
  constructor(deviceId, { inc = {}, dec = {} } = {}) {
    this.id = deviceId
    this.inc = { ...inc, [deviceId]: 0 }
    this.dec = { ...dec, [deviceId]: 0 }
  }
  increment(n = 1) { this.inc[this.id] += n }
  decrement(n = 1) { this.dec[this.id] += n }
  value() { return Object.values(this.inc).reduce((a, b) => a + b) - Object.values(this.dec).reduce((a, b) => a + b) }
  merge(other) {   // 逐分片 max：交换律+结合律+幂等
    for (const [id, v] of Object.entries(other.inc)) this.inc[id] = Math.max(this.inc[id] ?? 0, v)
    for (const [id, v] of Object.entries(other.dec)) this.dec[id] = Math.max(this.dec[id] ?? 0, v)
    return this
  }
}

// 简版序列 CRDT：id 定位插入 + 墓碑删除
class SimpleSequence {
  constructor(deviceId) {
    this.deviceId = deviceId
    this.items = []        // [{ id, ch, leftId, tombstone }]
    this.localSeq = 0
  }
  insert(leftId, ch) {
    const item = { id: `${this.deviceId}:${++this.localSeq}`, ch, leftId, tombstone: false }
    const idx = this.items.findIndex((i) => i.id === leftId)
    this.items.splice(idx + 1, 0, item)   // 本地视图即时插入
    return item
  }
  remove(id) {
    const item = this.items.find((i) => i.id === id)
    if (item) item.tombstone = true       // 墓碑：不物理删除
    return id
  }
  merge(op) {
    if (op.tombstone !== undefined) {     // 删除 op：标记墓碑
      const it = this.items.find((i) => i.id === op.id)
      if (it) it.tombstone = true
      return
    }
    const idx = this.items.findIndex((i) => i.id === op.leftId)  // 以左邻居定位
    const insertAt = idx + 1
    // 并发插入同位置：按 id 字典序决胜，两端一致
    while (insertAt < this.items.length && this.items[insertAt].id < op.id) break
    this.items.splice(insertAt, 0, { id: op.id, ch: op.ch, leftId: op.leftId, tombstone: false })
  }
  text() { return this.items.filter((i) => !i.tombstone).map((i) => i.ch).join('') }
}
```
