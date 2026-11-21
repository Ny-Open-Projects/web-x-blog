---
title: [ALG-083] 长页面按"屏"切了 N 段懒加载区块，`segments[i]` 表示进入第 i 段最多可预加载到第几段之后，问从第 0 段出发能否把整页加载完（跳跃游戏）？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-083：长页面按"屏"切了 N 段懒加载区块，`segments[i]` 表示进入第 i 段最多可预加载到第几段之后，问从第 0 段出发能否把整页加载完（跳跃游戏）？
**答**：贪心维护"能到达的最远下标 far"：从左往右扫，若当前下标 i 超过 far 说明中间有断层返回 false；否则用 `i + segments[i]` 扩张 far，`far >= 末段` 即可达。时间 O(n)，空间 O(1)。

```javascript
function canReach(segments) {
  let far = 0;
  for (let i = 0; i < segments.length; i++) {
    if (i > far) return false;               // 当前段不可达
    far = Math.max(far, i + segments[i]);
    if (far >= segments.length - 1) return true;
  }
  return true;
}
```
