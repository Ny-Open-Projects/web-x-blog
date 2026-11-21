---
title: [DP-279] 源码识别：View Transition API 源码中的快照与命令流？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-279：源码识别：View Transition API 源码中的快照与命令流？
**答**:
- 备忘录（快照对）：document.startViewTransition(callback) 在 DOM 变更前捕获旧快照（::view-transition-old）、变更后捕获新快照（new）——动画在两个快照间插值，真实 DOM 早已切换。
- 命名组合：view-transition-name 标记独立动画单元（元素级快照），同名的 old/new 配对。
- 状态机：capturing → updating（callback 执行）→ animating → finished，animation.finished promise 链。
- 识别要点：能说清"异步 callback 要等 promise"（async/await inside startViewTransition，转场等待数据就绪才播放新快照）。

```javascript
// View Transition（源码级心智）
async function navigateWithTransition(to) {
  const vt = document.startViewTransition(async () => {
    await router.push(to);          // DOM 更新（可异步等待数据）
    await dataReady;                // promise resolve 才捕获新快照
  });
  vt.ready.then(() => animateExtra()).catch(() => {});    // 状态机：animating
  await vt.finished;
}
// CSS 驱动：
// ::view-transition-old(root) { animation: fade-out .2s }
// ::view-transition-new(root) { animation: fade-in .2s }
// .card { view-transition-name: card-3 }  → 元素级独立快照（卡片跨页位移动画）
```
