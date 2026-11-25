---
title: [PER-789] 离线包与 Service Worker 双方案对比与选型：各自适用边界与共存策略
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-789：离线包与 Service Worker 双方案对比与选型：各自适用边界与共存策略

**答**：
- 离线包（容器拦截）：由 App 容器在请求层拦截，不依赖页面 JS 执行，冷启动即生效（首访就命中）；但只能在自家 App 内用，且需客户端发版支持。
- Service Worker：Web 标准能力，跨容器可用；但首次访问无 SW（第二次才生效），冷启动 SW 启动本身有延迟，且依赖页面 JS。
- 选型：自有 App 主阵地用离线包（保首访命中），浏览器/外部流量用 SW + PWA 兜底；两者共存时以离线包优先（容器层拦截先于 SW 触发）。
- 统一视角：两者本质都是"请求拦截+本地缓存"，把 SW 的缓存策略表（cache-first/SWR）复用到离线包策略配置上，心智统一。

```javascript
// 双方案共存的路由决策（配置化）
const cacheStrategy = {
  'static/': { sw: 'cache-first', offline: true },    // 静态资源：两方案都覆盖
  'api/list': { sw: 'stale-while-revalidate', offline: false },  // 数据接口：仅 SW
  'sdk/': { sw: null, offline: true },                // 容器 SDK：仅离线包
};
function intercept(url) {
  const rule = matchRule(url, cacheStrategy);
  if (rule.offline && OFFLINE_MAP.has(url)) return local(url);   // 离线包优先
  if (rule.sw && navigator.serviceWorker?.controller) return;    // SW 处理
  return network(url);                                            // 兜底回源
}
```
