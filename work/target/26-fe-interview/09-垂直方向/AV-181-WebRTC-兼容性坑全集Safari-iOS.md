---
title: [AV-181] WebRTC 兼容性坑全集：Safari/iOS 的差异清单。（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-181：WebRTC 兼容性坑全集：Safari/iOS 的差异清单。（高频）
**答**：
- SDP：Safari 的 H264 profile 协商严格（要用 Constrained Baseline）；renegotiation 时序怪癖，冲突要显式 rollback。
- iOS 特有：切后台 RTC 挂起、锁屏断流、静音键影响音频路由、getUserMedia 必须 HTTPS。
- API 缺口：RTCRtpScriptTransform 与 Chrome 的 createEncodedStreams 是两套；sendEncodings 部分字段支持滞后；getStats 字段命名与单位有差异。
- 播放侧：Safari 原生 HLS 不走 MSE，hls.js 要探测降级为原生播放。
- 工程对策：能力探测表 + adapter.js 兼容层 + 真机回归矩阵（iOS 大版本必测），把"差异"变成数据而不是记忆。

```javascript
// WebRTC 兼容层：统一差异点（adapter 思路简版）
const compat = {
  supportsSimulcast: (() => {
    const pc = new RTCPeerConnection();
    try {
      pc.addTransceiver('video', { direction: 'sendonly', sendEncodings: [{ rid: 'q' }, { rid: 'f' }] });
      return true;
    } catch { return false; } finally { pc.close(); }
  })(),
  supportsEncodedTransform: typeof RTCRtpScriptTransform !== 'undefined',
  nativeHls: document.createElement('video').canPlayType('application/vnd.apple.mpegurl') !== '',
};
// Safari 与 Chrome 的 insertable streams 两套接口统一封装
function attachTransform(sender, worker) {
  if (compat.supportsEncodedTransform) {
    sender.transform = new RTCRtpScriptTransform(worker, { role: 'sender' });  // 新标准与Safari
  } else if (sender.createEncodedStreams) {                                     // Chrome 旧接口
    const { readable, writable } = sender.createEncodedStreams();
    worker.postMessage({ readable, writable }, [readable, writable]);
  }
}
// getStats 兼容取数：字段与单位差异统一封装
async function outboundBytes(pc) {
  const s = await pc.getStats();
  let total = 0;
  s.forEach((r) => { if (r.type === 'outbound-rtp' && r.kind === 'video') total += r.bytesSent ?? 0; });
  return total;  // 差分再除时间 由调用方计算速率
}
```
