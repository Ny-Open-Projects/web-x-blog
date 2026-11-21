---
title: [MFW-228] TanStack Start 的流式 SSR 与 Query 脱水细节
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-228：Start 流式 SSR 与 Query 脱水

**答**:
- 脱水时机：loader 的 ensureQueryData Promise 完成即可流式吐出（不必等全部 loader——Suspense 边界分批）——Query 缓存序列化进 HTML
- 客户端复水：dehydrate(queryClient).payload → script 注入 → hydrate 前 setQueryData（缓存版本一致——staleTime 继承服务端时间戳避免立即重拉）
- 流式分段：慢 loader 的段用 Suspense 包裹（后吐）——Query 脱水分批跟随（部分复水也要一致——key 齐全才 set）
- 陷阱：SSR 抛错的路由段——错误也要序列化给客户端（ErrorComponentProps 接管）——不能只 hydrate 成功路径

```javascript
// 服务端出口
const html = await render(() => <App />, { dehydrate: () => dehydrate(queryClient) })
// 客户端入口
hydrate(app, { hydrate: (el) => hydrate(queryClient, extracted) })   // 复水到同一缓存
```
