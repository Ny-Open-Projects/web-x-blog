---
title: [XP-096] Native 与 H5 之间的数据同步怎么做？登录态、用户资料如何保持一致？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-096：Native 与 H5 之间的数据同步怎么做？登录态、用户资料如何保持一致？
**答**：
- 同步三类数据：**会话态（token/登录态）、用户画像（昵称头像）、应用配置（主题/语言/灰度桶）**；原则是"原生为权威源，H5 为订阅者"。
- 注入时机：容器创建时通过启动参数/Cookie/localStorage 注入初始快照（避免页面起来后再等桥调用），**注入必须在首屏脚本前完成**。
- 变更推送：原生侧数据变更（登录/登出/资料修改）经桥广播 `profile:update` 事件，H5 订阅后刷新自身状态；H5 侧修改走桥回写原生，由原生统一分发。
- 一致性校验：数据带版本戳/时间戳，页面 `visibilitychange` 回前台时对账一次，不一致拉取最新——防多容器/长驻页面持有旧态。
- 多容器一致性：多个 WebView 实例共享登录态用原生 Cookie 同步（`CookieManager`/`WKHTTPCookieStore`）而非各自存储；账号切换时统一清理所有容器缓存（XP-094 安全项）。

```javascript
// bridge/sync.js —— 原生权威源 + 事件广播 + 前台对账
const ctx = { user: null, config: null, version: 0 };     // H5 侧本地快照

// 1) 容器创建时原生注入初始快照（首屏脚本前执行，避免首屏桥等待）
window.__BOOT_DATA__ && hydrate(window.__BOOT_DATA__);

// 2) 订阅原生变更广播：登录态/资料/配置任一变化即推送
bridge.on('state:update', (payload) => {
  if (payload.version <= ctx.version) return;             // 旧版本戳丢弃，防乱序
  hydrate(payload);
  emitter.emit('store:changed', ctx);                     // 通知页面级订阅者
});

// 3) H5 侧修改走原生回写，由原生统一分发（单一写入口）
export async function updateProfile(patch) {
  const next = await bridge.call('user.updateProfile', patch);
  hydrate(next);                                          // 原生返回新版本快照
  return next;
}

// 4) 前台对账：回可视时向原生要最新版本戳，不一致则拉全量
document.addEventListener('visibilitychange', async () => {
  if (document.visibilityState !== 'visible') return;
  const remote = await bridge.call('state.version', {});
  if (remote.version !== ctx.version) hydrate(await bridge.call('state.snapshot', {}));
});

function hydrate(data) { Object.assign(ctx, data, { version: data.version }); }
// 登出特殊处理：原生清理 Cookie 与所有容器缓存后再广播 state:update（user=null）
```
