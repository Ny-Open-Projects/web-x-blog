---
title: [ZSM-087] useMutation 的回调族（onMutate/onSuccess/onError/onSettled）执行顺序和各自职责是什么？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-087：useMutation 的回调族（onMutate/onSuccess/onError/onSettled）执行顺序和各自职责是什么？
**答**：
- 顺序：mutate 调用 → onMutate（乐观写/取消在途/做快照，返回值进 context）→ mutationFn → 成功 onSuccess / 失败 onError → 总会执行的 onSettled。
- context 传递：onMutate 返回对象，onError/onSettled 第三参收到，用于回滚快照。
- 双层注册：useMutation 里的回调是实例级；全局 mutationCache 的 onSuccess/onError 做横切（上报、统一 toast）——两者都跑，实例级先。
- mutate vs mutateAsync：mutate 吞错走 onError；mutateAsync 抛异常由 try/catch 接管，适合在 async 流程里编排，但要自己兜错误防 unhandled rejection。

```javascript
const m = useMutation({
  mutationFn: api.submit,
  onMutate: async v => { /* 乐观 */ return { prev } },
  onSuccess: (res, v) => toast.success('已提交'),
  onError: (e, v, ctx) => { qc.setQueryData(['list'], ctx.prev); toast.error('失败已回滚') },
  onSettled: () => qc.invalidateQueries({ queryKey: ['list'] }), // 无论如何对齐
})
```
