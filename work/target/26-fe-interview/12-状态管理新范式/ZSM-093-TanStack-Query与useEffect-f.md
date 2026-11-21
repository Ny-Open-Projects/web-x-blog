---
title: [ZSM-093] 为什么「useEffect + fetch + useState」应该被 TanStack Query 取代？列出五个具体痛点
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-093：为什么「useEffect + fetch + useState」应该被 TanStack Query 取代？列出五个具体痛点
**答**：
- 竞态：快速切换参数时旧响应覆盖新响应，需手动 AbortController/序号——Query 按 key 天然隔离。
- 去重：同参数多组件同时请求会打多次接口——Query 同 key 合并并发。
- 缓存与重取：离开页面回来就重新 loading——Query 有 staleTime/gcTime/后台刷新。
- 重试与错误：手写 retry/错误分类/上报样样要自己造——Query retry + QueryCache 层统一。
- 生命周期：StrictMode 双挂载双请求、卸载后 setState 警告、取消逻辑散落——Query 统一管理观察者。
- 追问钩子：useEffect fetch 还有「数据与缓存无关联，无法失效协作」的架构级问题。

```javascript
// 旧写法的竞态隐患
useEffect(() => {
  let alive = true
  api.goods(kw).then(d => { if (alive) setList(d) }) // 手动防卸载 + 手动防竞态
  return () => { alive = false }
}, [kw])
// Query 版：一个声明全解决
const { data } = useQuery({ queryKey: ['goods', kw], queryFn: () => api.goods(kw) })
```
