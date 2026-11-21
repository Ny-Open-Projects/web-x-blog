---
title: [DP-228] 源码识别：Vue Router 导航守卫源码中的职责链与错误流？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-228：源码识别：Vue Router 导航守卫源码中的职责链与错误流？
**答**:
- 职责链（文档化最清晰）：resolveHooks（beforeEach/resolve）→ beforeRouteEnter → 全局 confirmHooks → 组件更新钩子 → afterHooks，runGuardQueue 把每组串成队列，返回值驱动下一轮。
- 错误传播：守卫 throw / 返回 Error → 导航中止并进入 router.onError 链（错误也是职责链）。
- 命令递归：redirect 结果重新走 navigate（DP-210 同款），vue-router 源码里 navigate 嵌套调用直到目标稳定。
- 识别要点：能画出守卫执行顺序图（8 个钩子的时序）并在"组件内 beforeRouteUpdate vs beforeRouteEnter"上不出错。

```javascript
// Vue Router runGuardQueue（源码级简化）
const runGuardQueue = guards => guards.reduce((p, g) => p.then(() => g()), Promise.resolve());
async function navigate(toLocation, from) {
  const guards = [];
  // 1) 全局 beforeRouteLeave（离开组件）→ 2) 全局 beforeEach → 3) 路由级 beforeEnter
  guards.push(...extractComponentsGuards(matchedRecords, 'beforeRouteLeave', ...).reverse());
  guards.push(...router.beforeHooks.map(g => () => g(toLocation, from)));
  guards.push(...matched.map(r => r.beforeEnter).filter(Boolean));
  await runGuardQueue(guards);
  // 4) 全局 beforeResolve → 5) 组件内 beforeRouteUpdate/Enter
  await runGuardQueue(confirmingGuards);
  commitNavigation(toLocation);                              // 提交 + afterHooks
  router.afterHooks.forEach(h => h(toLocation, from));
}
// 错误流：任何 guard throw → navigate 顶层 catch → errorHandlers.forEach(h => h(err))
```
