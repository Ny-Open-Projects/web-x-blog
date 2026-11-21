---
title: [TST-029] 测试里怎么切换环境变量？vi.stubEnv 怎么用？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-029：测试里怎么切换环境变量？vi.stubEnv 怎么用？
**答**：
- 问题：代码读 `import.meta.env.VITE_API_HOST` 或 `process.env.NODE_ENV` 做分支，测试要覆盖不同环境（dev/prod 行为不同、灰度开关）。
- 方案：`vi.stubEnv('NODE_ENV', 'production')` 注入；配 `vi.unstubAllEnvs()` 或 config `unstubEnvs: true` 在每条用例后自动还原。
- 细节：Vitest 会同时同步 process.env 与 import.meta.env；stubEnv 置空串可模拟「未设置」；对 `import.meta.env.PROD` 这类编译期常量也按 NODE_ENV 推导。
- 反模式：直接 `process.env.X = 'y'` 不还原，导致后续用例读到脏值（顺序依赖 bug 的典型来源）。
- 追问钩子：构建期注入的 define 常量（Vite define）测试里靠 alias/mock 被测模块解决，stubEnv 管不到。

```typescript
import { describe, it, expect, vi, afterEach } from 'vitest';
import { apiHost } from './host';

afterEach(() => vi.unstubAllEnvs());

describe('按环境取 API 域名', () => {
  it('生产环境走正式域名', () => {
    vi.stubEnv('NODE_ENV', 'production');
    expect(apiHost()).toBe('https://api.example.com');
  });
  it('开发环境走测试域名', () => {
    vi.stubEnv('NODE_ENV', 'development');
    expect(apiHost()).toBe('http://localhost:3000');
  });
});
```
