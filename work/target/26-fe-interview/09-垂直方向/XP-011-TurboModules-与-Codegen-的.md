---
title: [XP-011] TurboModules 与 Codegen 的作用和协作方式？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-011：TurboModules 与 Codegen 的作用和协作方式？
**答**：
- **Codegen**：编译期扫描 `Native<Name>.ts` 规格文件（Typed API），生成 Java/ObjC++ 胶水代码与 C++ 结构体，把"运行时反射查方法名"变成"编译期符号绑定"。
- **TurboModules**：基于 JSI 的模块系统，**懒加载**——JS 首次 require 时才初始化原生模块（旧版启动即全量注册），并允许原生模块做异步初始化。
- 协作流程：写 TS 规格 → codegen 生成 `Spec` → 原生实现 `Spec` 接口 → JS 通过 TurboModuleRegistry 获取。
- 类型契约带来两大收益：JS 与原生接口类型安全（编译期报错）、跨平台参数转换代码自动生成。
- 旧 NativeModules 在新架构下经由 interop layer 兼容运行，但拿不到同步调用等新能力。

```typescript
// specs/NativeLocation.ts —— Codegen 规格文件（新架构模板）
import type { TurboModule } from 'react-native';
import { TurboModuleRegistry } from 'react-native';

export interface Spec extends TurboModule {
  // Codegen 据此生成 Android(Java/Kotlin) 与 iOS(ObjC++) 的接口与参数转换代码
  getCurrentPosition(promise: Promise<{ lat: number; lng: number }>): void;
  startHeadingUpdate(callback: (degree: number) => void): void; // 函数引用可传，旧 Bridge 做不到
  readonly isSupported: boolean;                                 // 常量也走编译期契约
}

export default TurboModuleRegistry.getEnforcing<Spec>('Location');

// 原生侧（示意 Android）：
// class LocationModule : NativeLocationSpec(this.reactContext) {
//   override fun getCurrentPosition(promise: Promise) { ... }  // 实现 Codegen 产物接口
// }
// package.json 配置：codegenConfig { "name": "RNLocationSpec", "type": "modules", "jsSrcsDir": "specs" }
```
