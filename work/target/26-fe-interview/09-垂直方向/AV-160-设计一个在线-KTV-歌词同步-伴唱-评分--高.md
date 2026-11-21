---
title: [AV-160] 设计一个在线 KTV（歌词同步/伴唱/评分）。（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-160：设计一个在线 KTV（歌词同步/伴唱/评分）。（高频）
**答**：
- 核心：伴奏与原唱双音轨 + 歌词逐字同步（QRC 逐字时间戳）+ 混音（人声 + 伴奏）+ 评分（音高比对）。
- 同步基准：用媒体时钟（audioContext.currentTime / video.currentTime）驱动，不用 setInterval 累计（会漂移）。
- 连麦合唱：伴奏由主唱端统一播放，副唱端只收人声——避免两端伴奏不同步；RTC 只上行人声。
- 评分：Web Audio 取人声基频（自相关法），与标准 MIDI 音高比对，逐句给分。
- 体验：歌词逐字染色、下一句提示行、抢唱/慢唱检测提示。

```javascript
// KTV 歌词逐字同步与音高采集
class KtvStage {
  constructor(lrc, musicEl) {
    this.lrc = parseQrc(lrc);          // 逐字时间戳
    this.music = musicEl;
  }
  tick() {                             // rAF 驱动 基准 = 媒体时钟
    const t = this.music.currentTime * 1000;
    const word = this.lrc.wordAt(t);
    if (word) paintLyric(word, (t - word.start) / word.dur);  // 逐字染色进度 0-1
    requestAnimationFrame(() => this.tick());
  }
  startPitchTrack(userStream) {        // 评分：取用户人声基频
    const ctx = new AudioContext();
    const an = ctx.createAnalyser();
    an.fftSize = 2048;
    ctx.createMediaStreamSource(userStream).connect(an);
    const buf = new Float32Array(an.fftSize);
    setInterval(() => {
      an.getFloatTimeDomainData(buf);
      const f0 = autocorrelation(buf, ctx.sampleRate);          // 基频估计
      const midi = f0 ? 69 + 12 * Math.log2(f0 / 440) : null;   // 转 MIDI 音高
      scoreEngine.push(midi, this.lrc.expectedMidiAt(this.music.currentTime * 1000));
    }, 100);
  }
}
```
