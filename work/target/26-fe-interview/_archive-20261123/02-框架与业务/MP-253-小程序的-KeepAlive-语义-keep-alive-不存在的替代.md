---
title: [MP-253] 小程序没有 keep-alive，页面状态保留怎么实现？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-253：页面状态保留（无 keep-alive 的替代）？
**答**：
- 天然保留：页面栈内页面 navigateBack 返回时实例存活（数据/UI 状态自动保留）——无需额外处理。
- redirectTo 跳转后返回（页面被销毁）：用「状态持久化」——store 快照 + storage 草稿，onLoad 恢复。
- Tab 页：常驻不销毁，onShow 时刷新数据（静默更新保持状态）。
- 组件级：数据缓存到页面级 store/父页面；跨页共享列表滚动位置——记录 scrollTop 到 store，onShow 恢复。
- 设计含义：小程序的「返回」就是 KeepAlive，架构上要把「可恢复状态」设计成可序列化的（这也是面试常考的取舍点）。
