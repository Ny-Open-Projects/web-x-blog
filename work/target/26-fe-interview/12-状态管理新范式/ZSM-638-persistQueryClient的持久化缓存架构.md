---
title: [ZSM-638] persistQueryClient：查询缓存的持久化与体积/安全控制
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-638：persistQueryClient：查询缓存的持久化与体积/安全控制

**答**：
- persistQueryClient 把 QueryCache 持久化到 storage（localStorage/IndexedDB/AsyncStorage），首屏 hydrate 后「离线也能看到上次的数据」——PWA/弱网场景的核心能力。持久化内容是 dehydrate 的产物（data + dataUpdatedAt），恢复时按时间判断是否直接可用。
- 体积控制三手段：1) `persistQueryClientPersist` 的 `dehydrateOptions.shouldDehydrateQuery` 白名单——只持久化「高价值」query（列表/配置），不持久化详情页海量缓存；2) 每条 query 配独立 buster（`persister` 层做字段裁剪）；3) 超限降级——IndexedDB 写入前检查体积（如 >2MB 只保留最近 N 条）。
- 失效协议：`buster` 版本字符串——应用 schema 升级（数据结构变了）时换 buster，旧缓存整体丢弃（比 migrate 简单粗暴但可靠）；时效靠 dataUpdatedAt + 客户端 staleTime 自然判断。
- 安全：敏感数据（薪资、医疗）不持久化——白名单反向排除；存储加密意义有限（XSS 可拿 key），重点是「不要存不该存的」。
- 异步恢复的时序：IndexedDB hydrate 是异步的——首帧可能没缓存数据，用 `resumePausedMutations` + Suspense/骨架处理；localStorage 同步版无此问题但有主线程成本。
- 追问钩子：persist 与 SW Cache API 分工——Cache API 存「响应体」（HTTP 层），persistQueryClient 存「查询结果对象」（应用层），弱网首屏两者可叠加。

```javascript
// 持久化配置
import { persistQueryClient, persistQueryClientRestore, persistQueryClientSubscribe } from '@tanstack/query-persist-client'

const queryClient = new QueryClient({
  defaultOptions: { queries: { gcTime: 1000 * 60 * 60 * 24 } },   // gcTime > maxAge 才有意义
})

const localStoragePersister = createAsyncStoragePersister({
  storage: localStorage,
  key: 'QUERY_CACHE_V1',
  buster: 'schema-v3',                      // schema 升级 → 换 buster 全量失效
  throttleTime: 3000,                       // 写节流：3s 合并
})

// 只持久化白名单 query
persistQueryClient({
  queryClient,
  persister: localStoragePersister,
  dehydrateOptions: {
    shouldDehydrateQuery: (query) =>
      query.queryKey[0] === 'config' || query.queryKey[0] === 'feed',
  },
})

// 恢复流程：async persister → 等待 → hydrate → 触发挂载请求（若 stale）
// 组件侧处理异步恢复
const isRestoring = useIsRestoring()   // 恢复期间 useQuery 不发请求
if (!isRestoring) { /* 正常数据路径 */ }
```
