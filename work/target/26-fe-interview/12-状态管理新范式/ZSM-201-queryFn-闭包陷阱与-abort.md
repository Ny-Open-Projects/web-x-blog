---
title: [ZSM-201] queryFn 里闭包变量不更新和请求取消怎么一起解决
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-201：queryFn 里闭包变量不更新和请求取消怎么一起解决

**答**：
- queryFn 是普通函数，每次渲染重新创建，但闭包里捕获的变量如果不在 queryKey 里，缓存命中时用的是旧闭包值——规则是「参与请求的所有变量都必须进 queryKey」
- queryFn 收到 context，其中 `signal` 是 AbortSignal，queryKey 变化或组件卸载时 Query 会自动 abort，fetch 传 `signal` 就能真正取消底层请求
- 取消后抛出的是 AbortError，库会吞掉它不计为错误，不要自己 catch 后再 setState
- ESLint 规则 `@tanstack/query/exhaustive-deps` 能静态检查 queryKey 与 queryFn 依赖一致性，建议 CI 强制开启

```javascript
import { useQuery } from '@tanstack/react-query'

function Search({ keyword, lang }) {
  const query = useQuery({
    // keyword/lang 都参与请求 → 都必须进 key
    queryKey: ['search', keyword, lang],
    queryFn: async ({ signal, queryKey }) => {
      // 也可以从 queryKey 反取参数，避免闭包漂移
      const [, kw, lg] = queryKey
      const res = await fetch(`/api/search?q=${kw}&lang=${lg}`, { signal })
      if (!res.ok) throw new Error(`HTTP ${res.status}`)
      return res.json()
    },
    // queryKey 变化时旧请求自动 abort，这里无需手动 AbortController
  })
  return <pre>{JSON.stringify(query.data ?? {})}</pre>
}
```
