---
title: [PER-785] 池化 WebView 的登录态与 Cookie 预置：复用实例如何保证用户态正确且不串号
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-785：池化 WebView 的登录态与 Cookie 预置：复用实例如何保证用户态正确且不串号

**答**：
- 风险场景：A 用户退登后 B 用户登录，取到带 A Cookie 的池实例——串号是最高优先级事故。
- 方案：实例登记"所属会话指纹"（uid/token 哈希），acquire 时比对，指纹不一致先走清 Cookie+storage 再交付；共享域 Cookie 由容器在登录/登出事件里主动刷新池实例。
- 预置：登录后 idle 时对热池实例批量写入新 Cookie（容器侧 API），让复用实例"出厂即带登录态"，省一次鉴权往返。
- 细节：多账号/小号场景禁用池化或按账号分池；退出登录必须同步清池（不能只清当前页）。

```javascript
class SessionAwarePool {
  constructor() { this.pool = []; }
  acquire(session) {                          // session: { fp: 会话指纹 }
    const i = this.pool.findIndex(w => w.fp === session.fp);
    if (i >= 0) return this.pool.splice(i, 1)[0];       // 指纹一致：直接复用
    const w = this.pool.pop();
    if (w) {                                    // 指纹不一致：清理后重新预置
      w.clearCookies(); w.clearStorageByPrefix('app_');
      w.presetCookie(session.cookie); w.fp = session.fp;
    }
    return w;
  }
  onLogout() { this.pool.splice(0).forEach(w => { w.clearCookies(); w.destroy(); }); }  // 登出全清
}
```
