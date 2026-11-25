---
title: [XP-168] 跨端容器与 Flutter 混合：Flutter 模块嵌入容器
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-168：跨端容器与 Flutter 混合：Flutter 模块嵌入容器

**答**：
- Flutter 模块嵌入：Add-to-App——Flutter Engine 嵌入自研容器，Flutter 渲染独立Surface（与 Native View 混合）。
- 通信：Flutter 与 JS 桥（MethodChannel ↔ JSI 双向桥接）——Flutter 调 JS 业务、JS 调 Flutter UI。
- 成本：Flutter Engine 内存 ~30MB——单页面嵌入不划算（多页面共享 Engine 才值）。

```javascript
// JS ↔ Flutter 双向桥
class FlutterBridge {
  constructor(channel) { this.channel = channel; }             // MethodChannel
  call(method, args) {                                         // JS → Flutter
    return new Promise((res) => this.channel.invokeMethod(method, args, res));
  }
  onEvent(event, cb) {                                         // Flutter → JS
    this.channel.setMethodCallHandler((call) => {
      if (call.method === event) cb(call.args);
    });
  }
}
// 架构：容器 JS 逻辑层 → FlutterBridge → Flutter Engine（渲染 Surface）
// 多页面共享：一个 Engine 多个 FlutterViewController（页面级路由）——省内存
```
