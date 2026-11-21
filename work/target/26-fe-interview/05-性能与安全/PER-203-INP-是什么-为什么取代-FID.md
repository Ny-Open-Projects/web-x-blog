---
title: [PER-203] INP 是什么？为什么用它取代 FID 作为响应性核心指标？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-203：INP 是什么？为什么用它取代 FID 作为响应性核心指标？

**答**：
- 定义：INP（Interaction to Next Paint）衡量用户与页面交互后，到下一次视觉更新的总延迟，取整个生命周期内所有交互的"最差表现"（按 p98 口径统计）。2024 年 3 月起正式取代 FID，成为 Core Web Vitals 三指标之一，良好阈值 ≤ 200ms。
- FID 的缺陷：只统计"第一次交互的输入延迟"（事件被派发到 handler 开始执行的时间），既不看后续交互，也不看 handler 执行与渲染耗时——一个只在开屏时点一下就能"骗过" FID 的页面，INP 下无处遁形。
- INP 的三段构成：input delay（主线程忙导致事件排队）+ processing（事件 handler 执行）+ presentation delay（渲染下一帧）。任一段超标都会拖垮 INP，因此优化面覆盖主线程调度、handler 逻辑与渲染成本。
- 与 FID 的口径差异决定了数据会"变差"：接入后 P75 INP 明显高于原 FID 是正常现象，应按 INP 重新定阈值，而不是拿 FID 的 100ms 硬套。

```javascript
// FID 只测第一次交互的 input delay；INP 测每次交互到下一帧的完整耗时
// 一次点击的生命周期（INP 口径）：
// [事件排队] —— input delay ——> [handler 执行] —— processing ——> [渲染] —— presentation ——> 下一帧 paint
//
// 常见把 INP 打爆的写法：
listEl.addEventListener('click', (e) => {
  const item = filterHugeList(e.target.dataset.id); // processing 慢：同步重计算
  syncReportToBeacon();                              // 又叠一次同步 IO
  renderThousands(item);                             // presentation 慢：强制大范围 reflow/paint
});
// 优化方向：handler 里先同步做最小 UI 反馈（乐观更新），
// 重计算用 requestAnimationFrame / scheduler.yield 切片，重渲染走虚拟列表
```
