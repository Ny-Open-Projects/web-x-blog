---
title: [MP-210] Taro 的自定义渲染器架构（渲染到 Flutter/鸿蒙等）？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-210：Taro 自定义渲染器架构？
**答**：
- Taro 抽象出「渲染引擎接口」（类似 React 自定义 renderer）：树同步、事件注册、setData 实现——新端只需实现该接口。
- 鸿蒙端：逻辑层跑 ArkTS/JS，渲染层接 ArkUI 声明式组件——同一 Taro 组件树映射。
- 价值：React/Vue 心智跨端复用到底（Web/H5/小程序/快应用/RN）。
- 边界：端能力差异大的 API（支付/生物识别）仍需 per-platform 实现；自定义渲染器维护成本 = 端数量。
- 面试表达：Taro 的本质是「React/Vue 的多端 reconciler + 能力垫片」。
