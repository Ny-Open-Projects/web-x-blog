---
title: [AV-168] 设计一个网页版多机位导播台（切换/预览/PGM）。（高频压轴）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-168：设计一个网页版多机位导播台（切换/预览/PGM）。（高频压轴）
**答**：
- 广播术语：PVW（预览，准备切出的画面）、PGM（节目，正在输出的画面）、Tally（机位在播提示灯）。
- 核心：多路输入（拉流预览）→ 切换（硬切/叠化/画中画）→ 合成输出（canvas/WebGL 合成）→ 推流（WHIP/RTMP）。
- 切换时序：切 PGM 前先在 PVW 调好；硬切要在同一 rAF 内换源防撕裂；叠化用合成层透明度动画。
- 音频导播：音频跟随视频源或独立调音台（每路 gain + 主输出）。
- 工程约束：多路同时解码性能（≤4 路 720p）、键盘快捷键（1-4 选机位，空格切出）、Tally 状态信令同步。

```javascript
// 导播台合成核心：PVW/PGM 双缓冲 + 硬切/叠化
class Switcher {
  constructor(sources) {              // sources: [{ id, video }]
    this.sources = sources;
    this.pgm = sources[0];
    this.canvas = document.createElement('canvas');   // 1280x720 合成画布
  }
  cut(toId) {                         // 硬切：立即换 PGM 源（同 rAF 内完成防撕裂）
    this.pgm = this.sources.find((s) => s.id === toId);
    tally.broadcast({ pgm: toId });   // Tally 广播 各机位端亮红灯
  }
  fade(toId, ms = 500) {              // 叠化：透明度动画
    const from = this.pgm, to = this.sources.find((s) => s.id === toId);
    const start = performance.now();
    const step = (now) => {
      const k = Math.min(1, (now - start) / ms);
      this.composite(from, to, k);    // 两层叠加 alpha = k
      if (k < 1) requestAnimationFrame(step);
      else { this.pgm = to; tally.broadcast({ pgm: to.id }); }
    };
    requestAnimationFrame(step);
  }
  output() { return this.canvas.captureStream(30); }   // 合成画布 → 推流
  composite(a, b, k) { /* 在 canvas 上按 alpha 绘制两层 */ }
}
```
