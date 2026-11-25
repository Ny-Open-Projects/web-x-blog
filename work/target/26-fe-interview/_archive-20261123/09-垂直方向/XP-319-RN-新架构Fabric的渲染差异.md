---
title: [XP-319] RN 新架构（Fabric）的渲染差异
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-319：RN 新架构（Fabric）的渲染差异

**答**：
- Fabric：同步渲染/优先级调度（与 React 18 并发一致）——交互优先级可中断渲染。
- 收益：列表/复杂界面丢帧减少； bridge 减少依赖（JSI 直调）。
- 迁移：老模块（原生 UI 组件）需适配 Fabric——灰度切换观察崩溃率。

```javascript
// Fabric 迁移检查
function fabricReady(module) {
  return {
    jsi: module.usesLegacyBridge ? '需改造 JSI' : 'ok',
    nativeComponent: module.paperProps ? '适配 Fabric spec' : 'ok',
    concurrent: module.usesLegacyLifecycle ? '替换 UNSAFE_ 生命周期' : 'ok',
  };
}
```
