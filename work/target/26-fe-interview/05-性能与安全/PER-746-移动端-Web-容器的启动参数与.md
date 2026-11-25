---
title: [PER-746] 移动端 Web 容器的启动参数与首屏数据预取协议：容器预取、H5 消费与失配兜底
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-746：移动端 Web 容器的启动参数与首屏数据预取协议：容器预取、H5 消费与失配兜底

**答**：
- 协议设计：容器在创建 WebView 时并行预取首屏接口（Native 网络栈更快），结果序列化进启动参数或 JS 注入；H5 启动时按路由+参数规范化 key 消费预取数据。
- 失配兜底：预取参数与页面实际参数不一致（ deeplink 参数后到）、预取失败、数据格式版本不匹配——三种失配都要降级为页面自己请求，且预取数据带时间戳（过期不用）。
- 关键点：预取 key 必须两端同源（同一规范化函数，双端约定字段顺序）；预取数据要标记来源（`fromPrefetch: true`）便于统计命中率；预取失败的监控（容器预取成功率 < 80% 说明协议有问题）。
- 收益：命中时首屏接口耗时为 0（省 300~800ms），是秒开最大单项优化；命中率目标 85%+。

```javascript

const prefetchProtocol = {
  flow: '容器创建 WebView -> Native 并行预取首屏接口 -> 序列化注入 -> H5 按 key 消费',
  mismatch: ['参数不一致（deeplink 后到）', '预取失败', '格式版本不匹配 -> 都降级页面自请求'],
  key: '预取 key 双端同一规范化函数（字段排序+类型规整）',
  metrics: ['命中率目标 85%+', '预取成功率 < 80% 说明协议有问题', '标记 fromPrefetch 统计'],
};
// 双端共用 key 规范（约定字段字典序）
function normKey(route, params) {
  const sorted = Object.keys(params).sort()
    .map(k => `${k}=${String(params[k])}`).join('&');           // 双端一致：字典序+String 化
  return `${route}?${sorted}`;
}
// H5 消费
function consumeFirstScreen(route, params) {
  const key = normKey(route, params);
  const boot = window.__HYBRID_BOOT?.prefetched;
  if (boot?.key === key && Date.now() - boot.ts < 30000) {
    track('prefetch-hit', { key, fromPrefetch: true });
    return Promise.resolve(boot.data);                          // 命中：0 网络耗时
  }
  track('prefetch-miss', { key, reason: boot ? 'key-mismatch' : 'absent' });
  return fetch(route.api).then(r => r.json());                  // 失配兜底
}
```

**追问**：

1. `normKey` 用 `String(params[k])`，`1` 和 `'1'` 会归一，但 `undefined` 和缺字段呢？ → 要显式剔除 undefined 再排序拼接，否则两端 key 不一致直接全 miss。
2. 预取成功但数据超过 30s，为什么不用？ → 首屏展示旧价或旧库存有资损风险，宁可回源，时效阈值按业务敏感度定。
3. 命中率 85% 目标，deeplink 参数后到导致 miss 怎么优化？ → 容器等参数就绪再预取，或对常见参数组合做预取池，而不是先取后改 key。
