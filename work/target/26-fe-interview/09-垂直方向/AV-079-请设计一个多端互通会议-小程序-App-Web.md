---
title: [AV-079] 请设计一个多端互通会议（小程序/App/Web）。
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-079：请设计一个多端互通会议（小程序/App/Web）。
**答**：
- 互通的本质：统一信令协议 + 统一媒体接入（SFU 对各端一视同仁）+ 各端 SDK 封装同一套业务语义（房间/角色/麦位）。
- 各端差异：Web 走浏览器 WebRTC；小程序用 live-pusher/live-player（RTMP 私有链路或微信同层 RTC）；App 用原生 SDK。差异被服务端转协议抹平（小程序 RTMP 进 → 服务端转 RTP 进 SFU）。
- 对齐问题：各端时间戳基准不同，混流/录制以服务端时钟为准；消息序号全局统一。
- 能力降级：小程序不支持 simulcast → 服务端转码出多档；Web 端不支持 H265 → 协商回落 H264。
- 联调方法论：以信令协议文档 + 时序图为契约，各端独立跑通"回环测试"再互通。

```javascript
// 统一信令契约（各端共同遵守的协议定义）
// 统一协议 schema（节选）
const SIGNAL_PROTOCOL = {
  'join.req':   { roomId: 'string', token: 'string', clientType: 'web|miniprogram|app', sdkVersion: 'string' },
  'join.resp':  { code: 'number', selfUid: 'string', snapshot: 'PeerSnapshot' },
  'media.pub':  { sdp: 'string', tracks: [{ kind: 'audio|video', simulcast: 'boolean' }] },
  'media.ans':  { sdp: 'string' },
  'ice.cand':   { candidate: 'IceCandidate' },
  'room.evt':   { event: 'peer-joined|peer-left|role-changed', payload: 'object' },
};
// 小程序端适配器：live-pusher/RTMP 进 RTC 网
const miniAdapter = {
  async publish(roomId, streamName) {
    const pushUrl = await fetch(`/api/rtmp/url?room=${roomId}&stream=${streamName}`)
      .then((r) => r.json());
    const ctx = wx.createLivePusherContext();
    return new Promise((resolve, reject) =>
      ctx.start({ url: pushUrl.rtmp, mode: 'RTC', success: resolve, fail: reject }));
    // 服务端把 RTMP 转 RTP 注册进 SFU，其余端正常 consume
  },
};
```
