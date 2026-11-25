---
title: [AV-359] DRM（数字版权管理）在浏览器的接入
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-359：DRM（数字版权管理）在浏览器的接入

**答**：
- 体系：EME（Encrypted Media Extensions）+ CDM（Widevine/FairPlay/PlayReady）；浏览器实现 CDM。
- 流程：license 请求（服务器返回密钥）→ CDM 解密 → 解码；MSE 喂加密段（cenc 加密）。
- 分层：L1（硬件安全）L3（软件）——高清内容要求 L1，探测 keySystem 能力。

```javascript
// EME 接入骨架
async function setupDRM(video, { certUrl, licenseUrl, keySystem = 'com.widevine.alpha' } = {}) {
  const config = [{ initDataTypes: ['cenc'],
    videoCapabilities: [{ contentType: 'video/mp4; codecs="avc1.640028"' }] }];
  const access = await navigator.requestMediaKeySystemAccess(keySystem, config);
  const keys = await access.createMediaKeys();
  await video.setMediaKeys(keys);
  const session = keys.createSession();
  session.addEventListener('message', async e => {
    const lic = await fetchLicense(licenseUrl, e.message);
    await session.update(lic);                        // 密钥回填
  });
  return session;
}
```
