---
title: [AV-125] DRM 与加密播放怎么做？EME 流程与 Widevine/FairPlay 的区别？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-125：DRM 与加密播放怎么做？EME 流程与 Widevine/FairPlay 的区别？（高频）
**答**：
- 三层概念：内容加密（CENC 标准分片加密）、密钥管理（DRM 服务签发 license）、协议桥（EME 让 JS 与浏览器 CDM 交互）。
- 三大体系：Widevine（Chrome/Android）、FairPlay（Safari/iOS）、PlayReady（Edge/Windows）；同一内容打 CENC，各端请求各自体系的 license。
- EME 流程：requestMediaKeySystemAccess → createMediaKeys → setMediaKeys → encrypted 事件 → generateRequest → license 请求 → session.update。
- 轻量替代：AES-128 加密 HLS（AV-141），安全性低于 DRM 但实现简单，适合内部培训等场景。
- 前端注意：license 请求要带自定义 header（走 xhr 设置）；HDCP 输出保护用 getStatusForPolicy 查询。

```javascript
// EME 标准流程骨架（Widevine 示例）
async function setupDrm(video, licenseUrl, authToken) {
  const config = [{
    initDataTypes: ['cenc'],
    videoCapabilities: [{ contentType: 'video/mp4; codecs="avc1.42E01E"' }],
  }];
  const access = await navigator.requestMediaKeySystemAccess('com.widevine.alpha', config);
  const keys = await access.createMediaKeys();
  await video.setMediaKeys(keys);
  video.addEventListener('encrypted', async (ev) => {
    const session = keys.createSession('temporary');
    session.addEventListener('message', async (msg) => {
      const res = await fetch(licenseUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/octet-stream', Authorization: authToken },
        body: msg.message,                                   // license challenge
      });
      await session.update(new Uint8Array(await res.arrayBuffer())); // 密钥入库 解密开始
    });
    await session.generateRequest(ev.initDataType, ev.initData);
  });
}
// 输出保护查询：4K 仅在 HDCP2.2 输出下可用
// const status = await video.mediaKeys.getStatusForPolicy({ minHdcpVersion: '2.2' }); // 'usable'
```
