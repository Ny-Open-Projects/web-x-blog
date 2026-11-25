---
title: [WCN-260] Signals flush 与浏览器事件循环的时序细节（点击→写→flush→绘制）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-260：Signals flush 与浏览器事件循环的时序细节（点击→写→flush→绘制）？
**答**：
- 点击处理器内写信号 → 微任务 flush → DOM 更新 → 同帧绘制：用户感知一次更新（无中间帧）。
- 若 flush 推迟到宏任务（rAF）：可能多出一帧旧内容——默认微任务更稳。
- 连续高频事件（输入）：每次事件微任务 flush，频率=事件频率——需要额外节流时显式 throttle。
- 测量：Performance 面板看「写→DOM 更新」延迟（应 < 1 帧）。

```javascript
input.addEventListener('input', () => {
  query.value = input.value;   // 写
});                              // 微任务内 flush → DOM 更新 → 本帧绘制
// 长队列场景显式节流：
const slow = throttledSet(query, 100);
r
```
