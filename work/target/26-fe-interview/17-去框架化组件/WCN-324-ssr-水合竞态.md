---
title: [WCN-324] 元素注册晚于用户交互（水合竞态）的处理？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-324：元素注册晚于用户交互（水合竞态）的处理？
**答**：
- 用户点击未注册元素 → 事件丢失（无监听）——需要「预注册捕获层」。
- 方案：根级统一委托（capture 阶段）暂存事件队列，元素注册后按序回放（或丢弃并提示重试）。
- 禁止项：注册后合成事件回放（可能与最新状态冲突）——回放只做「意图转换」（如重发请求）。
- 度量：水合前交互率（丢失交互数）——> 1% 需缩短注册延迟。

```javascript
document.addEventListener('click', (e) => {
  const el = e.target.closest('ds-x');
  if (el && !customElements.get('ds-x')) {
    pendingIntents.push({ el, type: 'click', at: Date.now() });  // 暂存意图
  }
}, true);   // capture：注册前也能收到
r
```
