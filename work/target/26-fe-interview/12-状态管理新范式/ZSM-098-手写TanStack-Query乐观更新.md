---
title: [ZSM-098] 笔试：手写带快照回滚的乐观更新工具（useOptimisticUpdate）
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-098：手写带快照回滚的乐观更新工具（useOptimisticUpdate）

**题目要求**：
- 实现 `useOptimisticUpdate({ key, apply, request })`：调用 `run(payload)` 时 ① 取消在途（简化为忽略）② 快照当前缓存 ③ apply 写入乐观值 ④ 执行 request，成功后 invalidate（标记重取），失败回滚快照。
- 回滚后必须通知订阅者重渲染。

```javascript
function useOptimisticUpdate({ key, apply, request }) {
  const kstr = JSON.stringify(key)
  return async (payload) => {
    const prev = cache.get(kstr)?.data            // 1. 快照
    try {
      cache.set(kstr, { ...(cache.get(kstr) ?? {}), data: apply(prev, payload) })
      emit(kstr)                                  // 2. 乐观渲染
      await request(payload)                      // 3. 真实请求
      const e = cache.get(kstr); if (e) e.stale = true // 4. 失效，等下个订阅周期重取
      emit(kstr)
    } catch (e) {
      cache.set(kstr, { ...(cache.get(kstr) ?? {}), data: prev }) // 5. 回滚
      emit(kstr)
      throw e
    }
  }
}

// 用法：点赞
const like = useOptimisticUpdate({
  key: ['posts'],
  apply: (posts, id) => posts.map(p => p.id === id ? { ...p, liked: true, likes: p.likes + 1 } : p),
  request: id => api.like(id),
})
```

**评分点**：
- 快照在乐观写之前取，回滚还原的是「本次操作前」的状态。
- 乐观写后主动 emit 通知 UI（若忘记 emit，乐观更新无效）。
- 失败回滚 + 错误继续抛出（调用方可 toast）。
- 成功后标记 stale 而不是直接删除缓存，保持先显旧数据。
- 能指出并发多次 run 会互相覆盖快照，需按调用序号维护快照栈（答出加分）。
