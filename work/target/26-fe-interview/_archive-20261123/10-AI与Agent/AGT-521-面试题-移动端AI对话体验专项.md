---
title: [AGT-521] 移动端 H5 内嵌 AI 对话，有哪些专项问题（键盘顶起、长任务保活、手势冲突）？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-521：移动端 H5 内嵌 AI 对话，有哪些专项问题（键盘顶起、长任务保活、手势冲突）

**答**：
- 软键盘是头号问题：iOS 用 visualViewport 监听视口变化来移动输入框（focus 时键盘顶起），Android 需处理 window resize；输入框要 sticky 在视口底部而非页面底部。
- 长任务（Agent 执行中）切后台会被杀：返回时用「对账恢复」——拉取任务最新状态补齐缺失片段，而不是装作无事发生。
- 手势冲突：对话区下拉刷新 vs 回到底部按钮；侧滑返回会误触，生成中要禁用侧滑或二次确认。

```javascript
// visualViewport 处理软键盘顶起
const vv = window.visualViewport;
vv.addEventListener('resize', () => {
  const kbH = window.innerHeight - vv.height;   // 键盘高度估算
  inputBar.style.transform = `translateY(${-kbH}px)`;
  msgList.style.paddingBottom = `${kbH + 16}px`;
});
document.addEventListener('visibilitychange', () => {
  if (document.visibilityState === 'visible' && turn.inFlight) {
    reconcileTurn(turn.id);   // 回前台对账：拉最终状态补片段
  }
});
```

