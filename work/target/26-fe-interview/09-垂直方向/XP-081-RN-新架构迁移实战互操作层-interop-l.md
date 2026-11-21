---
title: [XP-081] RN 新架构迁移实战？互操作层（interop layer）怎么用？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-081：RN 新架构迁移实战？互操作层（interop layer）怎么用？
**答**：
- 开启开关：`gradle.properties` 设 `newArchEnabled=true`，iOS Podfile 设 `ENV['RCT_NEW_ARCH_ENABLED'] = '1'`；先用互操作层让存量代码"零修改"跑在新架构上。
- **互操作层**：旧 Native Module 经 `TurboModuleInterop`（JS 侧 API 不变，底层走 JSI）、旧 Native Component 经 `RCTComponentViewFactory` 兼容包装被 Fabric 挂载——先得新架构收益（同步布局、批量渲染），再逐步重写。
- 迁移顺序策略：先基础库（手势/导航/WebView）→ 自研组件 → 业务模块；每步跑双轨回归（旧架构基线 vs 新架构），指标对齐（启动、列表、动画帧率）。
- 依赖矩阵盘点：`npx react-native upgrade` 后检查三方库新架构兼容声明（react-native-screens/gesture-handler/reanimated 均 required），不兼容库先找替代或锁版本隔离。
- 回滚与风控：保留旧架构构建变体（flavor/scheme）做应急回退；灰度（XP-083）观察崩溃率与 JS 异常率达标后放量；迁移期禁止同时大改业务逻辑。

```text
// android/gradle.properties —— 开启新架构 + 互操作层
newArchEnabled=true
hermesEnabled=true

// ios/Podfile —— iOS 侧同义开关
ENV['RCT_NEW_ARCH_ENABLED'] = '1'
// 旧三方 Native Module 在新架构下经 interop 自动包装，JS 调用 API 完全不变
// TurboModuleProvider 发现模块未实现 TurboSpec 时走 TurboModuleInterop 兜底

迁移执行清单（按序）：
  1 依赖盘点     梳理三方库新架构兼容矩阵，锁定版本，无替代的封装隔离
  2 开关开启     双端打开 newArchEnabled，互操作层承接存量模块与组件
  3 双轨回归     启动耗时 列表帧率 动画 崩溃率 四指标与旧架构基线对比
  4 基础库替换   手势 导航 图像库逐个换成 Fabric/TurboModule 原生支持版本
  5 业务迁移     高频 Native Module 改写 Spec（XP-078 流程），codegen 验证
  6 灰度放量     XP-083 流程，JS 异常率 崩溃率达标后逐桶放量，保留回退变体
```
