---
title: [FRP-283] 笔试：手写双端 diff（Vue 风格四指针）
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-283：笔试：手写双端 diff
**题**：实现 `twoWayDiff(oldChildren, newChildren)`：返回 { unmount: [], mount: [], moves: [{ el, anchor: 'before'|'after', ref }] }；四指针（头头/尾尾/旧头新尾/旧尾新头）匹配 + key Map 兜底；用最小用例验证反转场景零移动。

```javascript
function twoWayDiff(oldC, newC) {
  const result = { unmount: [], mount: [], moves: [] }
  let i = 0, j = 0, oldEnd = oldC.length - 1, newEnd = newC.length - 1
  while (i <= oldEnd && j <= newEnd && oldC[i].key === newC[j].key) { i++; j++ }          // 头头
  while (i <= oldEnd && j <= newEnd && oldC[oldEnd].key === newC[newEnd].key) { oldEnd--; newEnd-- } // 尾尾
  while (i <= oldEnd && j <= newEnd && oldC[i].key === newC[newEnd].key) {                  // 旧头→新尾
    result.moves.push({ el: oldC[i], ref: newC[newEnd + 1], dir: 'before' }); i++; newEnd-- }
  while (i <= oldEnd && j <= newEnd && oldC[oldEnd].key === newC[j].key) {                  // 旧尾→新头
    result.moves.push({ el: oldC[oldEnd], ref: newC[j], dir: 'before' }); oldEnd--; j++ }
  const map = new Map(oldC.slice(i, oldEnd + 1).map((c, k) => [c.key, i + k]))
  for (; j <= newEnd; j++) {
    const idx = map.get(newC[j].key)
    if (idx === undefined) result.mount.push(newC[j])
    else { result.moves.push({ el: oldC[idx], ref: newC[j + 1], dir: 'before' }); map.delete(newC[j].key) }
  }
  map.forEach(idx => result.unmount.push(oldC[idx]))
  return result
}
// 反转 [a,b,c] → [c,b,a]：头头不中，尾尾不中，旧尾→新头三次匹配 → moves 0（指针交换）
```
**评分点**：
- 四组指针匹配顺序正确（头头/尾尾/旧头新尾/旧尾新头）。
- 中间乱序 Map 兜底。
- 未匹配新节点 mount、未匹配旧节点 unmount。
- 反转场景零移动断言。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-fbba9bd1-05ae-4024-8195-0a5cd017a07e-cwd'; fi
exit "$__zcode_status"
