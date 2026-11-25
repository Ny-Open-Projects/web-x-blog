---
title: [XP-187] Electron 与原生模块：Native addon 集成
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-187：Electron 与原生模块：Native addon 集成

**答**：
- Native addon（C++/Rust NAPI）：性能关键路径（加密/图像处理）用原生模块——需按 Electron ABI 版本编译（electron-rebuild）。
- 分发：预编译多平台二进制（mac/win/linux × x64/arm64）或用户本地编译（慢）；prebuild-install 思路。
- 沙箱限制：sandbox: true 下渲染进程不能用 native addon——放主进程或 utility process。

```javascript
// native module 加载（主进程）
let nativeCrypto;
try {
  nativeCrypto = require('../build/Release/crypto_addon');       // 预编译产物
} catch {
  nativeCrypto = require('crypto');                               // 降级：纯 JS 实现
}
// electron-rebuild：针对 Electron ABI 重编译（Node ABI ≠ Electron ABI）
// npx electron-rebuild -f -w crypto_addon
// prebuild 分发：CI 构建多平台二进制 → npm install 时下载对应平台产物（免本地编译）
// 沙箱模式：native addon 只能在主进程/utility process 使用——渲染进程无法 require
```
