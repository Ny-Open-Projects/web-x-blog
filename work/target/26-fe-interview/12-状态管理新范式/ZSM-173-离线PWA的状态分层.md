---
title: [ZSM-173] 场景：离线可用的 PWA，状态层要补哪些能力？数据可靠性怎么保证？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-173：场景：离线可用的 PWA，状态层要补哪些能力？数据可靠性怎么保证？
**答**：
- 缓存持久化：Query 走 persistQueryClient（147 已考实现，这里考设计）或 SWR 自定义 provider，让刷新/断网后仍有数据；配合 staleTime 放宽，避免一联网就全量重取打爆服务端。
- 写操作可靠性：离线队列（121 已考实现）——mutation 失败/断网入队，online 时按序重放；队列要幂等（clientId 去重）防止重放造成重复提交。
- 冲突处理策略：last-write-wins（简单场景）、版本号乐观锁（服务端校验 if-match）、CRDT（协同文档）；PWA 表单类业务一般用乐观锁。
- UI 状态指示：`navigator.onLine` + 缓存 staleness 组合成「离线横幅 + 数据时间戳」，让用户知道看到的是多久前的数据——可观测性进 UI。

```javascript
// 离线横幅：在线状态 + 数据新鲜度
function OfflineBanner() {
  const online = useOnline()                    // navigator.onLine + 事件
  const { dataUpdatedAt } = useQuery({ queryKey: ['orders'], ... })
  const staleMin = Math.floor((Date.now() - dataUpdatedAt) / 60000)
  if (online) return null
  return <div className="banner">离线模式 · 数据更新于 {staleMin} 分钟前</div>
}

// 幂等 mutation：clientId 保证重放不重复
async function createOrderWithRetry(draft) {
  const clientId = crypto.randomUUID()
  try {
    return await api.createOrder({ ...draft, clientId })   // 服务端按 clientId 去重
  } catch (e) {
    if (!navigator.onLine) {
      queueMutation(() => api.createOrder({ ...draft, clientId }))
      return { pending: true, clientId }
    }
    throw e
  }
}
```
