---
title: [XP-398] 手写一个多端会话 token 管理器（互踢可配）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## XP-398：手写一个多端会话 token 管理器（互踢可配）

**答**：
- 需求：implement TokenManager({ multiDevice })。setToken(token, deviceId)；refresh() 续期；被踢（服务端 409 带 kickDevice）时若非本设备忽略、本设备被踢清空跳登录；activeDevices() 列表由服务端返回；输出当前 token 状态。
- 边界：multiDevice=false 时新登录踢旧设备（客户端收到 kick 事件清空）；refresh 竞态合并（单飞）；token 内存持有不落盘。
- 评分点：互踢策略；本设备判定；单飞续期；内存态

```javascript
class TokenManager {
  constructor({ multiDevice = true } = {}) { this.multiDevice = multiDevice; }
  setToken(token, deviceId) {
    if (!this.multiDevice && this.deviceId && this.deviceId !== deviceId)
      return { kicked: this.deviceId };               // 单设备模式踢旧
    this.deviceId = deviceId; this._token = token;    // 内存态
    return { ok: true };
  }
  get token() { return this._token; }
  onKick(event) {
    if (event.deviceId === this.deviceId) {
      this._token = null;
      navigate('/login');
      return { kickedSelf: true };
    }
    return { kickedSelf: false };
  }
  async refresh(api) {
    this._refreshing ??= api('/auth/refresh').finally(() => this._refreshing = null);
    return this._refreshing;                          // 单飞
  }
}
```
