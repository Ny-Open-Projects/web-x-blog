---
title: [PER-661] 手写一个密钥管理前端 SDK：会话密钥申请、仅内存持有、轮换监听与销毁
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-661：手写一个密钥管理前端 SDK：会话密钥申请、仅内存持有、轮换监听与销毁

**答**：
- 前端密钥的正确姿势：**密钥来自服务端会话下发**（RSA 包裹），只在内存持有（不写 localStorage/sessionStorage），页面卸载即销毁；轮换由服务端推送事件触发重新申请。
- 要点：加密导出不可行（导出 raw 再加密还是落盘）——原则是不导出，需要持久化的场景（记住登录）改用设备绑定凭据（WebAuthn）而不是存密钥；密钥对象用 `crypto.subtle` 的 Key 对象（不可读出原始字节）天然防内存嗅探。
- 边界：轮换期间新旧密钥并行（版本前缀）；销毁动作尽力而为（JS 无法真正抹内存，Key 对象由 GC 回收）；多 Tab 共享密钥不落地方案（BroadcastChannel 传 Key 对象不可行，需各自申请）。
- 评分点：Key 对象持有与轮换并行。

```javascript

class KeyVault {
  constructor(serverPubKey) { this.keys = new Map(); this.serverPub = serverPubKey; }
  async init() {
    await this.rotate();                                          // 启动申请会话密钥
    this.ws = listenServerEvent('key-rotate', () => this.rotate());
    addEventListener('pagehide', () => this.destroy());           // 卸载销毁
  }
  async rotate() {
    // 向服务端申请：返回 RSA 包裹的 AES 密钥（用 RSA-OAEP 公钥包裹）
    const { wrapped, version } = await api('/session/key', { pubFingerprint: this.fp });
    const aesKey = await unwrapKey(wrapped, this.serverPub);      // 解包为 subtle Key 对象
    this.keys.set(version, { key: aesKey, ts: Date.now() });      // 仅内存 Map
    // 轮换并行：新版本加密，旧版本只解密，过期版本清理
    for (const [v, k] of this.keys) if (Date.now() - k.ts > 300000) this.keys.delete(v);
  }
  current() { return [...this.keys.values()].at(-1).key; }
  destroy() { this.keys.clear(); this.ws?.close(); }              // 尽力销毁（GC 兜底）
}
// 红线：密钥永不写 localStorage/sessionStorage/cookie；需持久化的登录态用 WebAuthn 凭据
```
