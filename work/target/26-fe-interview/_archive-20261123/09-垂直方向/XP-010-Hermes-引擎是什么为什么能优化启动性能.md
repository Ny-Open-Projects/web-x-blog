---
title: [XP-010] Hermes 引擎是什么？为什么能优化启动性能？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-010：Hermes 引擎是什么？为什么能优化启动性能？
**答**：
- Hermes 是 Facebook 为 RN 定制的 JS 引擎，核心是 **AOT 字节码**：打包期把 JS 编译成 bytecode，运行时免了解析/AST/编译，直接执行。
- 收益：TTI（可交互时间）显著下降、内存占用降低（无 JIT 的元数据开销）、包体积可控（bc 文件比源码小）。
- 配套能力：Hermes GC 优化（分代回收适配移动端）、`RAM bundle`/inline requires 按需加载、`console` 裁剪。
- 调试支持：Hermes 支持标准调试协议，React Native DevTools 直接 attach；可用 `hgstack`/Sourcemap 还原线上堆栈。
- 注意：字节码与 Hermes 版本绑定，热更新 bundle 需要确保引擎版本一致。

```yaml
# 开启 Hermes 的配置链路
# android/gradle.properties
android:
  properties:
    hermesEnabled: true          # Android 启用 Hermes
# ios/Podfile
ios:
  podfile: |
    :hermes_enabled => true      # CocoaPods RN 启用 Hermes
# metro.config.js 产出字节码（RN 0.70+ 默认内置，此处展示命令本质）
# npx react-native bundle \
#   --platform android --dev false \
#   --entry-file index.js \
#   --bundle-output index.android.bundle \
#   --assets-dest res/
# 之后 composeHermesc 将 .bundle 编译为 .hbc 字节码：
#   hermesc -O -emit-binary index.android.bundle -out index.android.hbc
# 启动链路变化：读 .hbc 直接执行，省去 parse+compile（约等于省掉 40%-60% 启动 JS 时间）
```
