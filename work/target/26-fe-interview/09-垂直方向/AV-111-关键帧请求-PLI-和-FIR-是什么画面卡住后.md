---
title: [AV-111] 关键帧请求 PLI 和 FIR 是什么？画面卡住后为什么会自动恢复？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-111：关键帧请求 PLI 和 FIR 是什么？画面卡住后为什么会自动恢复？（高频）
**答**：
- 解码端丢包/换流后无法继续解 P 帧，通过 RTCP 反馈向发送端要关键帧：PLI（Picture Loss Indication）与 FIR（Full Intra Request）。
- 差异：FIR 常用于"新订阅者必须立刻出画"，PLI 用于丢包后恢复；前端不直接发送，由解码器自动触发，SFU 再向源头转发。
- 前端感知：getStats 的 inbound-rtp 里 pliCount/firCount 上涨 = 远端频繁请求关键帧，说明链路丢包严重或订阅切换频繁。
- 体验问题：切流后黑屏 1-2 秒本质是等 I 帧；优化靠 SFU 缓存最近 GOP 或发布端关键帧间隔更密。
- 与 AV-083 花屏排查呼应：花屏是"错的帧还在解"，说明 PLI 恢复链路失效，要查 RTCP 通道。

```javascript
// 监控 PLI/FIR 频次：判断链路丢包与解码健康度
class KeyframeMonitor {
  constructor(pc, peerId, interval = 2000) {
    this.prev = new Map();
    this.timer = setInterval(async () => {
      const stats = await pc.getStats();
      stats.forEach((r) => {
        if (r.type !== 'inbound-rtp' || r.kind !== 'video') return;
        const p = this.prev.get(r.id) ?? { pli: 0, fir: 0 };
        const d = {
          pli: (r.pliCount ?? 0) - p.pli,
          fir: (r.firCount ?? 0) - p.fir,
          lost: (r.packetsLost ?? 0) - (p.lost ?? 0),
        };
        if (d.pli + d.fir > 2) {
          report({ level: 'warn', peerId, ssrc: r.ssrc, ...d,
            msg: '关键帧请求激增 链路丢包或订阅切换' });
        }
        this.prev.set(r.id, { pli: r.pliCount ?? 0, fir: r.firCount ?? 0, lost: r.packetsLost ?? 0 });
      });
    }, interval);
  }
  stop() { clearInterval(this.timer); }
}
```
