---
title: [XP-022] Flutter 与原生的通信（Platform Channel）原理？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-022：Flutter 与原生的通信（Platform Channel）原理？
**答**：
- 核心机制：Dart 与原生（Kotlin/ObjC）之间通过 **BinaryMessenger** 传二进制消息，`MethodCodec`（StandardMessageCodec）编解码——数据按类型表（int/double/String/List/Map/Uint8List）编码，**不是 JSON**。
- 四种通道：MethodChannel（方法调用+返回）、BasicMessageChannel（双向消息流）、EventChannel（原生持续推送流）、以及 Pigeon（类型安全的代码生成方案，推荐）。
- 通道调用是**异步**的（跨线程消息），无泛型校验，参数只支持 codec 类型表内的类型，自定义对象需转 Map。
- 性能注意：高频大数据（如实时帧）应降频聚合或直接走 texture/FFI 共享内存，不走 channel 序列化。
- 与 RN 的 JSI 对比：channel 是异步消息、JSI 是同步直接调用，这是两套架构的本质区别之一。

```dart
// Dart 侧：MethodChannel 双向通信 + EventChannel 流
static const _method = MethodChannel('app/pay');
static const _events = EventChannel('app/pay/events');

Future<Map<String, dynamic>> requestPay(Order o) async {
  // 参数/返回都经 StandardMessageCodec 编码为二进制，非 JSON 字符串
  final result = await _method.invokeMethod<Map<Object?, Object?>>(
    'requestPay',
    {'orderId': o.id, 'amountFen': o.amountFen, 'channel': o.channel},
  );
  return result?.cast<String, dynamic>() ?? {};
}

Stream<PayState> payStateStream() => _events.receiveBroadcastStream().map(
      (e) => PayState.values.byName(e as String),
    );

// Android 侧（示意 Kotlin，放在 FlutterActivity 中）：
// EventChannel(flutterEngine.dartExecutor.binaryMessenger, "app/pay/events")
//   .setStreamHandler(object : EventChannel.StreamHandler {
//     override fun onListen(args: Any?, events: EventChannel.EventSink?) { payEmitter = events }
//     override fun onCancel(args: Any?) { payEmitter = null }
//   })
// MethodChannel(...).setMethodCallHandler { call, result ->
//   when (call.method) { "requestPay" -> startPay(call.arguments(), result) }
// } // result.success(map) 只能调用一次，与 RN Promise 规约一致
```
