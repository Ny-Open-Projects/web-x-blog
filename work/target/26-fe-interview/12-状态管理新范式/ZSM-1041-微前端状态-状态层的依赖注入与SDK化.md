---
title: [1041] 微前端状态 SDK 化（依赖注入的标准接口）
date: 2026-11-17
categories: [状态管理新范式]
tags: [前端面试, 面试题, 微前端]
type: 面试题
---

## 1041：微前端状态 SDK 化（依赖注入的标准接口）

**答**：
- SDK 化动机：每个子应用手写总线订阅/门访问/生命周期清理——重复且易漏；平台提供 SDK（createAppSdk(deps)——统一封装总线/门/清理/调试钩子），子应用只写业务。
- SDK 接口：sdk.bus.publish/subscribe（自动带应用命名空间与版本）、sdk.gate（状态门访问）、sdk.onUnmount(fn)（清理注册——卸载时统一执行）、sdk.debug（快照/录制钩子自动接入）。
- SDK 的治理红利：所有子应用的状态行为走同一 SDK——探针/监控/规范在 SDK 内实现一次全应用生效（治理的杠杆点）；绕过 SDK 的裸用（直接 import 总线）被 lint 禁止。
- 追问钩子：为什么「绕过 SDK 禁止」这么重要？——SDK 是治理的收口点（校验/监控/清理都在里面）；一个应用裸用总线 = 它的行为对所有治理工具不可见 = 治理网破洞——收口点必须强制。

```ts
// 平台 SDK
export function createAppSdk(app, deps) {
  const cleanups = [];
  return {
    bus: wrapBus(deps.bus, app),                     // 自动命名空间
    gate: deps.gate,
    onUnmount: fn => cleanups.push(fn),              // 清理注册
    debug: attachDebug(app),
    destroy() { cleanups.forEach(f => f()); },       // 卸载统一清理
  };
}
// 子应用：sdk.onUnmount(() => timers.forEach(clearTimeout))
```
