---
title: [MP-208] Taro 的 eventCenter 与跨页面通信怎么做？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-208：Taro eventCenter 与跨页面通信？
**答**：
- eventCenter：全局事件总线（on/off/emit），页面 A 修改数据后 emit，页面 B 监听刷新——弥补小程序无法在 navigateBack 时传参。
- 使用模式：类型化事件（TS 泛型约束事件名与 payload）；页面卸载 off 清理（防泄漏/重复触发）。
- 替代方案：全局状态（Pinia/zustand for Taro）、storage 轮询（不推荐）、navigateTo events 参数。
- 边界：事件是「广播」，慎用于强依赖时序的逻辑——顺序敏感场景用显式回调/store。
- 常见坑：组件重复挂载导致重复监听——useEffect cleanup 里 off。
