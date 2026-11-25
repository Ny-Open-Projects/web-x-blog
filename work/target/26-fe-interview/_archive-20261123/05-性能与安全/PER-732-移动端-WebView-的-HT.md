---
title: [PER-732] 移动端 WebView 的 HTTP 缓存与 H5 缓存协同：容器缓存目录、清理时机与双缓存打架问题
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-732：移动端 WebView 的 HTTP 缓存与 H5 缓存协同：容器缓存目录、清理时机与双缓存打架问题

**答**：
- 三层缓存叠加：WebView 磁盘缓存（HTTP 缓存）、H5 层缓存（IDB/内存）、服务端缓存——"双缓存打架指 H5 层缓存了旧数据但 HTTP 缓存返回 304 造成数据陈旧，或反向。
- 协同原则：**不可变资源**（带 hash 文件名）交给 HTTP 缓存（max-age=1y + immutable），H5 层不重复缓存静态资源；**可变 API** 不依赖 HTTP 缓存（Cache-Control: no-cache + ETag 条件请求），数据缓存归 H5 层管理（TTL 语义自己定）。
- 容器清理时机：磁盘配额告警、版本升级、用户登出——H5 侧要暴露 `clearCache(scope)` JSAPI 并区分 scope（静态/API/全部），全清后要有冷启动心理预期。
- 排查工具：容器侧缓存目录占用统计 JSAPI + Performance API 的 transferSize（0 = 命中缓存）验证策略是否生效。

```javascript

const webviewCacheCoop = {
  immutable: '静态资源（hash 文件名）：HTTP 缓存 max-age=1y immutable，H5 不重复缓存',
  api: 'API：no-cache + ETag 条件请求，数据 TTL 语义归 H5 层管（避免双缓存打架）',
  cleanup: { triggers: ['配额告警', '版本升级', '登出'], api: 'clearCache(scope) 区分静态/API/全部',
    note: '全清后首启是冷加载，要有骨架屏预期' },
  verify: 'resource entries transferSize === 0 即命中 HTTP 缓存，用于验证策略生效',
};
function verifyCacheHit() {
  return performance.getEntriesByType('resource')
    .filter(r => r.transferSize === 0).length /
    Math.max(1, performance.getEntriesByType('resource').length);
}
```
