---
title: [ZSM-207] 数量不固定的列表要每行发一个查询怎么并行管理
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-207：数量不固定的列表要每行发一个查询怎么并行管理

**答**：
- `useQueries({ queries: [...] })` 接收动态数组，返回与输入同序的数组，每个元素是一个 useQuery 结果
- 典型场景：列表页拿到 50 个商品 id，批量查每个 id 的实时库存/价格，无法用一个 key 表达
- keys 动态生成时要保证确定性（排序后再 map），否则 key 数组变化导致缓存全 miss
- 更优解往往是后端提供 `ids` 批量接口 + 一个普通 useQuery；useQueries 适合接口只支持单查的现实约束

```javascript
import { useQueries } from '@tanstack/react-query'

function StockList({ ids }) {
  const results = useQueries({
    queries: ids.map((id) => ({
      queryKey: ['stock', id],
      queryFn: () => fetchStock(id),
      staleTime: 10_000,
    })),
    combine: (rs) => ({            // v5 combine 聚合，避免每行渲染抖动
      stocks: rs.map((r) => r.data),
      loading: rs.some((r) => r.isPending),
    }),
  })
  return results.loading ? '加载中' : <List stocks={results.stocks} />
}
```
