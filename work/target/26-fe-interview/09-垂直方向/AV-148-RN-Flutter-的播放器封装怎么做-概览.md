---
title: [AV-148] RN/Flutter 的播放器封装怎么做？（概览）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-148：RN/Flutter 的播放器封装怎么做？（概览）
**答**：
- RN：react-native-video（基于 ExoPlayer/AVPlayer）；Flutter：video_player、better_player、fijkplayer。
- 桥接要点：JS/Dart 只发指令（play/seek/setSource）+ 收事件（state/progress/error），媒体能力全在 native 层。
- 事件归一：native 事件粒度与 Web 不同（如 iOS itemDidPlayToEndTime），封装层要归一成统一状态机（对齐 AV-126 协议）。
- 原生能力穿透：画中画、后台播放、锁屏控制（MPNowPlayingInfoCenter / AudioService）需在 native 开，封装层暴露开关。
- 选型：纯播放用官方库；直播/DRM/自定义 UI 用 better_player 这类增强库；深度需求自写桥接。

```typescript
// RN 播放器统一封装：桥接层归一事件
import Video, { VideoRef } from 'react-native-video';
class RNPlayerAdapter implements UnifiedPlayer {          // 实现 AV-126 统一协议
  private ref = React.createRef<VideoRef>();
  private listeners = new Map<string, Function[]>();
  state: PlayerState = 'idle';
  load(src: PlaySource) {
    this.state = 'loading';
    return <Video
      ref={this.ref}
      source={{ uri: src.url }}
      resizeMode="contain"
      playsInLine                                          // 对齐 Web 的 playsinline
      onReadyForDisplay={() => this.emit('state', 'playing')}
      onPlaybackStalled={() => this.emit('state', 'stalled')}
      onError={(e) => this.emit('error', e)} />;
  }
  on(ev: string, cb: Function) {
    const l = this.listeners.get(ev) ?? [];
    l.push(cb);
    this.listeners.set(ev, l);
  }
  private emit(ev: string, p?: unknown) { this.listeners.get(ev)?.forEach((f) => f(p)); }
  play() { return this.ref.current?.resume(); }
  pause() { this.ref.current?.pause(); }
  destroy() { /* 卸载组件并清理native资源 */ }
}
```
