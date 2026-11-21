---
title: [ZSM-114] 带取数的组件怎么测试？SWR 的测试要点和缓存污染怎么处理？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-114：带取数的组件怎么测试？SWR 的测试要点和缓存污染怎么处理？
**答**：
- 三层策略：mock fetcher 层（msw 拦截请求）、直接注入缓存（`mutate(key, mockData, { revalidate: false })`）、关闭副作用（revalidateOnFocus 等在测试环境全关）。
- 缓存污染是头号坑：SWR 全局缓存跨测试用例存活，会导致「第二个用例没请求就拿到上个用例的数据」。解法是每个用例前 `cache.clear()` 或渲染时包独立的 `<SWRConfig value={{ provider: () => new Map() }}>`。
- 断言异步数据用 waitFor/byRole 而非固定 sleep；测试错误分支时让 msw 返回 500 并断言 error UI 与重试按钮。
- 组件外逻辑（如 onLogout 批量失效）单独抽函数测，不经过组件渲染。

```javascript
import { render, screen, waitFor } from '@testing-library/react'
import { SWRConfig } from 'swr'
import { GoodsList } from './goods-list'
import { server } from './mocks/server'

beforeEach(() => server.listen({ onUnhandledRequest: 'error' }))
afterEach(() => server.resetHandlers())

function renderIsolated(ui) {
  return render(
    // 独立缓存实例：用例间互不污染
    <SWRConfig value={{
      provider: () => new Map(),
      revalidateOnFocus: false,
      revalidateOnReconnect: false,
    }}>{ui}</SWRConfig>
  )
}

test('渲染商品列表', async () => {
  renderIsolated(<GoodsList/>)
  await waitFor(() => expect(screen.getByRole('list')).toBeInTheDocument())
})
```
