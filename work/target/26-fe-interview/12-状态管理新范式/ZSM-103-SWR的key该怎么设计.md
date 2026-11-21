---
title: [ZSM-103] SWR 的 key 该怎么设计？函数 key、依赖参数、条件取数分别怎么写？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-103：SWR 的 key 该怎么设计？函数 key、依赖参数、条件取数分别怎么写？
**答**：
- key 是缓存的唯一坐标：字符串或数组（内部序列化为同一字符串），所有参数必须进 key，否则不同参数共享缓存会串数据——「列表页第 3 页显示第 1 页数据」基本都是 key 漏了分页参数。
- 函数 key（`() => key`）用于 key 依赖的参数可能未就绪的场景，配合条件取数 `key: ready ? url : null`：key 为 null 时 SWR 不发请求，参数到了再自动触发。
- key 还可传 `[url, token]` 多元组；但注意对象成员顺序会影响序列化结果，动态拼接参数请用 URLSearchParams 固定顺序。
- 全局 mutate 按 key 精确失效，所以 key 设计同时就是失效策略——团队里应抽统一的 `keys.goods(id)` 工厂避免手拼字符串。

```javascript
import useSWR from 'swr'

const keys = {
  goods: (id) => ['/api/goods', id],
  search: (kw, page) => `/api/search?kw=${encodeURIComponent(kw)}&page=${page}`,
}

function GoodsDetail({ id }) {
  // 条件取数：id 未就绪时不请求
  const { data } = useSWR(id ? keys.goods(id) : null, fetcher)
  return <Detail data={data}/>
}

function SearchList({ keyword, page }) {
  // 函数 key：依赖变化自动重新取数
  const { data } = useSWR(() => keyword ? keys.search(keyword, page) : null, fetcher)
  return <List items={data?.list}/>
}
```
