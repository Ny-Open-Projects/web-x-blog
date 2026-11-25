---
title: [AV-260] 视频 DRM 播放：EME 接入与降级
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-260：视频 DRM 播放：EME 接入与降级

**答**：
- DRM（EME）：Widevine（Chrome/Android）/ FairPlay（Safari）——requestMediaKeySystemAccess 探测 → license 交换 → 解密播放。
- 降级：DRM 不支持 → 明文试看片段 + 登录提示；或 L1 级别设备差异（分辨率限制）。
- 前端实现：MediaKeys + MediaKeySession（license 请求/更新）接线。

```javascript
async function setupDRM(video, licenseServer) {
  const config = [{ initDataTypes: ['cenc'],
    videoCapabilities: [{ contentType: 'video/mp4; codecs="avc1.640028"' }] }];
  const access = await navigator.requestMediaKeySystemAccess('com.widevine.alpha', config);
  const keys = await access.createMediaKeys();
  await video.setMediaKeys(keys);
  const session = keys.createSession();
  session.addEventListener('message', async (e) => {
    const license = await fetch(licenseServer, { method: 'POST',
      body: e.message }).then(r => r.arrayBuffer());        // license 交换
    await session.update(license);
  });
  // 初始化数据（从 MP4 pssh box 提取）
  await session.generateRequest('cenc', psshData);
}
// 降级：requestMediaKeySystemAccess 抛错 → 试 playready → 明文试看 + 引导升级
```
