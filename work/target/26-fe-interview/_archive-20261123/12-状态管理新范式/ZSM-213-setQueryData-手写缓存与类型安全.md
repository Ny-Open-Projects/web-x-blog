---
title: [ZSM-213] 直接 setQueryData 改缓存的适用场景与风险
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-213：直接 setQueryData 改缓存的适用场景与风险

**答**：
- 适用：WebSocket 推送单点更新、乐观更新落地、本地计算结果写回（如阅读数 +1）；本质是「以服务端数据源身份直接改缓存」
- 风险一：写入的数据结构必须与 queryFn 返回完全一致（含形状），否则消费端 select/派生崩溃——用 updater 函数 `(old) => ...` 做增量而非整包替换
- 风险二：直接写 data 不改 updatedAt，条目仍是 stale，挂载时可能被 refetch 覆盖；必要时用 `setQueryData` 后再 `invalidate` 或调整 staleTime
- updater 里 old 可能是 undefined（缓存不存在），必须兜底返回；不要在 updater 里做异步

```javascript
queryClient.setQueryData<Order>(['order', id], (old) =>
  old ? { ...old, status: 'PAID' } : old   // old 兜底，不做整包替换
)
// 与 invalidate 的选择：能精确算出结果 → setQueryData；算不出 → invalidate
```
