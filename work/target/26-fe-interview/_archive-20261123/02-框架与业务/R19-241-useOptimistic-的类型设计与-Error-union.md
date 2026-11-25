---
title: [R19-241] useOptimistic 场景的类型设计（Result union）怎么做？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-241：useOptimistic 场景的类型设计（Result union）怎么做？
**答**：
- action 返回 discriminated union：`type Ok = { ok: true; data } | { ok: false; code: ErrorCode; fieldErrors? }`，前端用 narrowing 处理，杜绝「先 access 再判断」。
- 乐观操作类型同样 union：`{ type: 'add', item } | { type: 'toggle', id, checked } | { type: 'remove', id }`，reducer 用 switch exhaustive check（never 兜底）。
- 泛型复用：`useActionState<TInput, TResult>` 与 Result<T> 组合，action 层到 UI 层类型贯通。
- 收益：错误码新增时编译器强制处理，避免运行时 undefined。
```javascript
type Result<T> = { ok: true; data: T } | { ok: false; code: 'AUTH' | 'VALIDATION' | 'CONFLICT'; fieldErrors?: Record<string, string> }
```
