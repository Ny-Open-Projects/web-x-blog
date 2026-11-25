---
title: [ZSM-049] Jotai 异步 atom 抛错后组件会一直卡住吗？ErrorBoundary 与重试怎么设计？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-049：Jotai 异步 atom 抛错后组件会一直卡住吗？ErrorBoundary 与重试怎么设计？
**答**：
- 异步 atom reject 后，读取该 atom 的组件抛出错误，若没有 ErrorBoundary 整个子树卸载崩溃；有 EB 则展示 fallback。
- EB 不能自动重试：需要给派生链加「刷新信号」（刷新计数 atom）或用 `atomWithRetry` 模式，reset 计数后 atom 重新求值。
- 推荐生产写法：异步 atom 统一返回 Result 结构 `{ status, data, error }`，UI 层不依赖 Suspense/EB 的隐式行为，错误可控可测。
- Suspense 方案适合「首屏骨架屏」，交互型页面更倾向 loadable/Result 显式三态。

```javascript
const retryAtom = atom(0)
const profileAtom = atom(async get => {
  await get(retryAtom)
  try { return { status: 'ok', data: await fetchProfile() } }
  catch (e) { return { status: 'error', error: e } }
})
function Profile() {
  const r = useAtomValue(profileAtom)
  const setRetry = useSetAtom(retryAtom)
  if (r.status === 'error') return <button onClick={() => setRetry(c => c+1)}>重试</button>
  return <Avatar user={r.data} />
}
```
