---
title: [PER-385] HTTP 缓存头的调试方法论：一个"总是回源"的资源如何系统排查？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-385：HTTP 缓存头的调试方法论：一个"总是回源"的资源如何系统排查？

**答**：
- 排查链（从响应倒推）：① 看响应头——有没有 Cache-Control/ETag/Last-Modified；② 看请求头——请求是否带了 `Cache-Control: no-cache`（代码里 fetch 默认参数/cache: 'no-store'）或 Authorization（带凭据请求默认不走共享缓存）；③ 看 URL——query 里有时间戳/随机数（`?t=169...` 反缓存写法）直接废掉缓存键；④ 看 CDN 面板——该 URL 的缓存 key 规则是否包含 Cookie/全 query。
- 常见元凶排行：URL 带时间戳（约定俗成的反缓存，改用内容 hash 文件名）；fetch 默认 `cache: 'default'` 但响应头 `no-store`（服务端配置错）；HTML 中间层代理剥离缓存头；Set-Cookie 响应导致浏览器拒绝缓存共享。
- 修复验证：DevTools Network 禁用缓存关闭，二次加载看 `from disk cache`/`from memory cache`/`304`；CDN 面板命中率分 URL 验证；RUM 侧看该资源 transferSize 是否归零（命中本地缓存 transferSize=0）。
- 方法论沉淀：把"缓存头审计"进巡检（PER-364），新资源上线自动检查缓存头是否合理。

```text
"总是回源"排查链：
1. 响应头：Cache-Control 缺失/no-store？ ETag 有无？
2. 请求头：fetch 有无 cache:'no-store'？ 带 Authorization？（默认不走共享缓存）
3. URL：query 带时间戳/随机数？（缓存键被污染）
4. CDN：缓存 key 是否含 Cookie/全 query？
5. 中间层：网关/代理是否剥了缓存头？ Set-Cookie 导致拒绝缓存？
验证：二次加载 from cache 或 304；transferSize === 0；CDN 命中率分 URL 复查
修复优先级：去掉 URL 时间戳（内容 hash）> 修正响应头 > 调 CDN key 规则
```
