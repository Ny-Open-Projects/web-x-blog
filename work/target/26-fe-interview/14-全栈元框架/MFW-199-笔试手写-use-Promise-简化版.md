---
title: [MFW-199] 笔试：手写 use(Promise) 的简化版（挂起与缓存）
date: 2026-11-19
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-199：笔试：手写 `use(Promise)` 的简化版（挂起与缓存）
**答**：React 的 `use(promise)` 在渲染期间读取 Promise：pending 时抛出 promise 让 Suspense 接管，resolve 后返回值，reject 时抛给 ErrorBoundary。实现简化版：① 同一个 promise 组件重渲染时不重复订阅（结果缓存挂在 promise 上）；② pending 抛出原 promise（Suspense 靠引用稳定去重，不能每次抛新 promise）；③ resolve 后返回 value；④ reject 后抛出错误（只抛一次，后续重渲染抛同样的错误）；⑤ 不允许在 try/catch 里捕获挂起信号（调用方误用时给出可读报错）。

```tsx
type Status = 'pending' | 'ok' | 'err';
interface Wrapped<T> {
  status: Status; value?: T; error?: unknown;
}

export function useFake<T>(promise: Promise<T>): T {
  const w = (promise as any).__wrapped as Wrapped<T> | undefined;
  const record: Wrapped<T> = w ?? (promise as any).__wrapped = { status: 'pending' }; // ① 状态挂 promise 上

  if (record.status === 'ok') return record.value as T;         // ③
  if (record.status === 'err') throw record.error;              // ④ 稳定抛同一错误

  record.then(
    (value: T) => { record.status = 'ok'; record.value = value; },
    (error: unknown) => { record.status = 'err'; record.error = error; },
  );
  // ⑤ 用 Error 标记挂起信号，误被 try/catch 吞掉时提示更可读
  const suspension = new Error(
    'A component suspended while responding to synchronous input. ' +
    'This will cause the UI to be replaced with a loading indicator.',
  );
  (suspension as any).then = record.then; // React 内部靠 promise 的 then 恢复
  throw suspension;                        // ② 同一 promise → 同一引用 → Suspense 去重
}

// 用法
function Profile({ userPromise }: { userPromise: Promise<{ name: string }> }) {
  const user = useFake(userPromise); // pending → Suspense fallback
  return <h1>{user.name}</h1>;
}
```

**评分点**：
1. 状态缓存在 promise 对象上（而非组件 state）：同一 promise 多次 use 是幂等的，重渲染不重复订阅。
2. pending 时抛出的挂起信号引用稳定（React 靠 promise 身份做 Suspense 去重），每次抛新 promise 会导致 fallback 闪烁。
3. 错误只记录一次、稳定重抛：reject 后重渲染必须抛同一错误，避免错误边界状态漂移。
4. resolve/reject 都要更新 record 状态后才能让重渲染拿到终值——能说出「需要一次调度触发重渲染」是加分（真实实现靠 internal scheduler）。
5. 知道真实 use() 的额外约束：可以在渲染中调用但不能在事件回调中、不能 try/catch 吞掉 promise 挂起。