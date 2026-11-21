---
title: [NODE-149] 服务发现与健康检查如何实现？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-149：服务发现与健康检查如何实现？
**答**：
- 三件事：**注册**（实例上线带 TTL 登记）、**心跳续约**（过期自动摘除，解决实例死亡不注销）、**发现**（客户端拉取 + 本地缓存，注册中心挂了也能用旧表）。
- 生产选型：Consul/Nacos/etcd/K8s Service；自研仅用于理解原理。
- 健康检查两级：liveness（进程活着）与 readiness（依赖就绪可接流量，NODE-061）——**注册时机绑定 readiness**，依赖没就绪不接流量。
- 优雅上下线：上线 readiness 通过后再注册；缩容先反注册再停进程，避免 502 窗口。

```javascript
// 简易注册中心核心（生产用 Consul/Nacos）
const registry = new Map(); // key: name:addr → { addr, weight, expires }

function register(name, instance, ttlMs = 15_000) {
  registry.set(`${name}:${instance.addr}`, { ...instance, name, expires: Date.now() + ttlMs });
}
function renew(name, addr, ttlMs = 15_000) {          // 心跳续约
  const k = `${name}:${addr}`;
  const it = registry.get(k);
  if (it) it.expires = Date.now() + ttlMs;
  else register(name, { addr }, ttlMs);
}
setInterval(() => {                                    // 过期摘除：实例死了不注销也自动下线
  for (const [k, v] of registry) if (v.expires <= Date.now()) registry.delete(k);
}, 5000);

// 客户端：拉取 + 过滤 + 本地缓存（注册中心挂了用旧表）
function discover(name) {
  return [...registry.values()]
    .filter((i) => i.name === name && i.expires > Date.now())
    .map(({ addr, weight }) => ({ addr, weight }));
}
// 实例侧：readiness 通过才 register；SIGTERM 先反注册再排空
```
