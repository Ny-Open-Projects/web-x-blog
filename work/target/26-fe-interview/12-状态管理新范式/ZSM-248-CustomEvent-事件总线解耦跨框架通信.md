---
title: [ZSM-248] 什么时候用 CustomEvent 事件总线而不是状态桥
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-248：什么时候用 CustomEvent 事件总线而不是状态桥

**答**：
- 判断标准：共享的是「状态」（需要最新值、可回读）还是「事件」（一次性通知，无当前值）——登录态/主题是状态，登出通知/埋点是事件
- CustomEvent 走 DOM 事件系统：跨框架零依赖、天然支持微前端边界（window/document 冒泡），但无回读、无顺序保证、事件名要全局唯一
- 状态桥必须单实例（全局单例 store）；事件总线可以多实例并存，解耦性更强
- 工程约定：事件名带命名空间（app:user:logout），payload 走 detail，监听方挂 window 防止 shadow DOM 截断冒泡

```javascript
// 发
window.dispatchEvent(new CustomEvent('app:cart:updated', { detail: { count: 3 } }))
// 收（React/Vue/任意框架一致）
useEffect(() => {
  const h = (e) => setCount(e.detail.count)
  window.addEventListener('app:cart:updated', h)
  return () => window.removeEventListener('app:cart:updated', h)
}, [])
```
