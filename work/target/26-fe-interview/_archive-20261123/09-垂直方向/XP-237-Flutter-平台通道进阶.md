---
title: [XP-237] Flutter 平台通道进阶：Pigeon 类型安全通信
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-237：Flutter 平台通道进阶：Pigeon 类型安全通信

**答**：
- Pigeon：Flutter 类型安全平台通道——Dart/Kotlin/Swift 接口定义 → 代码生成（类型安全，免手写 MethodChannel 编解码）。
- 收益：编译期类型检查（方法签名/参数类型一致）；免手写编解码（StandardMethodCodec 手写易错）。
- 对比 MethodChannel：手写灵活但易错（类型不匹配运行时才炸）；Pigeon 编译期保障。

```javascript
// pigeons/battery.dart（接口定义）
import 'package:pigeon/pigeon.dart';
@HostApi()
abstract class BatteryApi {
  int getBatteryLevel();
}
@FlutterApi()
abstract class BatteryEventApi {
  void onLevelChanged(int level);
}
// 生成：flutter pub run pigeon --input pigeons/battery.dart
// → Dart 接口 + Kotlin/Swift 实现 stub——类型安全（编译期检查）
// 对比 MethodChannel：手写 invokeMethod('getBatteryLevel') 返回 dynamic——类型错运行时才炸
```
