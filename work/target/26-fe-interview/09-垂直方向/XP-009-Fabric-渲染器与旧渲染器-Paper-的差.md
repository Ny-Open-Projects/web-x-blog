---
title: [XP-009] Fabric 渲染器与旧渲染器（Paper）的差异是什么？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-009：Fabric 渲染器与旧渲染器（Paper）的差异是什么？
**答**：
- **C++ ShadowTree**：布局树移到 C++ 层（旧版在 JS 线程算 Yoga），与 JS 线程解耦，布局不再阻塞 JS。
- **同步可中断渲染**：React 18 并发特性（Transition、Suspense）可支持，渲染阶段可中断重排；旧版是"整树 commit 异步通知"。
- **挂载机制**：Fabric 由 C++ Mounting 阶段统一计算 Diff 后原子提交到平台视图；旧版由 UIManager（Java/ObjC）增量处理，容易出现中间态闪烁。
- **代码生成**：组件规格（Props/Events）由 Codegen 生成，JS 与原生强契约，属性解析在编译期完成。
- 淘汰了 LegacyComponents，新组件必须提供 Fabric 实现（interop layer 兼容旧三方）。

```jsx
// Fabric 组件：Props 由 Codegen 规范约束，编译期生成解析代码
import React from 'react';
import { View, Text, Pressable } from 'react-native';

// specs/NativeBadge.ts 中 Codegen 规格：
// export interface Spec extends TurboModule { ... }
// Fabric 视图组件的 props 必须与 Codegen 生成的类型一一对应
export function Badge({ label, tint, onPress }) {
  return (
    <Pressable onPress={onPress} accessibilityRole="button">
      {/* Fabric 下 View 布局由 C++ ShadowTree + Yoga 完成，不占 JS 线程 */}
      <View style={{ backgroundColor: tint, borderRadius: 8, padding: 4 }}>
        <Text style={{ color: '#fff', fontSize: 12 }}>{label}</Text>
      </View>
    </Pressable>
  );
}
// 原生侧（Kotlin/ObjC）需实现 Fabric 组件注册：
// BadgeViewManager : SimpleViewManager<BadgeView> + @ReactProp(label)（新架构经 Codegen 绑定）
```
