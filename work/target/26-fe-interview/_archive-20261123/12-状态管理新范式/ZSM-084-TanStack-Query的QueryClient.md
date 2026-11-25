---
title: [ZSM-084] QueryClient 的实例管理有哪些坑？多实例、测试隔离和持久化分别怎么做？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-084：QueryClient 的实例管理有哪些坑？多实例、测试隔离和持久化分别怎么做？
**答**：
- 单实例原则：一个 React 应用一个 QueryClient（SSR 每请求一个）；多实例会导致缓存分裂、失效无效（invalidate 的不是同一个缓存）。
- 测试隔离：每个用例 `new QueryClient()` 包 Provider，或 afterEach `qc.clear()`，防缓存泄漏造成「单测偶发通过」。
- 持久化：persistQueryClient（experimental_createQueryPersister/localStorage）把缓存写盘，冷启动直出；必须配 staleTime，否则恢复即全量重取。
- 销毁：应用卸载（测试、微前端子应用卸载）调用 qc.clear() 或 unmount 时清理观察者，防内存泄漏。

```javascript
// 测试隔离模板
function renderWithClient(ui) {
  const qc = new QueryClient({ defaultOptions: { queries: { retry: false } } })
  return render(<QueryClientProvider client={qc}>{ui}</QueryClientProvider>)
}
// 持久化
import { experimental_createQueryPersister } from '@tanstack/query-persist-client'
const persister = experimental_createQueryPersister({ storage: localStorage, maxAge: 60_000 })
new QueryClient({ defaultOptions: { queries: { persister: persister.persisterFn, staleTime: 60_000 } } })
```
