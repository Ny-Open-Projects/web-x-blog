---
title: [MFW-657] Monorepo shared 组件的 SSR 污染
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-657：Shared 组件的 SSR 污染

**答**:
- shared 组件的 SSR 污染场景：1) **server-only 的代码进 client bundle**（shared 包导出 db 函数——client import barrel 拿到全部 RBL-613 barrel 逃逸）；2) **全局状态污染**（shared 包的模块级变量——SSR 多请求共享同一模块实例（Node 进程单例——请求 A 的状态泄漏到请求 B——AsyncLocalStorage 修复 RBL-519）；3) **样式全局泄漏**（shared CSS 的全局选择器——多 App 共享时的污染 RBL-766）。
- 污染的检测：1) client bundle 的 server 模块扫描（RBL-780）；2) SSR 并发请求的状态测试（并发渲染两请求——状态互不污染的断言：`Promise.all([render(reqA), render(reqB)])` 且结果独立）；3) shared 包的 lint（模块级可变状态禁止—— ESLint no-module-level-mutation）。
- 修复模式：ALS 上下文（请求级状态）+ 纯函数组件（无模块级 mutable）。
- 追问钩子：为什么「shared 包的模块级状态」在 SSR 下是并发定时炸弹？——模块级变量 = 进程单例（Node 进程处理多请求共享同一模块实例）；请求 A 写 state=1 → 请求 B 读到 A 的 state（数据串包——安全事件）；dev 单请求看不出（串行）；生产并发下爆发（RBL-956 静默清单的 SSR 版）；「SSR 的并发模型」：每请求隔离（ALS）是唯一正确姿势——模块级 mutable 在 SSR 中永不安全。

```typescript
// 反模式：shared 包模块级状态
// packages/shared/src/user-context.ts
let currentUser: string | null = null;                   // 模块级 mutable！
export function setCurrentUser(u: string) { currentUser = u; }
export function getCurrentUser() { return currentUser; }
// SSR 并发：请求 A setCurrentUser('a') → 请求 B getCurrentUser() 返回 'a'（串包！）

// 修正：ALS
import { AsyncLocalStorage } from 'node:async_hooks';
const als = new AsyncLocalStorage<{ user: string }>();
export function runWithUser<T>(user: string, fn: () => T): T {
  return als.run({ user }, fn);
}
export function getCurrentUser() {
  return als.getStore()?.user ?? null;                   // 请求级隔离
}
// 渲染入口
export async function handle(req) {
  const user = await auth(req);
  return runWithUser(user, () => renderPage(req));        // ALS 上下文包裹渲染
}
// 并发测试
test('no state leak', async () => {
  const [a, b] = await Promise.all([
    runWithUser('alice', async () => { await sleep(10); return getCurrentUser(); }),
    runWithUser('bob', async () => { await sleep(5); return getCurrentUser(); }),
  ]);
  expect(a).toBe('alice'); expect(b).toBe('bob');        // 互不污染
});
```
