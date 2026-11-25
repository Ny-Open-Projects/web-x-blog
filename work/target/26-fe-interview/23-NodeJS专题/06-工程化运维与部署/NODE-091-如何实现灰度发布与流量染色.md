---
title: [NODE-091] 如何实现灰度发布与流量染色？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-091：如何实现灰度发布与流量染色？
**答**：
- 灰度策略：按 **uid/设备指纹取模**（稳定分流）、按白名单（内部员工先行）、按比例（1% → 5% → 50% → 100%）、按地域/机房。
- 实现：BFF 网关在入口决策——读取灰度配置（配置中心热更新，NODE-089）→ 计算命中版本 → **流量染色**：把 `x-gray-tag: v2` 写入请求头传递给下游，同时写响应头让前端感知；下游多版本实例按 tag 路由（K8s label selector / service mesh）。
- 关键细节：同一用户的**所有请求必须稳定命中同一版本**（会话粘性），避免体验分裂；灰度实例要有独立监控看板（错误率对比 v1/v2）；自动回滚：灰度错误率超阈值自动切回全量 v1。

```javascript
// 灰度决策中间件（BFF 入口）
const grayConfig = { enabled: true, ratio: 5, whitelist: [1, 42, 10086], tag: 'v2' };

function pickVersion(uid) {
  if (!grayConfig.enabled) return 'v1';
  if (grayConfig.whitelist.includes(uid)) return grayConfig.tag;      // 白名单
  // 稳定哈希取模：同一 uid 永远同一桶，不会一会儿 v1 一会儿 v2
  const bucket = murmurhash(String(uid)) % 100;
  return bucket < grayConfig.ratio ? grayConfig.tag : 'v1';
}

app.use(async (ctx, next) => {
  const uid = ctx.state.user?.uid ?? 0;
  const version = pickVersion(uid);
  ctx.state.grayTag = version;
  ctx.set('x-gray-tag', version);                     // 响应头：前端/测试感知当前版本
  await next();
});

// 调用下游时透传染色头，下游按 tag 路由到对应版本实例
async function callDownstream(path) {
  return fetch(`${DOWNSTREAM_URL}${path}`, {
    headers: { 'x-gray-tag': ctx.state.grayTag },     // 染色透传
  });
}

// 自动回滚：灰度版本错误率超阈值自动切回
setInterval(async () => {
  const v2Stats = metrics.get('error_rate', { tag: 'v2' });
  const v1Stats = metrics.get('error_rate', { tag: 'v1' });
  if (v2Stats > v1Stats * 2 && v2Stats > 0.01) {      // 错误率翻倍且超 1%
    grayConfig.enabled = false;
    log.error({ event: 'gray_auto_rollback', v2_error_rate: v2Stats });
    alertToOps('灰度自动回滚已触发');
  }
}, 30000).unref();
```
