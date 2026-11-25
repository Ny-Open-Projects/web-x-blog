---
title: [XP-070] 设计一个原生模块桥接层，RN 与 Flutter 两套实现的差异对比？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-070：设计一个原生模块桥接层，RN 与 Flutter 两套实现的差异对比？
**答**：
- 同一契约两种实现：接口定义（TS Spec / Dart 抽象类）→ 平台胶水（Codegen TurboModule / MethodChannel handler）→ 原生实现共享（同一份原生代码，两套薄绑定层）。
- 关键差异：**调用模型**——RN 新架构经 JSI 可同步、传参走 JSI Value 直转；Flutter MethodChannel 永远异步、参数经 StandardMessageCodec 二进制编解码（非 JSON，但仍有序列化成本）。
- 事件流：RN 用 EventEmitter（原生 emit）；Flutter 用 EventChannel（StreamHandler + EventSink），语义等价。
- 线程模型：RN 原生模块方法默认非主线程；Flutter 平台通道 handler 默认在平台主线程，重活要自己 `compute`/ isolate 或原生侧切线程。
- 工程结论：契约与原生核心代码全端共享，绑定层薄壳化；性能敏感高频调用优先 RN/JSI 或 Flutter 的 FFI/texture 方案。

```typescript
// RN 侧：specs/NativeBattery.ts（Codegen 契约，见 XP-011）
import type { TurboModule } from 'react-native';
import { TurboModuleRegistry } from 'react-native';
export interface Spec extends TurboModule {
  getLevel(): number;                                        // JSI 同步直达
  startMonitor(cb: (pct: number) => void): void;             // 函数引用直达 C++
}
export default TurboModuleRegistry.getEnforcing<Spec>('Battery');
```

```dart
// Flutter 侧：同一契约经 MethodChannel（异步 + codec 编解码）
class BatteryBridge {
  static const _ch = MethodChannel('app/battery');
  static const _events = EventChannel('app/battery/events');
  Future<int> getLevel() async => _ch.invokeMethod<int>('getLevel') as int;   // 永远异步
  Stream<int> monitor() => _events.receiveBroadcastStream().cast<int>();      // 对应 RN EventEmitter
}
// Android 原生（共享实现，两套绑定）：
// override fun onMethodCall(call: MethodCall, result: MethodChannel.Result) {
//   when (call.method) { "getLevel" -> result.success(BatteryCore.level()) } }  // Flutter：主线程回调
// RN 侧实现 BatteryModule : NativeBatterySpec {
//   override fun getLevel() = BatteryCore.level()          // JSI 同步；默认在 native 线程池
//   override fun startMonitor(cb: Callback) { BatteryCore.monitor { cb.invoke(it) } }
// }
// 差异总结：RN=同步直调+函数引用；Flutter=异步消息+codec 序列化+主线程回调（重活自切线程）
```
