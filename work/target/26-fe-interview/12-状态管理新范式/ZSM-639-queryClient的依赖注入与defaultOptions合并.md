---
title: [ZSM-639] queryClient 的依赖注入与 defaultOptions 三层合并机制
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-639：queryClient 的依赖注入与 defaultOptions 三层合并机制

**答**：
- TanStack Query 的 DI 设计：所有 hook（useQuery/useMutation）通过 `useQueryClient()` 从 Context 拿 client 实例——同一组件树可以挂多个 client（多后端/多租户），测试时注入 mock client。client 是「配置 + 缓存 + 调度」的聚合根，库的状态管理哲学是「一切配置都可按层覆盖」。
- 三层合并：`client.defaultOptions`（全局）→ `queryCache.config`（按缓存）→ 单次调用 options（hook 参数）。合并规则是浅合并 + 特殊字段覆盖——**嵌套对象（如 retry 的函数）直接整体覆盖不递归**，所以 hook 里只写想覆盖的顶层键。
- per-key 默认值：`queryClient.setQueryDefaults(['todos'], { staleTime: 60000 })`——按 key 前缀给缓存条目组设默认；`setQueryDataDefaults` 给初始值。适合「同域 API 不同策略」（配置类长缓存、交易类短缓存）。
- 运行期全局控制：`client.isFetching()`（在途计数）、`client.mount()`/`unmount()`（observer 生命周期）、`client.resumePausedMutations()`（恢复离线 mutation）——这些能力让 client 成为「全局网络状态的控制器」，WS 事件/路由切换时可以程序化批控。
- 追问钩子：SSR 每请求 client + defaultOptions 也要每请求新建（defaultOptions 里若有闭包可变状态会串请求）。

```javascript
// 多 client 场景
const mainClient = new QueryClient({
  defaultOptions: { queries: { staleTime: 30_000, retry: 2 } },
})
const billingClient = new QueryClient({
  defaultOptions: { queries: { staleTime: 0, retry: 1 } },   // 交易域：短缓存少重试
})
<QueryClientProvider client={mainClient}>
  <BillingSection client={billingClient} />   // 局部覆盖 provider
</QueryClientProvider>

// per-key 默认值
queryClient.setQueryDefaults(['config'], { staleTime: 1000 * 60 * 10, gcTime: Infinity })
queryClient.setQueryDefaults(['orders'], { staleTime: 0, refetchOnWindowFocus: true })
useQuery({ queryKey: ['config', 'theme'] })    // 自动应用 config 组默认

// 运行期批控：路由切换暂停预取 / 全局失效
router.beforeEach(() => {
  if (queryClient.isFetching() > 20) queryClient.cancelQueries()   // 请求过载保护
})
// 登出时：清空 + 恢复暂停的 mutation 不该再发
queryClient.cancelQueries()
queryClient.removeQueries()
queryClient.getMutationCache().clear()
```
