---
title: [FRP-203] Vue3 快速 diff 的前置/后置处理覆盖哪些场景？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-203：Vue3 快速 diff 的前缀/后缀处理覆盖哪些场景？
**答**：
- 前缀同步：从头比较，key/type 相同则 patch 并前移 i1/i2——处理「追加新节点」场景，O(n) 就结束。
- 后缀同步：从尾比较，相同则 patch——处理「头部插入」场景。
- 中间乱序：i1/i2 未走完才进入——旧有剩余且新有剩余 → 构建新节点 key→index 映射做 keyed diff + LIS 移动；只有旧剩 → 批量 unmount；只有新剩 → 批量 mount。
- 收益：v-for 尾部 push/pop、头部 unshift 等高频操作完全避开 LIS 阶段。
- 对比 React：React 也要第一轮按位比较实现同样短路，思想相同。
