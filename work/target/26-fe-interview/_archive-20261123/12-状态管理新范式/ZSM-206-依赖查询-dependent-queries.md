---
title: [ZSM-206] 后一个查询依赖前一个查询的结果怎么写
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-206：后一个查询依赖前一个查询的结果怎么写

**答**：
- dependent query：`enabled: !!prev.data`，上一个查询拿到数据前，下一个保持 pending 不发请求
- 依赖的 id 要同时写进 queryKey，否则上游变化下游不会跟着刷新，形成脏数据
- 链式依赖超过两层要警惕瀑布请求（串行 RTT 叠加），能合并成一次后端聚合接口就合并
- `isPending` 判断是「等上游」还是「请求中」：enabled=false 时 isPending 为 true 但没有网络开销，UI 上要区分展示

```javascript
const { data: user } = useQuery({
  queryKey: ['user', userId],
  queryFn: () => fetchUser(userId),
})

const { data: projects, isPending } = useQuery({
  queryKey: ['projects', userId, user?.id],        // 依赖值进 key
  queryFn: () => fetchProjects(user.id),
  enabled: !!user,                                 // user 未就绪不发请求
})
```
