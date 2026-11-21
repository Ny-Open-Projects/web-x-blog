---
title: [PER-654] 端到端加密（E2EE）聊天在前端怎么实现？密钥协商、消息加密与设备间的信任传递
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-654：端到端加密（E2EE）聊天在前端怎么实现？密钥协商、消息加密与设备间的信任传递

**答**：
- 最小可行 E2EE：每设备生成身份密钥对（私钥永不出设备），**双棘轮可以简化为每会话 X25519 协商共享密钥 + 消息递增 IV"**——面试场景讲清 X3DH（身份钥/预签名钥协商）+ Double Ratchet（前向保密）的核心思想即可。
- 前端职责：密钥生成与存储（IndexedDB 加密存私钥，最好硬件背书 WebAuthn 绑定）、密钥指纹校验（扫码/对比验证对方身份防中间人）、多设备同步（设备密钥链：新设备由老设备扫码授权签名）。
- 服务器只做密文转发与公钥目录（key directory），公钥目录要带服务端签名防替换——服务器被黑也只见密文。
- 现实约束：搜索/推送/消息预览等体验功能与 E2EE 冲突（服务器看不到内容），要产品层取舍；群聊密钥轮换（成员变更即换会话钥）。

```javascript

// 简化 E2EE 会话建立（演示协商思想，生产用 Signal 协议库）
async function establishSession(myPriv, peerPub) {
  // X3DH 思想简化版：双方临时密钥对做 ECDH 得共享秘密
  const eph = await crypto.subtle.generateKey({ name: 'ECDH', namedCurve: 'X25519' }, true, ['deriveBits']);
  const shared = await crypto.subtle.deriveBits(
    { name: 'ECDH', public: peerPub }, eph.privateKey, 256);
  // HKDF 展开为会话密钥（真实实现还要混入身份钥/预签名钥）
  const sessionKey = await crypto.subtle.importKey('raw', shared, 'HKDF', false, ['deriveKey']);
  return crypto.subtle.deriveKey(
    { name: 'HKDF', hash: 'SHA-256', salt: new Uint8Array(32),
      info: new TextEncoder().encode('chat-session-v1') },
    sessionKey, { name: 'AES-GCM', length: 256 }, false, ['encrypt', 'decrypt']);
}
async function seal(key, msg, counter) {
  const iv = new Uint8Array(12); new DataView(iv.buffer).setUint32(0, counter); // 递增 IV
  return crypto.subtle.encrypt({ name: 'AES-GCM', iv }, key, new TextEncoder().encode(msg));
}
// 前向保密：每 N 条消息重协商会话密钥（简化 ratchet）；私钥不出设备，服务器只见密文
```
