---
title: [XP-078] RN 原生模块开发全流程（iOS / Android 双端）？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-078：RN 原生模块开发全流程（iOS / Android 双端）？
**答**：
- 新架构标准流程：**写 TS Spec（单一事实源）→ codegen 生成双端接口骨架 → iOS 实现 RCTTurboModule → Android 实现 TurboModule → 注册 → JS 调用**，生成代码不手改。
- iOS 侧：Podfile 加 `install_modules_dependencies(s)`，实现类遵循 codegen 生成的 `<Spec>` 协议，方法签名必须与 Spec 一致，`.podspec` 声明 `install_modules_dependencies`。
- Android 侧：实现 `NativeDeviceSpec()`（codegen 生成于 build 目录），包名注册到 `Package` 的 `getTurboModules`；注意主线程约束与 `@ReactModule`。
- 通信模型：方法调用经 JSI 直连（无 JSON 序列化），支持同步返回基础类型；异步用 Promise；主动通知 JS 用 `EventEmitter`（新架构下自建 `RCTEventEmitter` / `DeviceEventManagerModule`）。
- 线程纪律：耗时分派到自己的 methodQueue/executor；回调必须回到 JS 线程由框架保证，原生侧不要在回调里做重活。双端行为差异（权限弹窗时机等）在 Spec 注释与单测（mock 桥）里固化。

```typescript
// specs/NativeDeviceSpec.ts —— codegen 的单一事实源，双端实现以此为准
import type { TurboModule } from 'react-native';
import { TurboModuleRegistry } from 'react-native';

export interface Spec extends TurboModule {
  // 同步方法：JSI 直连，仅限轻量属性读取（不跨线程、无阻塞 IO）
  getDeviceId(): string;
  // 异步：Promise，双端 resolve/reject 线程由框架处理
  requestPermission(scope: string): Promise<boolean>;
  // 常量：codegen 生成 getConstants()，初始化时一次取回
  readonly deviceTier: string;
  // 事件约定：原生 emit，JS addListener
  addListener(eventName: string): void;
  removeListeners(count: number): void;
}
export default TurboModuleRegistry.get<Spec>('Device');

// iOS（ObjC++，Device.mm）：Podspec 中 install_modules_dependencies(s)
//   @interface Device () <NativeDeviceSpecBase>  // 协议由 codegen 生成
//   RCT_EXPORT_MODULE()
//   - (NSString *)getDeviceId { return _deviceId; }         // 签名与 Spec 严格一致
//   - (void)requestPermission:(NSString *)scope
//                    resolve:(RCTPromiseResolveBlock)resolve
//                     reject:(RCTPromiseRejectBlock)reject { ... 主线程弹窗 ... }
// Android（Kotlin，DeviceModule.kt）：
//   class DeviceModule(reactContext: ReactApplicationContext) :
//       NativeDeviceSpec(reactContext) {                  // 继承 codegen 生成基类
//     override fun getName() = NAME
//     override fun requestPermission(scope: String, promise: Promise) {
//       UiThreadUtil.runOnUiThread { /* 弹系统授权框 */ }   // UI 操作必须主线程
//     }
//   }
//   companion object { const val NAME = "Device" }        // 与 Spec 的 'Device' 对齐
```
