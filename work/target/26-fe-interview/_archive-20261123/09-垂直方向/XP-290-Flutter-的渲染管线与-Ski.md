---
title: [XP-290] Flutter 的渲染管线与 Skia Impeller
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-290：Flutter 的渲染管线与 Skia Impeller

**答**：
- Flutter 自绘（Skia/Impeller）不依赖系统控件——一致性高但首帧要编译着色器（jank 来源）。
- Impeller：预编译着色器（iOS 3.10+），消除首次动画的 shader 编译卡顿。
- 优化：warm-up 阶段预跑动画、避免 build 中做重计算（const widgets）。

```javascript
// Flutter 首帧预热概念
// 1. Impeller 开启（ios/Runner Info.plist 无需配置，默认 3.10+）
// 2. 预热动画：
// void warmUpShaders() {
//   final controller = AnimationController(vsync: tester);
//   // 播放核心动画一帧，触发着色器编译缓存
// }
// 3. const widget 减少 rebuild：
// const Text('static title')  // 编译期常量，跳过 rebuild
```
