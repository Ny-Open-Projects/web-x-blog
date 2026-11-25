---
title: [PER-196] 浏览器隐私新技术（三方 Cookie 退场、分区存储）对前端有什么影响？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-196：浏览器隐私新技术（三方 Cookie 退场、分区存储）对前端有什么影响？

**答**：
- **三方 Cookie 退场**：广告/跨站身份链路迁移到第一方登录态 + 服务端签发匿名 ID；埋点身份从"跨站追踪"改为"第一方假名化"（与 PER-146 呼应）。
- **存储分区化**：iframe 内的 localStorage/Cookie 按顶层站点分区，跨站嵌入场景不能再依赖共享存储；需要共享时走 Storage Access API（带用户授权）。
- **能力探测先行**：所有隐私相关 API（storage、Topics、UA-CH）一律 feature detect + 服务端开关，杜绝"新浏览器抛错"事故。
- 工程账单：身份链路改造要同步改埋点口径与风控规则，否则指标断裂、风控误杀同时发生。

```javascript
// 隐私技术演进应对：三方 Cookie 退场与分区存储下的兼容策略
export function storageAvailable(type) {
  try {
    const s = window[type], k = '__probe__';
    s.setItem(k, k); s.removeItem(k);
    return true;
  } catch { return false; } // 分区或禁用后可能抛错
}

// 1. 身份标识：放弃三方 Cookie 依赖，改第一方存储 + 服务端签发匿名 ID
export async function getAnonId() {
  let id = null;
  if (storageAvailable('localStorage')) id = localStorage.getItem('anon_id');
  if (!id) {
    const r = await fetch('/api/identity/anon', { method: 'POST' }).then((x) => x.json());
    id = r.anon_id;                                   // 服务端签发，走第一方 HttpOnly Cookie
    try { localStorage.setItem('anon_id', id); } catch {}
  }
  return id;
}

// 2. 跨站嵌入场景：Storage Access API 带授权访问分区前的存储
export async function requestEmbeddedStorage() {
  if (document.hasStorageAccess && !(await document.hasStorageAccess())) {
    await document.requestStorageAccess().catch(() => null); // 用户拒绝则走无状态模式
  }
}

// 3. 采集端不再读跨站信号：Topics 与 UA-CH 全部 feature detect 加服务端开关
```
