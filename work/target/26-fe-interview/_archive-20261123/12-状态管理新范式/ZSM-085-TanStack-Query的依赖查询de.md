---
title: [ZSM-085] 依赖查询（先拿 token 再拉用户）怎么写？enabled 门控的正确姿势和边界
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-085：依赖查询（先拿 token 再拉用户）怎么写？enabled 门控的正确姿势和边界
**答**：
- 依赖查询：第一个查询拿 token/城市 id，第二个查询 `enabled: !!cityId`，cityId 就绪才发请求；queryKey 里带上依赖变量。
- enabled 语义：false 时不请求不缓存，组件读到 status 'pending'；依赖变化（false→true）自动触发。
- 边界一：enabled false 时 data 是 undefined，渲染层必须判空，不能拿 placeholder 充数。
- 边界二：能用 queryFn 内 await 合并的就合并（一次请求链），拆两次查询只为了「能独立缓存/失效」时才有价值。
- enabled 还用于：条件查询（弹窗打开才请求）、登录态门控、节流（配合 debounce 的 keyword）。

```javascript
const { data: city } = useQuery({ queryKey: ['geo'], queryFn: api.geo })
const { data: weather } = useQuery({
  queryKey: ['weather', city?.id],
  queryFn: () => api.weather(city.id),
  enabled: !!city?.id,   // 依赖就绪才发
})
// weather.data 判空渲染
```
