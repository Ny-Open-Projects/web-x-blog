---
title: [XP-094] WebView 的缓存策略怎么设计？资源与接口双缓存怎么做？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-094：WebView 的缓存策略怎么设计？资源与接口双缓存怎么做？
**答**：
- 分层缓存模型：**离线包（拦截替换静态资源，最快最可控）→ HTTP 缓存（Cache-Control/ETag，CDN 边缘）→ 内存缓存 → 接口数据缓存（本地兜底）**，逐层命中递减。
- 资源侧：核心静态资源进离线包（XP-093），大图/视频走 CDN + 懒加载；WebView 拦截请求（`shouldInterceptRequest`/`URLProtocol`）命中本地包直接返回，不发网络。
- **接口双缓存**：写穿透缓存（stale-while-revalidate）——先回本地缓存数据立即渲染，同时后台请求新数据刷新并更新缓存；缓存 key 含参数指纹与数据版本，过期策略按业务分级（列表 5 分钟、配置 1 小时、用户态不缓存）。
- 用户态安全：登录态相关接口禁缓存或加密存储；缓存清理随账号切换与包版本升级联动，防串号。
- 治理指标：离线包命中率、接口缓存命中后首屏耗时对比、脏数据投诉率；缓存策略变更需灰度验证（XP-093 灰度通道复用）。

```javascript
// api/cache.js —— 接口层 stale-while-revalidate 双缓存
const POLICY = { list: { maxAge: 5 * 60 }, config: { maxAge: 60 * 60 }, user: null };

async function request(path, params) {
  const policy = POLICY[routeOf(path)];
  const key = `${path}?${stableStringify(params)}`;      // 参数指纹做 key
  if (!policy) return rawFetch(path, params);            // 用户态等敏感接口：直连不缓存

  const cached = await cacheStore.get(key);              // 本地持久缓存（IndexedDB/MMKV）
  const fresh = cached && Date.now() - cached.t < policy.maxAge * 1000;

  if (fresh) return cached.data;                         // 新鲜缓存：0ms 返回
  if (cached) {
    renderStale(cached.data);                            // 旧缓存先渲染：骨架屏直接出内容
    revalidate(path, params, key);                       // 后台静默刷新，不打断交互
    return cached.data;
  }
  return rawFetch(path, params);                         // 无缓存：正常请求 + 骨架屏
}

async function revalidate(path, params, key) {
  try {
    const data = await rawFetch(path, params);
    await cacheStore.set(key, { data, t: Date.now() });
    applyFresh(data);                                    // 新数据到达，diff 后无感刷新
  } catch (e) { /* 静默失败：用户继续用旧数据 */ }
}
// 资源侧配套：离线包拦截 shouldInterceptRequest 命中本地；大图 CDN 参数裁剪 + 懒加载
// 命中缓存的首屏接口耗时 P95 从 ~800ms 降至 ~30ms（口径 XP-069/XP-117）
```
