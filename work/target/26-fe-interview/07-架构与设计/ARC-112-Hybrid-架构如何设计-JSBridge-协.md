---
title: [ARC-112] Hybrid 架构如何设计（JSBridge 协议 / 离线包 / 首屏加速）？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-112：Hybrid 架构如何设计（JSBridge 协议 / 离线包 / 首屏加速）？
**答**：
- JSBridge 协议四要素：请求 id（回调配对）、命名空间（module.action）、参数与结果序列化约定、权限模型（按域名/场景白名单授权能力）。
- 通信通道：iOS 用 WKScriptMessageHandler / prompt 拦截，Android 用 addJavascriptInterface（注解白名单），两端协议统一由桥层封装，业务只见 Promise。
- 离线包：业务 H5 打成 zip 包（含版本 manifest）预下发，客户端拦截请求优先取本地，命中离线包则首屏不发网络请求；差量更新降低流量。
- 首屏加速组合拳：离线包 + 接口预取（native 提前请求首屏接口注入）+ 免登注入（native 带登录态）+ 页面预加载。

```typescript
// JSBridge 协议定义（两端统一）
interface BridgeRequest { id: string; module: string; action: string; data?: unknown }
interface BridgeResponse { id: string; code: number; msg?: string; data?: unknown }

// WebView 侧：统一封装，业务只见 Promise
const pending = new Map<string, (res: BridgeResponse) => void>();
let seq = 0;
function invoke(module: string, action: string, data?: unknown): Promise<unknown> {
  const id = `${Date.now()}_${++seq}`;
  // 权限：桥层校验当前 H5 域名是否在 module 白名单内，不通过直接拒绝
  if (!bridgeACL.isAllowed(location.host, module, action)) {
    return Promise.reject(new Error(`bridge denied: ${module}.${action}`));
  }
  return new Promise((resolve) => {
    pending.set(id, (res) => res.code === 0 ? resolve(res.data) : Promise.reject(res.msg));
    native.postMessage(JSON.stringify({ id, module, action, data }));  // 走原生通道
  });
}
// 原生回调分发：按 id 配对 resolve，超时 5s 自动 reject 防泄漏
// 离线包 manifest 示例：
// { "biz": "mall", "version": "1.2.0", "files": {"index.html": "sha256..." },
//   "preFetch": ["/api/home/feed"], "interceptHosts": ["m.corp.com"] }
// 更新策略：native 启动时拉差量包（版本 diff）→ 校验 sha256 → 原子切换
```
