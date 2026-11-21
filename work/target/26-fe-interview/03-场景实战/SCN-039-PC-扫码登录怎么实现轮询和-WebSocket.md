---
title: [SCN-039] PC 扫码登录怎么实现？轮询和 WebSocket 怎么选？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-039：PC 扫码登录怎么实现？轮询和 WebSocket 怎么选？
**答**：
- 流程：PC 请求生成二维码（携带唯一 qrcodeId）→ 手机 App 扫码并确认登录 → 服务端将 qrcodeId 标记为已确认并签发 PC 端 token → PC 端感知后落地登录态。
- 选型：轮询（1~2 秒一次查状态）实现简单、无长连接运维成本，覆盖大多数场景；WebSocket 实时性好、省请求，适合二维码量大或要求秒级体验的业务。
- 必做细节：二维码 60 秒过期自动刷新；状态机清晰（待扫码 / 已扫码待确认 / 已确认 / 已过期），各状态对应不同界面文案。

```javascript
// PC 端：轮询扫码状态，带过期刷新与兜底超时
async function startScanLogin() {
  const { qrcodeId } = await api.createQrcode();  // 前端用 qrcode 库渲染二维码
  const timer = setInterval(async () => {
    const { status, token } = await api.checkQrcode(qrcodeId);
    if (status === 'confirmed') {                 // 手机端已确认
      clearInterval(timer);
      saveToken(token);                           // 落地登录态
      location.href = '/home';
    } else if (status === 'expired') {            // 过期：重新生成二维码再轮询
      clearInterval(timer);
      startScanLogin();
    }
    // pending 等待扫码 / scanned 已扫码待确认，界面展示对应文案
  }, 1500);
  setTimeout(() => { clearInterval(timer); refreshQrcode(); }, 60 * 1000); // 兜底过期
}
```
