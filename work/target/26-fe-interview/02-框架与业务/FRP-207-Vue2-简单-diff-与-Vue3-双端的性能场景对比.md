---
title: [FRP-207] Vue2 简单 diff 与 Vue3 双端 diff 的性能场景对比？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-207：Vue2 简单 diff 与 Vue3 双端 diff 的场景对比？
**答**：
- Vue2（简单同位 diff + key Map）：头部插入 [a,b,c] → [d,a,b,c] 需要把 a/b/c 全部移动——O(n) 次 DOM 移动。
- Vue3 双端：旧尾 c 与新尾 c 匹配、旧首 a 与新次首 a……通过头头/头尾/尾头/尾尾四组指针匹配，d 只需一次前插。
- 反转场景：Vue2 简单 diff 全部重排；双端 diff 尾头匹配直接翻转，接近零移动。
- 极端劣势场景：双端也有失手时（旋转数组），退化为 keyed Map + LIS，仍优于 Vue2。
- 总结：双端 diff 以「指针匹配」消灭大部分移动，是 Vue3 列表性能提升的主因之一。
