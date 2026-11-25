---
title: [ARC-417] 前端 SDK 的多版本共存架构如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-417：前端 SDK 的多版本共存架构如何设计？
**答**:
- 共存场景：同一页面多个业务接不同版本的 SDK（监控 SDK v2/v3）、第三方站点嵌入的 JS SDK 无法控制宿主升级。
- 架构方案：命名空间隔离（window.__SDK__ 挂载区分版本）、全局单例注册表（最先加载的版本作为 host，后续版本检测已存在则复用或降级为受控代理）。
- 协议优先：SDK 间通过"核心协议"通信（全局队列 + 版本协商），新版本只提交增量能力，旧版本接口行为保持向后兼容（弃用告警不删除，保留 N 个大版本）。
- 加载策略：loader 极小化（几 KB）负责版本决策——拉 manifest 决定加载哪个版本，业务代码只接触稳定 facade。
- 治理：版本使用分布上报（哪些宿主还在用 v1），推动升级有数据；硬 EOL 时 loader 返回兼容 shim 并告警。
```javascript
// SDK loader 版本协商
async function loadSDK() {
  if (window.__SDK__ && window.__SDK__.protocol >= 3) return window.__SDK__; // 复用已加载
  const manifest = await fetchJson('/sdk/manifest.json');      // { latest, minProtocol }
  if (window.__SDK__ && window.__SDK__.protocol >= manifest.minProtocol)
    return window.__SDK__;                                     // 旧版本满足最低协议
  return injectScript(`/sdk/v${manifest.latest}/index.js`);
}
```
