---
title: [ZSM-328] store 写入侧抛异常会不会拖垮整个应用怎么兜底
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-328：store 写入侧抛异常会不会拖垮整个应用，怎么兜底

**答**:
- 风险面：updater/派生函数抛错（如 undefined 读属性）、订阅回调抛错（一个 listener 炸掉其余通知）、persist 写盘抛错——三者都发生在 setState 调用栈里
- 防线一：updater 边界 try-catch，失败回滚到写入前快照并上报，绝不让「半个新状态」落地（先算后换，原子提交）
- 防线二：通知循环逐个 listener 隔离 try-catch，一个订阅者出错不影响其他订阅者与主流程
- 防线三：派生函数只读不写、store 数据入口有 schema 兜底（见 ZSM-288）——从源头减少异常

```javascript
function safeSetState(store, patch) {
  const snapshot = store.getState()
  try {
    const next = typeof patch === 'function' ? patch(snapshot) : { ...snapshot, ...patch }
    store.setState(() => next)                    // 原子提交
  } catch (e) {
    report('store_update_error', e)
    store.setState(() => snapshot)                // 回滚保证一致性
  }
}
// 订阅隔离
listeners.forEach((l) => { try { l(state) } catch (e) { report('listener_error', e) } })
```
