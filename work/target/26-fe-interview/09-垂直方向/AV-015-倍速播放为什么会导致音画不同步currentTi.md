---
title: [AV-015] 倍速播放为什么会导致音画不同步？currentTime 跳变要处理什么？
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-015：倍速播放为什么会导致音画不同步？currentTime 跳变要处理什么？
**答**：
- video+audio 分轨时（尤其 MSE 双 SourceBuffer），变速后两轨时钟漂移策略不同就会失同步；同一 mux 内浏览器会自己维持。
- 设置 `currentTime` 是硬跳变：会触发 seeking/waiting，清空 decode 队列，画面可能闪黑帧，外挂字幕/弹幕必须监听 `seeked` 重新对齐。
- 倍速只改 `playbackRate`，音频经 resample 变调；要保音调需 `preservesPitch = true`（默认 true， Safari 老版本要加 webkit 前缀）。
- 倍速范围兼容性：Chrome 支持 0.0625~16，iOS Safari > 4 有被静默限速的情况，需测试兜底。
- 实践：切倍速时若 buffer 不足先降速或提示；弹幕、歌词、字幕都以 currentTime 为唯一时钟源，禁止各自 setInterval 累计。

```javascript
// 倍速控制 + 同步敏感组件的时钟订阅
class PlaybackRateController {
  constructor(video) {
    this.video = video;
    if ('preservesPitch' in video) video.preservesPitch = true; // 保音调
    video.webkitPreservesPitch = true;
  }
  setRate(rate) {
    const clamp = (x) => Math.min(4, Math.max(0.5, x)); // 业务安全范围
    const r = clamp(rate);
    const wasBuffering = this.video.readyState < 3; // HAVE_FUTURE_DATA
    if (wasBuffering) return console.warn('buffer 不足，暂缓切速');
    this.video.playbackRate = r;
    this.video.dispatchEvent(new CustomEvent('ratechanged', { detail: r }));
  }
}

// 弹幕/字幕以 currentTime 为唯一时钟：seek 后强制对齐
const video = document.querySelector('video');
video.addEventListener('seeked', () => {
  danmakuEngine.reset(video.currentTime); // 清屏重排
  subtitleEngine.align(video.currentTime);
});
// 外部进程（如画中画/投屏）改了时间，也要感知
video.addEventListener('timeupdate', () => {
  if (Math.abs(video.currentTime - expectedTime) > 0.5) {
    expectedTime = video.currentTime; // 时钟被外部改动，重新同步
  }
});
```

---

## 三、流媒体协议（AV-016 ~ AV-023）
