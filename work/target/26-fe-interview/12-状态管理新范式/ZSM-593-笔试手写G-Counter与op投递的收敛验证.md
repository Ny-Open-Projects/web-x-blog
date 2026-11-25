---
title: [ZSM-593] 笔试：手写 G-Counter 与乱序 op 投递的收敛验证
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-593：手写 G-Counter 与乱序 op 投递的收敛验证
**答**：实现 op-based G-Counter：1) 三副本（A/B/C），本地 `increment(n)` 产生 op `{ device, delta, seq }` 并广播；2) `apply(op)`：按 `{device, seq}` 保证应用顺序——维护每 device 的已应用最高 seq，乱序到达时**先缓存（hold-back buffer）**，等前序补齐再按序应用；3) `merge(snapshot)`：state-based 合并（逐 device max）作为兜底恢复路径；4) `value()` 值为各 device 计数之和；5) 附用例：构造乱序投递场景验证缓存补齐后三副本收敛一致。

```javascript
class GCounter {
  constructor(deviceId) {
    this.id = deviceId
    this.shards = new Map()      // device -> applied value
    this.appliedSeq = new Map()  // device -> 最高已应用 seq
    this.buffer = new Map()      // device -> 未按序的 op 列表
    this.onBroadcast = null
  }

  increment(n = 1) {
    const seq = (this.appliedSeq.get(this.id) ?? 0) + 1
    const op = { device: this.id, delta: n, seq }
    this.shards.set(this.id, (this.shards.get(this.id) ?? 0) + n)
    this.appliedSeq.set(this.id, seq)
    this.onBroadcast?.(op)
  }

  apply(op) {
    const key = op.device
    const expect = (this.appliedSeq.get(key) ?? 0) + 1
    if (op.seq === expect) {
      this.shards.set(key, (this.shards.get(key) ?? 0) + op.delta)
      this.appliedSeq.set(key, op.seq)
      this.drain(key)            // 补齐缓存里连续的后续 op
      return
    }
    if (op.seq > expect) {
      // 乱序：先缓存
      const list = this.buffer.get(key) ?? []
      list.push(op)
      this.buffer.set(key, list)
    }
    // op.seq < expect：重复投递，幂等丢弃
  }

  drain(key) {
    const list = this.buffer.get(key)
    if (!list) return
    list.sort((a, b) => a.seq - b.seq)
    while (list.length && list[0].seq === (this.appliedSeq.get(key) ?? 0) + 1) {
      const op = list.shift()
      this.shards.set(key, (this.shards.get(key) ?? 0) + op.delta)
      this.appliedSeq.set(key, op.seq)
    }
    if (!list.length) this.buffer.delete(key)
  }

  // state-based 兜底：逐分片 max（增量永不丢）
  merge(snapshot) {
    for (const [device, v] of Object.entries(snapshot.shards)) {
      this.shards.set(device, Math.max(this.shards.get(device) ?? 0, v))
    }
  }

  value() { return [...this.shards.values()].reduce((a, b) => a + b, 0) }
  export() { return { shards: Object.fromEntries(this.shards) } }
}

// 用例：乱序投递收敛验证
const A = new GCounter('A'), B = new GCounter('B'), C = new GCounter('C')
const wire = []   // 模拟乱序网络
A.onBroadcast = B.onBroadcast = C.onBroadcast = (op) => wire.push(op)

A.increment(1); A.increment(2)   // A seq1 seq2
B.increment(5)
// 乱序投递：seq2 先于 seq1 到达 B
B.apply({ device: 'A', delta: 2, seq: 2 })   // 缓存
B.apply({ device: 'A', delta: 1, seq: 1 })   // 补齐 → drain 应用两条
B.apply({ device: 'A', delta: 2, seq: 2 })   // 重复：幂等丢弃
B.apply({ device: 'B', delta: 5, seq: 1 })
wire.forEach((op) => { A.apply(op); C.apply(op) })

console.log(A.value(), B.value(), C.value())   // 8 8 8：三副本收敛
A.merge(C.export())
console.log(A.value())                          // 8（merge 幂等）
```
**评分点**：
- 按 {device, seq} 的 hold-back 缓冲（乱序保序应用）
- 重复 op 幂等丢弃（seq < expect 直接忽略）
- 缓存 drain 的连续应用（补齐后级联释放）
- state-based merge 兜底 + 逐分片 max 的交换/结合/幂等性质
