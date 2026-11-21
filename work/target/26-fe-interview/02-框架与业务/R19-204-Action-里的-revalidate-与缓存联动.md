---
title: [R19-204] Server Action 中的 revalidateXxx 是怎么和缓存联动的？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-204：Server Action 中的 revalidateXxx 是怎么和缓存联动的？
**答**：
- `revalidatePath('/goods')`：失效该路径的 Router Cache 与 Data Cache，下一次导航/刷新重新取数。
- `revalidateTag('goods-list')`：按 tag 失效，配合 fetch 的 next.tags 使用，跨页面精准失效。
- Action 内调用后，React 会把受影响路径的更新「随响应」推给客户端（action 返回即触发客户端路由刷新），无需手动 router.refresh。
- 常见错误：action 里 revalidate 了但页面没更新——检查是否被 client cache 层（useEffect 缓存）挡住，或 tag 没挂在对应 fetch 上。
- 粒度选择：列表页用 tag（一改全失效），详情页用 path；避免全站 revalidatePath('/')。
