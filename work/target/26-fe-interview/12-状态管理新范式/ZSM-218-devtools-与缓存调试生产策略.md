---
title: [ZSM-218] Query devtools 怎么在生产环境安全接入排查线上问题
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-218：Query devtools 怎么在生产环境安全接入排查线上问题

**答**：
- devtools 是独立包（@tanstack/react-query-devtools），生产默认不打包；排查线上问题时可按「灰度开关 + 权限」动态挂载只读面板
- 更工程化的线上方案：订阅 QueryCache 事件，把 query key、耗时、成败上报到监控平台，比本地 devtools 覆盖面大
- devtools 能看缓存条目、fetchStatus 与 data 时间线，定位「为什么没重新请求」类问题最快（查 staleTime/gcTime/enabled）
- 生产安全线：只读不写、不展示敏感 data 字段（脱敏）、入口藏在 query 参数 + 员工身份校验之后

```javascript
const showDev = new URLSearchParams(location.search).has('__qd') && isStaff()
{showDev && <ReactQueryDevtools initialIsOpen={false} />}

// 线上监控：cache 事件上报
queryCache.subscribe((e) => {
  if (e.type === 'updated' && e.action?.type === 'success')
    report('query_ok', { key: JSON.stringify(e.query.queryKey) })
})
```
