---
title: [XP-008] JSI 的原理是什么？它如何实现 JS 与原生的直接调用？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 笔试题, 27]
type: 笔试题
---

## XP-008：JSI 的原理是什么？它如何实现 JS 与原生的直接调用？
**答**：
- JSI 是一层**纯 C++ 的抽象接口**（不依赖 JS 引擎实现），向上对接 JS 引擎（Hermes/JSC/V8），向下暴露 HostObject/HostFunction 概念。
- 原生对象以 `HostObject` 形式注册进 JS 全局，JS 侧拿到的是一个**代理对象**，属性访问/方法调用直接触发 C++ 虚函数调用。
- 关键收益：① 同步调用；② 参数无需 JSON 序列化（JSI Value 直接转换）；③ 可以传函数引用（Callback 也走 HostFunction）；④ 与引擎解耦，换引擎不改业务。
- 旧 Bridge 与 JSI 对比：Bridge 是"信箱异步传 JSON"，JSI 是"直接拿着引用调方法"。
- JSI 也是 RN 与 C++ 生态（Yoga、Fabric、TurboModules）统一的基石。

```typescript
// JSI 语义示意（C++ 侧等价逻辑以注释说明）
// C++ 侧：class JSI_DEVICE : public HostObject {
//   Value get(Runtime&, const PropNameID& name) override {
//     if (name.utf8(rt) == "vibrate") return Function::createFromHostFunction(...);
//   }
// } 并注入 global.__DeviceModule

// JS 侧：global 上直接拿到原生 HostObject 代理
declare const __DeviceModule: { vibrate: (ms: number) => void };

__DeviceModule.vibrate(30); // 同步直达 C++，参数 int 由 JSI Value 直接转换
// 对比旧 Bridge：
// NativeModules.Device.vibrate(30) → 入队 → JSON 化 → native 线程反序列化执行 → 无法同步

// 自定义 JSI 模块的注册（新架构下由 Codegen + Autolinking 自动完成）
import NativeVibrate from './specs/NativeVibrate'; // Codegen 生成的规格化封装
NativeVibrate.vibrate(30);
```
