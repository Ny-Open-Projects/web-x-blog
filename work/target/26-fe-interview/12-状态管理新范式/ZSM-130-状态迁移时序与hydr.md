---
title: [ZSM-130] 分层架构下的 hydration 时序问题：SSR 数据、持久化 store、URL 三者怎么对齐？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-130：分层架构下的 hydration 时序问题：SSR 数据、持久化 store、URL 三者怎么对齐？
**答**：
- 三条数据在 hydration 时各自就位：SSR 缓存靠 dehydrate/hydrate（Query）或 fallback（SWR）注入；持久化 store 靠 localStorage 回放（Zustand persist 的 onRehydrateStorage）；URL 状态直接从 location 解析，最早就绪。
- 经典错位：持久化 store 的旧值覆盖 SSR 新值（如主题/选中租户），或 SSR 数据尚未 hydrate 时组件读了空 store 触发双请求。解法：统一「等 hydrated 完成再渲染主树」的门控。
- Zustand 的 persist 提供 `hasHydrated` 回调；Query 的 hydration 用 `useHydrate` 在 client 入口一次性灌入，两者都不应在 render 期间异步写。
- 面试要点：能画出「Server render → 注入 script data → client hydrate → 缓存/store 对齐 → 首次交互」的时间线。

```javascript
// 入口：缓存、store、URL 三源对齐后再挂载业务树
import { Hydrate, QueryClientProvider } from '@tanstack/react-query'

function Root({ dehydratedState }) {
  const [queryClient] = useState(() => makeClient())
  const hydrated = useStoreHydrated()      // Zustand persist 完成标记
  if (!hydrated) return <AppSkeleton/>     // 门控：防旧值覆盖/双请求

  return (
    <QueryClientProvider client={queryClient}>
      <Hydrate state={dehydratedState}>    {/* SSR 缓存注入 */}
        <App/>                             {/* URL 状态组件内部直接 useSearchParams */}
      </Hydrate>
    </QueryClientProvider>
  )
}

function useStoreHydrated() {
  const [ready, setReady] = useState(false)
  useEffect(() => {
    usePersistStore.persist.onFinishHydration(() => setReady(true))
    if (usePersistStore.persist.hasHydrated()) setReady(true)
  }, [])
  return ready
}
```
