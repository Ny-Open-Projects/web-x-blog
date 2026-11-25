---
title: [PER-741] 移动端 PWA 离线可用的性能设计： precache 清单、runtime 缓存分策略与更新提示
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-741：移动端 PWA 离线可用的性能设计： precache 清单、runtime 缓存分策略与更新提示

**答**：
- 三层策略：**precache**（App Shell：HTML 骨架/关键 CSS/JS，安装期全量预缓存，离线秒开）、**runtime 缓存分策略**（静态资源 cache-first、API network-first 带超时回退缓存、图片 stale-while-revalidate）、**更新机制**（新 SW waiting -> 提示用户刷新，避免更新了但不生效"）。
- 性能取舍：precache 清单要克制（> 2MB 安装耗时且占配额），按页面拆分 precache（首页 shell 精确清单）；SW 响应要快（缓存命中 < 5ms），避免在 fetch 事件里做重计算。
- 移动端特有：浏览器杀死 SW/清理缓存的条件（7 天未用 storage 回收——Chrome），关键数据不能只放 Cache API（配额策略双写 IDB 兜底）。
- 度量：离线命中率、SW 拦截耗时分布、precache 安装耗时、更新采纳率。

```javascript

const pwaStrategy = {
  precache: { what: 'App Shell（HTML 骨架/关键 CSS/JS）', limit: '< 2MB，按页面拆分精确清单' },
  runtime: {
    static: 'cache-first（不可变资源）',
    api: 'network-first + 3s 超时回退缓存',
    image: 'stale-while-revalidate',
  },
  update: '新 SW waiting -> 提示刷新，避免不生效',
  mobile: 'Chrome 7 天未用清 storage：关键数据双写 IDB 兜底',
  metrics: ['离线命中率', 'SW 拦截耗时 < 5ms', 'precache 安装耗时', '更新采纳率'],
};
```
