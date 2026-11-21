---
title: [AV-058] 多码率切换的 UI 与策略怎么做？（手动+自动 ABR）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-058：多码率切换的 UI 与策略怎么做？（手动+自动 ABR）
**答**：
- 双模式：AUTO（默认，ABR 引擎决策）+ 手动档位（用户强制锁定，此时关闭 ABR 升档，只在卡顿时仍允许降档）。
- UI 细节：清晰度菜单展示当前档位与"自动"标记；切换立即生效（直播需对齐 I 帧）；切档后短暂 toast 提示。
- hls.js 对应：`hls.currentLevel`（立即切换）、`nextLevel`（下个分片生效，推荐）、`loadLevel`、`autoLevelEnabled`。
- 策略参数：`capLevelToPlayerSize`（按播放器尺寸封顶档位）、`startLevel`（起始档位，弱网低起点）。
- 埋点：每次切档记录 from/to/trigger(auto|manual)/buffer 水位，优化 ABR 参数。

```javascript
// 清晰度控制器：auto 与手动档互斥
class QualityController {
  constructor(hls) {
    this.hls = hls;
    hls.on(Hls.default.Events.LEVEL_SWITCHED, (_, d) => this.onChange?.(d.level));
  }
  get levels() {
    return this.hls.levels.map((l, i) => ({
      index: i, height: l.height, bitrate: l.bitrate,
      current: i === this.hls.currentLevel,
    }));
  }
  setAuto() {
    this.hls.currentLevel = -1;         // -1 = 自动 ABR
    this.manual = false;
  }
  setManual(index) {
    this.manual = true;
    this.hls.nextLevel = index;         // 下个分片生效，避免打断
    this.hls.autoLevelCapping = index;  // 手动模式下也限制 ABR 不会升回去
  }
  // 弱网例外：手动锁定 1080p 但持续卡顿，仍降一档并提示
  onStallTooLong() {
    if (this.manual && this.hls.currentLevel > 0) {
      this.hls.nextLevel = this.hls.currentLevel - 1;
      this.notifyUser('网络不佳，已暂时降低清晰度');
    }
  }
}
```
