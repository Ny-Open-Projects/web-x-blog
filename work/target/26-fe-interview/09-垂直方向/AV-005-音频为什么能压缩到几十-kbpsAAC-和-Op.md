---
title: [AV-005] 音频为什么能压缩到几十 kbps？AAC 和 Opus 的区别与选型？
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-005：音频为什么能压缩到几十 kbps？AAC 和 Opus 的区别与选型？
**答**：
- 压缩三板斧：心理声学模型（掩蔽效应，丢弃听不见的频段）、时频变换（MDCT）、熵编码，故有损压缩也能"听不出来"。
- AAC：MP3 继任者，44.1/48kHz 音乐场景质量好，直播/点播生态最成熟，浏览器 MP4 容器内兼容性最佳。
- Opus：RFC 6716，内置 SILK（语音）+ CELT（音乐）双模式自动切换，延迟极低（2.5~60ms 帧），是 WebRTC 唯一强制音频编码。
- 选型结论：点播/直播用 AAC（兼容），实时通信用 Opus（低延迟），窄带语音 Opus 16kbps 仍清晰。
- 语音也可再降级：Opus DTX（静音期不发包）大幅省带宽，是多人会议的标配。

```javascript
// Opus 编码参数在 SDP 中的典型协商结果
const OPUS_SDP_LINE =
  'a=rtpmap:111 opus/48000/2\r\n' +
  'a=fmtp:111 minptime=10;useinbandfec=1;stereo=0;sprop-stereo=0';
console.log(OPUS_SDP_LINE);
// useinbandfec=1 表示开启抗丢包的带内 FEC，弱网下音频更抗断

// WebRTC 中调整音频码率与 DTX（发送前设置）
const pc = new RTCPeerConnection();
pc.addEventListener('negotiationneeded', async () => {
  const sender = pc.getSenders().find((s) => s.track?.kind === 'audio');
  if (!sender) return;
  const params = sender.getParameters();
  params.encodings = [{ maxBitrate: 32_000, dtx: 'enabled' }];
  try {
    await sender.setParameters(params); // Opus 32kbps + DTX
  } catch (e) {
    console.warn('setParameters 失败，部分浏览器不支持 dtx 字段', e);
  }
});

// 用 isTypeSupported 确认 AAC 在 MSE 中可用
console.log(MediaSource.isTypeSupported('audio/mp4; codecs="mp4a.40.2"'));
```
