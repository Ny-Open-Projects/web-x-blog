---
title: [909] TanStack Query 的请求取消与竞态治理
date: 2026-11-17
categories: [状态管理新范式]
tags: [前端面试, 面试题, TanStack Query, 竞态]
type: 面试题
---

## 909：TanStack Query 的请求取消与竞态治理

**答**：
- 内置竞态保护：同 Key 并发请求只保留最后结果（key 变更自动取消旧请求）——但手动触发（按钮搜索）需要显式 cancelQueries；mutation 无内置竞态（连续提交两次），需防抖或幂等键。
- 统一取消场景：路由离开取消（abort 信号透传）、输入搜索防抖后取消上一次、乐观更新的 cancelQueries（防旧响应覆盖乐观值）。
- AbortSignal 透传：queryFn 接收 signal 传给 fetch——大型应用必须全程透传（不透传的取消是假取消：状态清理了但网络请求还在烧带宽）。
- 追问钩子：取消后组件重新挂载会重新请求吗？——会（取消的请求无结果缓存），这正是期望行为；gcTime 内有旧数据会先展示旧数据（stale-while-revalidate），不白屏。

```ts
const q = useQuery({
  queryKey: ['search', keyword],
  queryFn: ({ signal }) => fetch('/api/search?q=' + keyword, { signal }),
});
// mutation 防竞态：幂等键
const m = useMutation({
  mutationFn: v => submit({ ...v, idemKey: genIdem(v) }),
});
```

