---
title: [ALG-194] 前端 SDK 对本地埋点发送做限流：每秒最多 10 条，超出的直接丢弃。如何实现固定窗口限流？它有什么缺陷？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-194：前端 SDK 对本地埋点发送做限流：每秒最多 10 条，超出的直接丢弃。如何实现固定窗口限流？它有什么缺陷？
**答**：固定窗口：维护"当前窗口起始时间 + 计数"，请求到来时若已超出窗口时长则重置窗口与计数；计数未满放行并加一，满了拒绝。O(1)。缺陷是边界突刺：两个窗口交界处可能瞬间放过 2 倍流量（如上一窗口末尾 10 条 + 下一窗口开头 10 条都落在 1 秒内），对突发敏感的场景要用滑动窗口或令牌桶。

```javascript
function fixedWindowLimit(max, windowMs) {
  let count = 0;
  let windowStart = Date.now();
  return function allow() {
    const now = Date.now();
    if (now - windowStart >= windowMs) {   // 窗口过期：重置
      windowStart = now;
      count = 0;
    }
    if (count < max) {
      count++;
      return true;                         // 放行
    }
    return false;                          // 拒绝：UI 提示操作过快或延后重试
  };
}
// 缺陷：窗口边界突刺——交界瞬间最多放过 2 × max 条
// 例：23:59:59.9 放 10 条，00:00:00.1 又放 10 条，0.2s 内 20 条
```
