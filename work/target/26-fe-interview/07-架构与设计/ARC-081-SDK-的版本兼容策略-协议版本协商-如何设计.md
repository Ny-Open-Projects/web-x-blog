---
title: [ARC-081] SDK 的版本兼容策略（协议版本协商）如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-081：SDK 的版本兼容策略（协议版本协商）如何设计？
**答**：
- 三层兼容：传输协议版本（握手协商）、API 语义版本（semver）、能力探测（feature detect 而非 UA 判断）。
- 握手机制：init 时上报 SDK 版本与服务端约定区间，服务端返回该版本可用的能力集与降级开关；不兼容时服务端可下发"强制升级提示"。
- SDK 内部：旧接口保留 deprecated 包装一个 major 周期；关键协议字段只增不删（向后兼容扩展）。

```typescript
// SDK 握手协商：版本 + 能力集
interface HandshakeRequest  { sdk: 'corp-track'; version: string; capabilities: string[]; }
interface HandshakeResponse {
  ok: boolean;
  minVersion: string;                    // 服务端允许的最低版本
  enabledFeatures: string[];             // 下发可用能力：['beacon','apm','user-profile']
  configDelta?: Record<string, unknown>; // 远程配置覆盖
  forceUpgrade?: { message: string; url: string };
}

async function initSdk(userConfig: SdkConfig) {
  const hs = await post<HandshakeResponse>('/sdk/handshake', {
    sdk: 'corp-track', version: SDK_VERSION,
    capabilities: detectCapabilities(),  // ['sendBeacon','PerformanceObserver','IndexedDB']
  });
  if (hs.forceUpgrade) return promptUpgrade(hs.forceUpgrade);
  if (semverLt(SDK_VERSION, hs.minVersion)) return;        // 过旧版本自动停用，防脏数据
  const features = new Set(hs.enabledFeatures);
  features.has('beacon') ? useBeaconUploader() : useFetchUploader();  // 按协商结果装配
  applyConfig({ ...userConfig, ...hs.configDelta });
}
// 协议演进纪律：事件 schema 只加字段；删字段走 v2 事件名并行一个版本
```
