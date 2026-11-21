---
title: [TST-014] setupFiles 是干什么的？哪些全局设置适合放进 setup 文件？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-014：setupFiles 是干什么的？哪些全局设置适合放进 setup 文件？
**答**：
- 作用：每个测试文件执行前统一运行的引导脚本（相当于 Jest 的 setupFilesAfterEach），测试环境层面的公共配置都收口在这里。
- 典型内容：引入 `@testing-library/jest-dom` 断言扩展、MSW `setupServer` 并 `server.listen()`、mock matchMedia/ResizeObserver 等 jsdom 缺失 API、配置 ESLint 禁 only。
- 全局钩子：setup 里写的 `afterEach(server.resetHandlers)` / `afterEach(cleanup)` 对所有文件生效，避免每个测试重复写。
- 注意：setupFiles 每个测试文件各跑一次（文件隔离），所以其中变量不是跨文件共享的；跨文件共享用 globalSetup。
- 追问钩子：`setupFiles` 在测试框架安装前执行（导入了 vitest 的钩子 API 用 setupFiles）；纯注入全局变量可走 `test.env` 或 globals。

```typescript
// vitest.setup.ts
import '@testing-library/jest-dom/vitest';
import { server } from './__mocks__/msw-server';
import { afterEach, beforeAll, afterAll } from 'vitest';

beforeAll(() => server.listen({ onUnhandledRequest: 'error' })); // 未匹配请求直接报错，防漏 mock
afterEach(() => {
  server.resetHandlers();           // 用例间清掉临时 handler
});
afterAll(() => server.close());

// jsdom 缺的 API 兜底
if (!window.matchMedia) {
  window.matchMedia = (q) => ({ matches: false, media: q, addListener() {}, removeListener() {} } as any);
}
// vitest.config.ts: test: { setupFiles: ['./vitest.setup.ts'] }
```
