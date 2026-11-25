---
title: [ZSM-637] setQueryData 的命令式写缓存：边界与 setQueriesData 的批量匹配
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-637：setQueryData 的命令式写缓存：边界与 setQueriesData 的批量匹配

**答**：
- `setQueryData(key, updater)` 直接写缓存：status 变 success、dataUpdatedAt 刷新、observer 立即通知。三种用途：1) 乐观更新（写本地预期值）；2) 服务端返回的关联数据顺手写入（如登录响应里的 user 信息写进 `['me']` 缓存，省一次请求）；3) WS 推送更新某条数据。
- updater 的函数形态 `(old) => new`：old 为 undefined 时 updater 不执行（**必须在缓存已有条目时才生效**）——想「无则创建」要带第三参 `{ updatedAt }` 或先用 ensureQueryData 建条目。
- `setQueriesData(filter, updater)` 批量：按过滤器命中多个缓存一起更新（如改用户名后所有含 user 的缓存统一 patch）——注意 updater 收到的是各缓存的旧数据，要防御结构差异。
- 边界与风险：1) **命令式写缓存绕过了「服务端权威」**——写错的数据会在 staleTime 内被展示，必须只在「确知正确值」时写；2) 写缓存后是否 refetch 由是否 stale 决定，想要「立即对账」用 invalidateQueries；3) 命令式写入多起来，数据流向就乱（谁改的不知道）——团队规范：只允许在 mutation 的 onSuccess/onMutate 里写缓存，组件里禁止。
- 追问钩子：setQueryData 与 select 的交互——select 是「读取时转换」，写缓存永远写「原始形态」。

```javascript
// 基本用法
queryClient.setQueryData(['todo', id], (old) => ({ ...old, done: true }))

// 无条目时的坑
queryClient.setQueryData(['unknown'], (old) => old ?? { fresh: true })  // updater 不执行！
queryClient.setQueryData(['unknown'], { fresh: true })                  // 直接赋值：可创建

// 批量更新：用户改名后所有含该用户的缓存
queryClient.setQueriesData(
  { queryKey: ['user'] },   // 前缀匹配 ['user', x]
  (old) => old ? { ...old, name: '新名字' } : old
)

// WS 推送更新（服务端消息驱动）
ws.on('todo.updated', (payload) => {
  queryClient.setQueryData(['todo', payload.id], payload)     // 确知正确值：直接写
  // 不确定影响面时：invalidateQueries({ queryKey: ['todo', payload.id] })
})

// 团队规范示例
// ✓ 允许：mutation 钩子里写
useMutation({
  onSuccess: (newUser) => queryClient.setQueryData(['me'], newUser),  // 关联数据顺手写
})
// ✗ 禁止：组件任意位置 setQueryData（数据流不可追踪）
```
