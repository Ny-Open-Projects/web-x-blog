---
title: [DP-375] CQRS：前端读写分离
date: 2026-11-21
categories: [设计模式]
tags: [前端面试, 面试题, 设计模式]
type: 面试题
---

## DP-375：CQRS 前端裁剪版

**答**：
- CQRS 核心：读模型（查询优化）与写模型（命令校验）分离——前端裁剪：读缓存（Query 层：列表/详情缓存）与写命令（mutation 层：提交/校验）分离
- 实战形态：React Query 的 useQuery（读）/useMutation（写）就是前端 CQRS——读走缓存可失效，写走命令带乐观更新
- 读写分离的价值：读可缓存/可 SWR（性能），写可校验/可幂等（正确性）——两套关注点不同
- 读写的一致性桥：写成功后失效相关读缓存（invalidateQueries——CQRS 的同步点）
- 深水点：读模型的「视图裁剪」——列表读模型只取展示字段（大对象裁剪——BFF/selector 层做）——读写模型字段集不同

```javascript
// 读模型 (缓存化)
const { data: list } = useQuery(['orders', filter], () => api.list(filter), { staleTime: 30_000 });
// 写模型 (命令化)
const mutation = useMutation(api.create, {
  onMutate: optimisticAdd,                          // 乐观
  onSuccess: () => qc.invalidateQueries(['orders']),// CQRS 同步点: 写成功→读失效
});
// 读可缓存可失效, 写可校验可幂等 — 两套机制各自最优
```
