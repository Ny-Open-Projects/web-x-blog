---
title: [XP-212] Flutter 与原生通信：Platform Channel 与 FFI
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 笔试题, 27]
type: 笔试题
---

## XP-212：Flutter 与原生通信：Platform Channel 与 FFI

**答**：
- 题目：Flutter 平台通信——MethodChannel（方法调用）/ EventChannel（事件流）/ FFI（直接调 C 库）。实现一个 MethodChannel 调用。
- 思路：MethodChannel（名称唯一 + 编解码 StandardMethodCodec）→ Native handler 响应；EventChannel（Stream 流式推送）；FFI（Dart FFI 直接调 C——性能敏感）。
- 评分点：三种通道选型；编解码成本；FFI 场景。

```javascript
// Dart 侧 MethodChannel
const channel = MethodChannel('com.example/battery');
Future<int> getBatteryLevel() async {
  return await channel.invokeMethod('getBatteryLevel');        // Native 响应
}
// Native 侧（Android Kotlin）
channel.setMethodCallHandler { call, result ->
  when (call.method) {
    "getBatteryLevel" -> result.success(getBatteryLevel())
    else -> result.notImplemented()
  }
}
// EventChannel：流式推送（传感器/位置）
const eventChannel = EventChannel('com.example/sensor');
eventChannel.receiveBroadcastStream().listen((data) => updateUI(data));
// FFI：性能敏感（图像处理）直接调 C
final DynamicLibrary lib = DynamicLibrary.open('libimage.so');
final int Function(Pointer<Uint8>, int) sum = lib.lookupFunction<...>('sum_pixels');
```
