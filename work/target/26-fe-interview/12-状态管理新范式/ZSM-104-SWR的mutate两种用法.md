---
title: [ZSM-104] SWR 的 mutate 有哪两种用法？手动失效和乐观更新分别怎么实现？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-104：SWR 的 mutate 有哪两种用法？手动失效和乐观更新分别怎么实现？
**答**：
- 两种入口：全局 `mutate(key, data?, options?)` 可在任意位置失效任意缓存；绑定式 `const { mutate } = useSWR(key)` 只作用于当前 key。返回值都是 Promise，便于在异步 action 里链式收尾。
- 三种形态：`mutate(key)` 只重新验证；`mutate(key, newData, { revalidate: false })` 只写缓存；`mutate(key, newData)` 先写再验证（乐观更新默认形态）。
- 乐观更新标准姿势：用函数式更新拿到旧值 → 立即写本地 → 发请求 → 失败时 `mutate(key, oldData, { revalidate: false })` 回滚。
- 与 TanStack Query 对比：Query 靠 onMutate 快照 + onError 回滚 + onSettled invalidate 三段式，SWR 更轻但要自己写快照与回滚。

```javascript
import useSWR, { mutate as globalMutate } from 'swr'

async function likeGoods(id) {
  const key = ['/api/goods', id]
  // 乐观 +1：函数式拿到旧值
  await globalMutate(key, (cur) => ({ ...cur, likes: cur.likes + 1 }))
  try {
    const server = await api.like(id)
    // 用服务端真值覆盖并关闭本轮验证
    await globalMutate(key, server, { revalidate: false })
  } catch (e) {
    await globalMutate(key, (cur) => ({ ...cur, likes: cur.likes - 1 }),
      { revalidate: false })   // 回滚，不触发重取避免闪烁
    throw e
  }
}

function GoodsCard({ id }) {
  const { data, mutate } = useSWR(['/api/goods', id], fetcher)
  return <button onClick={() => mutate(d => ({ ...d, likes: d.likes + 1 }))}>
    赞 {data?.likes}
  </button>   // 绑定式 mutate 只改本地缓存，不重新请求
}
```
