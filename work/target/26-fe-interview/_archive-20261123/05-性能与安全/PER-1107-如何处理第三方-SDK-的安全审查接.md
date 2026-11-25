---
title: [PER-1107] 如何处理第三方 SDK 的安全审查（接入前/后）
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1107：如何处理第三方 SDK 的安全审查（接入前/后）

**答**：
- 接入前：审查数据流向（采集哪些字段/上报哪里）、隐私政策覆盖、SDK 权限需求、体积与 CSP 影响。
- 接入后：网络监控（SDK 上报的目标域与内容抽样）、版本升级 diff 审查（新版本加了采集项即触发评审）。
- 控制：SDK 加载走代理网关（可断供）、sandbox iframe 隔离不可信 SDK、最低权限原则（不给 DOM 全权）。
- 退出机制：SDK 可随时替换/下线，业务不硬绑定。

```javascript
// SDK 上报行为监控
function monitorSDK(sdkScriptUrl) {
  const origFetch = window.fetch, origBeacon = navigator.sendBeacon;
  const domain = new URL(sdkScriptUrl).host;
  function audit(kind, url, body) {
    report({ kind, by: domain, to: new URL(url, location.href).host,
      bytes: body?.length ?? 0 });                  // 抽样记录上报行为
  }
  window.fetch = (...a) => { audit('fetch', a[0], a[1]?.body); return origFetch(...a); };
  navigator.sendBeacon = (u, b) => { audit('beacon', u, b); return origBeacon.call(navigator, u, b); };
}
// 新版本 diff：监控到新增上报目标域即触发安全评审
```
