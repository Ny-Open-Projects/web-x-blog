---
title: [FRP-338] 框架无关的 Feature Flag 内核
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 面试题, 发布]
type: 面试题
---

## FRP-338：框架无关的 Feature Flag 内核

**答**：
- 内核模型：flags（Map<string, value>）+ 分流（用户哈希）+ 订阅（变更推送）——纯 JS；框架层做响应式绑定
- 分流一致性：跨框架页面同一用户必须同组——内核按 userId + experimentId 哈希（与端无关）——分流的「跨端一致」是核心需求
- 初始化时序：flags 在首屏渲染前就绪（同步注入 HTML 或启动接口）——「后到 flag」导致的闪烁与二次渲染要避免
- 热更新：flag 服务推送（SSE）→ 内核更新 → 订阅者（两框架）收到——实时开关的全链路
- 治理：flag 过期清理（TTL 自动摘除代码引用）、审计（谁改的）、回滚——flag 债务的系统化管理

```javascript
export function createFlags({ userId }) {
  const flags = new Map();
  const subs = new Set();
  const evalFlag = (key, def) => {
    const config = flags.get(key);
    if (!config) return def;
    if (config.rollout < 1) return hash(`${config.expId}:${userId}`) / 1e6 < config.rollout;  // 哈希分流
    return config.value;
  };
  return {
    get: evalFlag,
    setAll(map) { for (const [k, v] of Object.entries(map)) flags.set(k, v); subs.forEach((f) => f()); },
    sub(fn) { subs.add(fn); return () => subs.delete(fn); },
  };
}
// React: useSyncExternalStore(flags.sub, () => flags.get(key))
// Vue:   customRef 包 flags.get
```
