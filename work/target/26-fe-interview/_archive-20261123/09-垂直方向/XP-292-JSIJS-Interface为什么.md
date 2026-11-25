---
title: [XP-292] JSI（JS Interface）为什么比传统 Bridge 快
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-292：JSI（JS Interface）为什么比传统 Bridge 快

**答**：
- 传统 Bridge：JSON 序列化 + 异步线程队列——延迟高且无法同步返回。
- JSI：C++ 层直接持有 JS 对象引用（HostObject），同步调用、无序列化——性能 ×10。
- 应用：高性能模块（数据库/动画驱动/蓝牙）用 JSI 原生实现。

```javascript
// JSI HostObject 概念
// C++ 侧：
// class DbHostObject : public facebook::jsi::HostObject {
//   jsi::Value get(jsi::Runtime&, const jsi::PropNameID& name) override {
//     if (name.utf8(rt) == "query")
//       return jsi::Function::createFromHostFunction(rt, ..., querySync);
//   }
// };
// JS 侧直接同步调用：
// const rows = NativeDb.querySync(sql);   // 无 Promise 无序列化
```
