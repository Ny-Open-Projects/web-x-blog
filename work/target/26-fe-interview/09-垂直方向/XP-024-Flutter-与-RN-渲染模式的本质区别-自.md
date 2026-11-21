---
title: [XP-024] Flutter 与 RN 渲染模式的本质区别（自绘 vs 原生映射）？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-024：Flutter 与 RN 渲染模式的本质区别（自绘 vs 原生映射）？
**答**：
- **Flutter 自绘**：引擎持有完整渲染管线，UI 是像素输出，与平台控件无关——一致性最强、动画自由度高；代价是无法直接用系统控件、无障碍/输入法等需要引擎桥接。
- **RN 原生映射**：JS 描述的 View 树映射到系统真实控件（UITextView/TextView），天然获得系统无障碍、字体渲染、辅助能力；代价是**平台差异暴露**（两端样式/行为不完全一致）与映射开销。
- 布局引擎也不同：Flutter Yoga（C++ 常驻 ShadowTree）；RN 同样用 Yoga 但树的位置不同（Fabric 在 C++、旧版在 JS 侧）。
- 推论差异：Flutter 的热更新受限（Dart AOT 产物是引擎字节码）；RN 换 JS bundle 即可热更。
- 追问"谁性能高"：一般性结论 Flutter 帧稳定更优（无桥接、管线可控），RN 新架构后常规页面差距已缩小，列表与复杂动画 Flutter 仍占优。

```text
维度            Flutter 自绘                          RN 原生映射
UI 本体         Skia/Impeller 画布上的像素             系统 UIText 等 真实控件
一致性          三端像素级一致                          依赖平台控件 需逐项适配
平台能力接入    引擎桥接（无障碍 输入法 需适配）        原生天然具备
布局引擎        Yoga 常驻 C++ ShadowTree               Yoga Fabric C++ ShadowTree 新架构
动画上限        引擎内完成 可到每帧像素级              worklet 下沉 UI 线程后接近 原生控件动画受限
热更新          Dart AOT 受限                          替换 JS bundle 即可
包体积          引擎自带 基础包大                      复用系统控件 基础包小
典型瓶颈        raster 线程着色器 build 重建           JS 线程长任务 挂载吞吐
```
