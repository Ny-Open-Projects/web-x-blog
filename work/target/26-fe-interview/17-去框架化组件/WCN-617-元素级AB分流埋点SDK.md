---
title: [WCN-617] 笔试：实现元素级 AB 实验分流与埋点 SDK（稳定分桶 + 曝光去重 + 交互上报）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-617：笔试：实现元素级 AB 实验分流与埋点 SDK（稳定分桶 + 曝光去重 + 交互上报）

**答**：
- 需求：实现 ExperimentSDK：assign(user, exp) 返回稳定版本；trackExposure(el, expId) 同一元素只上报一次曝光；trackClick(el, expId) 上报交互并带版本上下文。
- 思路：稳定哈希分桶；曝光用 WeakSet 记录元素去重；上报 payload 统一带 {expId, version, userId}。
- 边界：用户无 id 时用会话 id；WeakSet 避免内存泄漏；上报失败静默降级不影响交互。

```javascript
class ExperimentSDK {
  constructor() { this.exposed = new WeakSet(); }
  assign(userId, exp) {
    let h = 0;
    for (const c of `${userId}:${exp.salt}`) h = (h * 31 + c.charCodeAt(0)) >>> 0;
    const version = h % 100 < exp.traffic ? exp.versionB : exp.versionA;
    return { version, bucket: h % 100 };
  }
  trackExposure(el, expId, version, userId) {
    if (!el || this.exposed.has(el)) return;
    this.exposed.add(el);
    this.send({ type: 'exposure', expId, version, userId });
  }
  trackClick(expId, version, userId) {
    this.send({ type: 'click', expId, version, userId });
  }
  send(payload) {
    try { navigator.sendBeacon?.('/exp', JSON.stringify(payload)); }
    catch { /* 上报失败静默降级 */ }
  }
}
const sdk = new ExperimentSDK();
const a = sdk.assign('u_1', { salt: 's', traffic: 50, versionA: 'A', versionB: 'B' });
sdk.trackExposure(document.body, 'btn', a.version, 'u_1');
```

**评分点**：
- 分桶用稳定哈希（用户+salt），同一用户结果一致。
- 曝光用 WeakSet 去重，且弱引用不泄漏。
- 上报 payload 带齐 expId/version/userId 上下文。
- sendBeacon + try/catch，失败不影响业务交互。
