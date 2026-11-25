---
title: [WCN-420] 笔试：信号系统的 SSR 求值模式（无订阅直读）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-420：笔试：信号系统的 SSR 求值模式（无订阅直读）。
**题目**：SSR 环境：signal.get 直接返回值（无订阅收集——无 effect 循环）；computed 直接求值缓存（单次渲染生命周期）；序列化初值注册表。

```javascript
const isServer = typeof window === 'undefined';
function track(node) {
  if (isServer) return;                    // SSR：无订阅收集
  if (stack.length) { /* 正常收集 */ }
}
function serializeSignals(registry) {
  return JSON.stringify(registry.map(s => ({ id: s.id, v: s._v })));  // 下发
}
// 客户端 restore：值一致 → 水合首帧不触发 effect

```

**评分点**：
- SSR 守卫：isServer → track 为 no-op。
- 渲染结束快照注册表值（下发 HTML）。
- 客户端 restore（值一致 → 水合不重算）。
- 禁止：SSR 中 schedule（无微任务意义）——守卫告警。
