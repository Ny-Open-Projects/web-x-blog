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

## 追问（补充）

**追问**：

1. 统一状态机里 stalled 与 loading 的边界怎么定，定错会怎样 → 播放中连续 3s 无 progress 才算 stalled，切源和 seek 属于 loading；混用会让卡顿率指标虚高甚至翻倍。
2. 各端错误码语义不一致，监控怎么横向对比 → SDK 内做错误码归一表（网络、解码、鉴权、资源四类），原始码放 detail 字段保留排障信息，指标层只认归一码。
3. SDK 升级后老业务插件不兼容怎么办 → 插件与 core 之间只依赖稳定事件协议并做版本协商，core 大版本升级提供兼容 shim 撑一个版本周期再删。
