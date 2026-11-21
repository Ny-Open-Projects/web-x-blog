---
title: [ZSM-205] 离线场景下 mutation 怎么排队等网络恢复再发
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-205：离线场景下 mutation 怎么排队等网络恢复再发

**答**：
- `networkMode` 控制断网行为：`online`（默认，直接抛错）、`always`（照发）、`offlineFirst`（先发一次，失败后等待重连重试）——mutation 想排队就用 `offlineFirst`
- 配合 `createSyncStoragePersister` + `persistQueryClient`，mutation 会被写入 storage，网络恢复 + 页面重载后自动重放
- 需要挂 `resumePausedMutations`：persister 恢复后调用它，让暂停的 mutation 继续执行
- 顺序敏感的操作要给 mutation 设置 `mutationKey` 相同值，库会按 key 串行重放，避免乱序覆盖

```javascript
import { createSyncStoragePersister } from '@tanstack/query-sync-storage-persister'
import { persistQueryClient } from '@tanstack/react-query-persist-client'
import { onlineManager } from '@tanstack/react-query'

const persister = createSyncStoragePersister({ storage: localStorage })
persistQueryClient({ queryClient, persister })

const queryClient = new QueryClient({
  defaultOptions: { mutations: { networkMode: 'offlineFirst', mutationKey: ['op'] } }
})

onlineManager.addEventListener('online', () => {
  queryClient.resumePausedMutations()   // 恢复暂停的 mutation 队列
})
```
