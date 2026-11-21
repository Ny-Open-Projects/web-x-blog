---
title: [AV-121] hls.js 的内部怎么工作？PlaylistLoader、FragmentLoader 与调度器？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-121：hls.js 的内部怎么工作？PlaylistLoader、FragmentLoader 与调度器？（高频）
**答**：
- 架构：主线程 Controller 状态机（IDLE→LOADING→PARSING→APPENDING→BUFFERING）+ 两类 Loader（playlist/fragment 分离，走 XHR/fetch）。
- LIVE 模式：按 reloadInterval 重拉 m3u8，用媒体序列号（MEDIA-SEQUENCE）增量发现新分片，滑动窗口决定可播区间。
- ABR 在 level-controller：吞吐 + buffer 选举 level，软切换优先（不重启解码）。
- 纠错链：分片超时/失败 → retry 配置 → 片段退避 → level 降级 → fatal 事件兜底。
- 可插拔点：自定义 loader（p2p 分发、防盗签注入）、自定义 abrController，是面试能加分的"工程深度"证据。

```javascript
import Hls from 'hls.js';
const hls = new Hls({
  liveSyncDurationCount: 3,          // 直播起点落后边缘 3 个分片 秒开与延迟的平衡
  manifestLoadingTimeOut: 10000,
  fragLoadingMaxRetry: 6,            // 分片重试次数
  abrEwmaDefaultEstimate: 1_000_000, // 初始带宽估计 影响首帧清晰度
  startLevel: -1,                    // -1 自动；0 锁定最低保首帧
});
hls.on(Hls.Events.MANIFEST_PARSED, (_, data) => data.levels.forEach((l) => console.log(l.height)));
hls.on(Hls.Events.FRAG_LOADED, (_, data) => trackFirstFrame(data.frag.stats.loading.end));
hls.on(Hls.Events.ERROR, (_, data) => {
  if (!data.fatal) return;           // 非致命错误内部自愈
  const recover = {
    [Hls.ErrorTypes.NETWORK_ERROR]: () => hls.startLoad(),        // 网络错重启加载
    [Hls.ErrorTypes.MEDIA_ERROR]: () => hls.recoverMediaError(),  // 解码错重建解码
  };
  (recover[data.type] ?? (() => hls.destroy()))();
});
hls.loadSource('https://cdn.example.com/live/index.m3u8');
hls.attachMedia(videoEl);
```
