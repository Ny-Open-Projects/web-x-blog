---
title: [XP-020] Dart 的 isolate 模型？与 JS 单线程模型对比？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-020：Dart 的 isolate 模型？与 JS 单线程模型对比？
**答**：
- Dart 默认 main isolate 单线程事件循环（与 JS 类似），但可以**真正并行**：每个 isolate 有独立的堆与事件循环，互不共享内存，靠消息传递（SendPort）通信。
- JS 的 Web Worker 也是多线程但浏览器环境受限；RN 中 JS 是单线程，CPU 密集任务会阻塞渲染指令派发。
- Flutter 中典型用法：`compute()` 把 JSON 解析/图片处理丢到后台 isolate，避免 UI 线程掉帧；isolate 间传大对象可走 `TransferableTypedData` 免拷贝。
- 与 JS 对比总结：JS 用"异步 IO + 切片"模拟并发，Dart 用"真并行 isolate + 消息传递"；两者 UI 线程都禁止长任务。
- 新特性：isolate groups（共享大部分堆、低开销 spawn）缓解消息拷贝成本。

```dart
// 后台 isolate 解析大 JSON，避免 UI 线程卡顿
import 'package:flutter/foundation.dart';

Future<List<Post>> parseInIsolate(String raw) async {
  // compute：短平快的一次性任务（内部 spawn isolate 并传参）
  final posts = await compute(_decode, raw);
  return posts.map(Post.fromJson).toList();
}

List<dynamic> _decode(String raw) => jsonDecode(raw) as List<dynamic>;

// 长驻任务：双工通信
Future<void> counterIsolate(SendPort mainPort) async {
  final port = ReceivePort();
  mainPort.send(port.sendPort);
  await for (final msg in port) {
    if (msg == 'tick') mainPort.send(DateTime.now().millisecondsSinceEpoch);
  }
}
// JS/RN 对比：同样任务只能 requestIdleCallback 切片或 Web Worker（浏览器环境才有）
// Dart：真并行执行，8 核机器可同时跑 8 个 isolate
```
