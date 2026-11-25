---
title: [WEB-168] Long Animation Frames API（LoAF）是干什么的？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-168：Long Animation Frames API（LoAF）是干什么的？
**答**：
- INP 差的时候只知道"这次交互慢"，LoAF 把慢帧拆开：每帧超过 50ms 时给出脚本耗时、阻塞时长、具体脚本 URL。
- 相比 Long Tasks：LoAF 覆盖到渲染相关阻塞，能定位到具体脚本与强制同步布局。
- 用法：PerformanceObserver 观察 long-animation-frame，把最重几帧连同交互信息上报。
- 修复路径：看 scripts 里 duration 集中在哪个模块 → 拆任务/延迟非关键代码/消除强制同步布局。

```javascript
new PerformanceObserver((list) => {
  for (const frame of list.getEntries()) {
    report('loaf', {
      duration: frame.duration,          // 帧总时长，达到 50ms 阈值才产生条目
      blocking: frame.blockingDuration,  // 超出 50ms 的阻塞部分
      scripts: frame.scripts.slice(0, 3).map((s) => ({   // 最重的脚本
        url: s.sourceURL || s.invokerType,               // 定位到文件或调用者
        duration: s.duration,
        forcedStyleAndLayout: s.forcedStyleAndLayoutDuration, // 强制同步布局
      })),
    });
  }
}).observe({ type: 'long-animation-frame', buffered: true });
```
