---
title: [XP-288] RN 的 Hermes 引擎与启动优化
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-288：RN 的 Hermes 引擎与启动优化

**答**：
- Hermes：字节码预编译（AOT），启动省去 JS 解析（首帧 -30%）；内存占用更低。
- 优化：启用 Hermes + 字节码内嵌 + 延迟 require（懒加载模块）。
- 度量：RN TTI（可交互时间）分版本对比，Hermes 开启前后对照。

```javascript
// RN 懒加载模块
// 反模式：顶部 import 重模块
// 正解：
const HeavyChart = React.lazy(() => import('./HeavyChart'));
// Hermes 配置（android/app/build.gradle）：
// def hermesEnabled = true
// bundle 命令：--bundle-output index.android.bundle --hermes-parse
```
