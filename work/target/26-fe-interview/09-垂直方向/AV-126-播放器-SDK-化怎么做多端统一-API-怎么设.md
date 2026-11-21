---
title: [AV-126] 播放器 SDK 化怎么做？多端统一 API 怎么设计？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-126：播放器 SDK 化怎么做？多端统一 API 怎么设计？（高频）
**答**：
- 问题：Web、小程序、RN/Flutter 三套底层 API，业务层写三遍；SDK 化 = 统一行为协议，端上各自实现 adapter。
- 统一接口三件套：生命周期（create/load/play/destroy）、统一状态机枚举、统一事件总线（事件名与载荷结构一致）。
- 分层设计：core（状态机/指标/错误码）→ adapter（hls.js/flv.js/小程序原生）→ 业务插件（弹幕/字幕/广告）。
- 指标口径统一进 SDK：首帧、卡顿、错误码全端一致，监控平台才能横向对比（关联 AV-131/132）。
- 插件机制：SDK 只管生命周期与事件，功能以插件注册，避免上帝类；新业务品类 = 新插件组合。

```typescript
// 统一播放器协议：各端 adapter 实现同一接口
type PlayerState = 'idle' | 'loading' | 'playing' | 'paused' | 'stalled' | 'error';
interface UnifiedPlayer {
  load(src: { url: string; protocol: 'hls' | 'flv' | 'native' }): Promise<void>;
  play(): Promise<void>; pause(): void; destroy(): void;
  readonly state: PlayerState;
  on(ev: string, cb: (p: any) => void): void;
  setRate(rate: number): void; setQuality(level: number): void;
  readonly metrics: { firstFrameMs?: number; stallCount: number; playedSec: number };
}
type AdapterFactory = (el: unknown, cfg: SdkConfig) => UnifiedPlayer; // web 传 video 元素 小程序传 context
const registry = new Map<string, AdapterFactory>([
  ['web-hls', webHlsAdapter], ['web-flv', webFlvAdapter], ['mp-live', miniprogramAdapter],
]);
export function createPlayer(platform: string, el: unknown, cfg: SdkConfig): UnifiedPlayer {
  const factory = registry.get(platform) ?? webHlsAdapter;
  return withPluginHooks(factory(el, cfg));   // 注入插件生命周期钩子
}
// core 保证：无论底层是 hls.js 还是 live-player，业务拿到的 state 枚举与 firstFrameMs 口径完全一致
```

## 十五、性能与 QoE 深化（AV-127 ~ AV-132）
