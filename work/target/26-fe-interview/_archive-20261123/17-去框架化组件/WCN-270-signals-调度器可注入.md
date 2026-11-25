---
title: [WCN-270] 可注入调度器（自定义 flush 时机）的设计与用例？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-270：可注入调度器（自定义 flush 时机）的设计与用例？
**答**：
- 库默认微任务 flush；提供 configureScheduler({ schedule }) 注入自定义策略。
- 用例 1：测试环境同步 flush（确定性断言）。
- 用例 2：Worker 内 flush 后 postMessage（跨线程渲染协调）。
- 用例 3：帧对齐（rAF flush，与绘制同步——适合动画驱动）。
- 约束：注入调度器必须保证最终 flush（库层兜底 timeout 防丢失）。

```javascript
configureScheduler({
  schedule: (flush) => requestAnimationFrame(flush),   // 帧对齐
});
// 测试环境：
configureScheduler({ schedule: (flush) => flush() });  // 同步
r
```
