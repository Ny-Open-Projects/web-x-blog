---
title: [RBL-431] 笔试：手写构建缓存 LRU 清理器
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-431：手写构建缓存 LRU 清理器
**答**：实现 `evictCache(entries, { maxSize })`：1) entries：`[{ key, size, lastUsed, pinned }]`（pinned=关键任务缓存不可清）；2) 超过 maxSize 时按 lastUsed 升序（LRU）逐个删除，直到达标；3) pinned 条目跳过；全部 pinned 且仍超限 → 返回 { overLimit: true }（明确不可达而非静默）；4) 删除批次输出（可审计：删了哪些）；5) 保护策略：单次最多删 50%（防止一次清光导致雪崩全量重算）；6) 并发访问安全说明（清理与写入并发时的窗口语义）。

```javascript
export function evictCache(entries, { maxSize, maxRatio = 0.5 } = {}) {
  const sorted = [...entries].sort((a, b) => a.lastUsed - b.lastUsed)   // LRU 升序
  let current = entries.reduce((s, e) => s + e.size, 0)
  const evicted = []
  const limit = Math.floor(entries.reduce((s, e) => s + e.size, 0) * maxRatio)

  for (const e of sorted) {
    if (current <= maxSize) break
    if (e.pinned) continue
    if (evicted.reduce((s, x) => s + x.size, 0) >= limit) break    // 单批上限
    current -= e.size
    evicted.push(e)
  }

  return {
    evicted,
    freedBytes: evicted.reduce((s, e) => s + e.size, 0),
    overLimit: current > maxSize,
    remaining: current,
  }
}
// 并发语义：清理与写入并发 → 写入临时文件后 rename 原子替换；清理只删完整条目目录
// 读取中的条目：靠「先读后删」的时间窗 + 条目级别引用计数可选
```
**评分点**：
- LRU 排序正确（lastUsed 升序）；pinned 保护
- 单批 50% 上限（防清光雪崩——全量重算风暴）
- overLimit 显式（全 pinned 超限时明确返回不可达而非假装成功）
- 并发窗口语义说明（rename 原子 + 完整条目删除）
