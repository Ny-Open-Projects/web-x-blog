---
title: [XP-015] RN 如何与原生模块通信？Promise 桥的完整链路是什么？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-015：RN 如何与原生模块通信？Promise 桥的完整链路是什么？
**答**：
- 新架构路径：TS 规格（Spec）→ Codegen 生成胶水 → 原生实现 `Spec`，JS 经 TurboModuleRegistry 调用。
- 回调形态三种：**Promise**（一次异步结果）、**Callback**（可多次触发，如传感器）、**Event Emitter**（原生主动广播，需原生 emit + JS 订阅）。
- Promise 桥链路：JS 调用 → JSI 传参 → 原生线程执行 → resolve/reject 携带结果回传 → JS 侧 promise settle；新架构无需 JSON 序列化。
- 踩坑点：原生必须保证 promise 只 settle 一次（二次 resolve 崩溃/告警）；长任务要在原生侧切线程；常量用 `constantsProvider` 导出。

```typescript
// JS 侧：规格化调用 + 三种通信形态
import { NativeEventEmitter } from 'react-native';
import NativeScanner from './specs/NativeScanner'; // Codegen 产物，见 XP-011

// 1) Promise：一次性异步结果
async function scanOnce(): Promise<{ text: string; format: string }> {
  try {
    return await NativeScanner.scanOnce({ timeoutMs: 5000 });
  } catch (e: any) {
    if (e.code === 'PERMISSION_DENIED') throw new Error('请开启相机权限');
    throw e;
  }
}

// 2) EventEmitter：原生持续广播（如扫码连续回调）
const emitter = new NativeEventEmitter(NativeScanner as any);
const sub = emitter.addListener('onBarcode', (payload: { text: string }) => {
  console.log('barcode', payload.text);
});
// sub.remove() 释放

// 3) 原生侧（示意 ObjC）Promise 规约：
// RCTPromiseResolveBlock resolve; RCTPromiseRejectBlock reject;
// 成功 resolve(@{...})；失败 reject(@"PERMISSION_DENIED", msg, nil)；且只允许调用一次
```
