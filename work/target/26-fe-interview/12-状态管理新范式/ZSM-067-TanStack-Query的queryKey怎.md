---
title: [ZSM-067] TanStack Query 的 queryKey 怎么设计？数组结构、层级和变量怎么定？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-067：TanStack Query 的 queryKey 怎么设计？数组结构、层级和变量怎么定？
**答**：
- key 是数组，元素从粗到细：`['资源名', 参数, 变体]`，如 `['goods', category, { page, sort }]`；Query 对 key 做**结构化深比较**（对象键序无关），所以同参数多写法是同一缓存。
- 层级即失效粒度：invalidateQueries(['goods']) 失效全部商品查询，['goods', 'shoes'] 只失效鞋类——前缀匹配是设计 key 的核心依据。
- 所有影响请求结果的变量必须进 key：分页、筛选、排序、语言、登录态；漏一个就是「切 tab 数据不刷新」的经典 bug。
- 反模式：把时间戳/随机数放进 key（缓存永远 miss）、把整个对象当字符串拼（丢结构化比较）、key 里塞函数（不可比较）。
- 复杂 key 用 queryOptions 工厂函数统一生成，保证写法一致。

```javascript
// 工厂：key 与 queryFn 同源，防止拼错
const goodsQueries = {
  all: (kw) => ({ queryKey: ['goods', { kw }], queryFn: () => api.goods({ kw }) }),
  detail: (id) => ({ queryKey: ['goods', 'detail', id], queryFn: () => api.goodsDetail(id) }),
}
useQuery(goodsQueries.all('手机'))
qc.invalidateQueries({ queryKey: ['goods'] })       // 全部商品失效
qc.invalidateQueries({ queryKey: ['goods', 'detail', id] }) // 只失效详情
```
