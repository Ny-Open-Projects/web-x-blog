---
title: [ZSM-216] staleTime Infinity 什么时候合理什么时候是坑
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-216：staleTime Infinity 什么时候合理，什么时候是坑

**答**：
- 合理面：本质不变的数据（国家列表、币种、用户自己的档案缓存至退出）、由 WS/Server Action 主动失效的数据（失效事件即新鲜度时钟）
- 坑面：把 Infinity 当「性能优化」，没有失效机制配合时数据永久陈旧；多标签页各自 Infinity，互相看不到更新
- 折中方案：staleTime Infinity + WebSocket 失效/版本号轮询，把「何时重新拉」的责任显式化
- 评估维度是数据新鲜度需求的业务成本：展示错 5 分钟的价格可接受吗？可接受才用长 staleTime

```javascript
// 不变的字典数据
useQuery({ queryKey: ['countries'], queryFn: fetchCountries, staleTime: Infinity })
// 版本号失效：轮询 version，变化即 invalidate
useQuery({ queryKey: ['meta-version'], queryFn: fetchVersion, refetchInterval: 60_000,
  select: (v) => { if (v !== last) queryClient.invalidateQueries({ queryKey: ['config'] }); return v } })
```
