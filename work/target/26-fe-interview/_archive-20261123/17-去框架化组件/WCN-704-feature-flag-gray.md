---
title: [WCN-704] 灰度发布 WC 组件时，如何用 feature flag 做细粒度开关与降级？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-704：灰度发布 WC 组件时，如何用 feature flag 做细粒度开关与降级？

**答**：
- 结论：把 flag 判断收敛到「组件注册层」——根据 flag 决定注册新 tag 还是旧 tag，而非散落在业务代码里；支持按用户/租户/百分比分流。
- flag 服务需本地缓存 + 超时降级到默认值，避免 flag 服务故障导致组件整体不可用；开关切换要幂等、可秒级回滚。
- 追问钩子：正在展示的旧组件实例如何在不刷新的情况下平滑切换到新版本？考察运行时升级与状态迁移能力。

```javascript
const FLAGS = { 'ds-table-v2': { enabled: true, ratio: 0.2 } };
function hash(str) { let h = 0; for (const c of str) h = (h * 31 + c.charCodeAt(0)) >>> 0; return h; }
function pickTag(flagKey, userId) {
  const f = FLAGS[flagKey] || { enabled: false, ratio: 0 };
  if (!f.enabled) return 'ds-table-v1';
  // 按用户哈希稳定分流，避免同一用户反复横跳
  return (hash(userId) % 100) < f.ratio * 100 ? 'ds-table-v2' : 'ds-table-v1';
}
function register(tag) {
  if (!customElements.get(tag)) customElements.define(tag, class extends HTMLElement {});
}
const tag = pickTag('ds-table-v2', 'user-42');
register(tag);
console.log('本次渲染使用:', tag);
```
