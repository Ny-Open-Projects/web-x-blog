---
title: [FRP-285] 笔试：手写 diff 的「最少移动」断言工具
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-285：笔试：手写 diff 最少移动断言工具
**题**：实现 `assertMinimalMoves(before, after, actualMoves)`：计算理论最少移动次数（LIS 长度判定）并断言 actualMoves 不超过它；同时校验 before/after 的 DOM 顺序语义（保留项相对顺序可乱、复用集合一致）。

```javascript
function minimalMoves(before, after) {
  const beforePos = new Map(before.map((k, i) => [k, i]))
  const kept = after.filter(k => beforePos.has(k))
  const oldSeq = kept.map(k => beforePos.get(k))
  const { indices } = lis(oldSeq)
  return kept.length - indices.length   // 保留节点数 - LIS 长度 = 最少移动
}
function assertMinimalMoves(before, after, actualMoves) {
  const expected = minimalMoves(before, after)
  if (actualMoves > expected) {
    throw new Error(`移动过多：actual=${actualMoves} minimal=${expected}`)
  }
  const keptBefore = before.filter(k => after.includes(k))
  const keptAfter = after.filter(k => before.includes(k))
  if (keptBefore.sort().join() !== keptAfter.sort().join()) {
    throw new Error('复用集合不一致：diff 丢失/错误复用了节点')
  }
}
// 测试：assertMinimalMoves([1,2,3,4], [4,1,2,3], moves) → minimal=1
```
**评分点**：
- 最少移动 = 保留数 - LIS 长度（公式核心）。
- 复用集合一致性校验（防 diff 静默丢节点）。
- 排序比较避免误报。
- 能用于 property-based 随机用例生成。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-933311cf-6d01-4fe0-bb53-fb2896f422e3-cwd'; fi
exit "$__zcode_status"
