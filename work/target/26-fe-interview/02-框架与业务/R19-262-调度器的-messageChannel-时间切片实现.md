---
title: [R19-262] React 调度器怎么用 MessageChannel 实现时间切片？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-262：React 调度器怎么用 MessageChannel 实现时间切片？
**答**：
- 时间切片：workLoop 每执行若干 Fiber 单元检查 deadline（帧预算 ~5ms），超时让出主线程。
- 让出与回归：用 MessageChannel 的 postMessage 排宏任务（比 setTimeout 精确、无 4ms 最低延迟），下次消息回调继续从断点渲染。
- 为什么不用 rAF：rAF 与绘制帧绑定，时序不可控；MessageChannel 独立于绘制循环。
- 为什么不用微任务：微任务不可中断，切片失效。
- 降级：无 MessageChannel 环境（老浏览器）退化 setTimeout。
