---
title: [XP-021] Skia 与 Impeller 的差异？Impeller 解决了什么问题？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-021：Skia 与 Impeller 的差异？Impeller 解决了什么问题？
**答**：
- Skia：通用 2D 渲染库，GPU 管线对象（shader）在**运行时按需编译**——首次出现复杂路径/特效时编译着色器造成毫秒级卡顿（jank），早期靠 SkSL 预热缓解但难覆盖全。
- Impeller：Flutter 自研渲染引擎，**构建期预编译所有着色器**（Metal/早期 Vulkan），运行时零编译卡顿；管线状态对象PSO 提前烘焙。
- 其他收益：更好的调试能力（可捕获每帧指令）、简化渲染栈、去掉 SkSL 编译层。
- 现状：iOS 默认启用（Metal），Android 逐步默认（Vulkan/回退 GL）；Skia 仍是回退与 CanvasKit（Flutter Web）底座。
- 顺带对比 Flutter Web 渲染器：canvaskit（Skia wasm）vs html renderer（见 XP-025）。

```yaml
# impeller 开关与验证（Flutter 3.10+）
ios:
  Runner:
    Info.plist:
      FLTEnableImpeller: true        # iOS 默认开启，显式声明便于回滚
android:
  gradle:
    app:
      build.gradle: |
        android {
          defaultConfig {
            // Flutter 3.16+ Android 逐步默认启用；回退开关
            // manifestPlaceholders += [io.flutter.embedding.android.Impeller: "true"]
          }
        }
# 验证着色器编译 jank 是否消除：
#   flutter run --profile → DevTools Performance → Raster 线程
#   Skia：首次进入复杂页面出现长 raster 块（shader 编译）
#   Impeller：raster 时间稳定，无首现尖刺
# 预热方案（Skia 时代）：flutter build 产物含 SkSL warmup：
#   flutter run --cache-sksl --profile → 交互采集 → flutter build --bundle-sksl-path flutter_sksl.json
```
