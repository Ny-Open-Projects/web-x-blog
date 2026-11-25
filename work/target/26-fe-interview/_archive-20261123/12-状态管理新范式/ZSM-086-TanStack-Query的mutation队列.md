---
title: [ZSM-086] TanStack Query 的 mutation 有队列吗？并发 mutate 和 mutationKey/mutationScope 串行怎么实现？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-086：TanStack Query 的 mutation 有队列吗？并发 mutate 和 mutationKey/mutationScope 串行怎么实现？
**答**：
- 每个调用 mutate 默认并发执行、互不排队；连续点「发布评论」会发 N 个请求。
- 需要串行（如文件顺序上传）：`mutationKey: ['upload']` + `scope: { id: 'upload' }`，同 scope 的 mutation 自动排队逐个执行。
- 队列化后 `isPaused/isPending` 反映当前队列状态；配合乐观更新时，串行保证缓存写顺序可预测。
- 不需要串行时别滥用：队列会拖慢体验，多数接口天然可并发。

```javascript
const upload = useMutation({
  mutationKey: ['upload'],          // v5 里 scope 需配 key
  mutationFn: api.upload,
  scope: { id: 'upload' },          // 同 id 串行排队
})
// upload.mutate(f1); upload.mutate(f2); upload.mutate(f3) → 依次执行
```
