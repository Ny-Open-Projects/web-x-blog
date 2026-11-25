---
title: [TST-024] Vitest 的类型测试（expectTypeOf / toTypeOf）怎么用？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-024：Vitest 的类型测试（expectTypeOf / toTypeOf）怎么用？
**答**：
- 定位：除运行时断言外，Vitest 提供 `expectTypeOf` 做编译期类型断言——验证函数签名、泛型推断、工具类型转换是否符合预期。
- 运行机制：`.toBeTypeOf/.toEqualTypeOf` 是「编译期校验 + 运行时 no-op」，类型错误在 `vitest --typecheck` 或 tsc 时暴露；`expectTypeOf(x).not.toBeNever()` 还能防类型退化成 any/never。
- 配置：`test.typecheck: { enabled: true, include: ['**/*.test-d.ts'] }`，类型测试通常与运行时测试分文件（*.test-d.ts）。
- 典型场景：测试泛型工具（API 层的类型推导、useXxx hook 的返回类型）、防止 `as any` 污染公共类型。
- 追问钩子：expectTypeOf 失败时的报错信息可读性差，复杂类型配合 `toPrint()`/tsc 输出排查。

```typescript
// src/api.test-d.ts
import { it, expectTypeOf } from 'vitest';
import { fetchUser } from './api';   // fetchUser(id: number): Promise<User>

it('fetchUser 返回类型推导正确', () => {
  expectTypeOf(fetchUser).parameter(0).toBeNumber();
  expectTypeOf(fetchUser(1)).resolves.toMatchTypeOf<{ id: number; name: string }>();
});

it('Partial 转换正确', () => {
  type P = Partial<{ a: number; b: string }>;
  expectTypeOf<P>().toEqualTypeOf<{ a?: number; b?: string }>();
});
// 运行：npx vitest --typecheck
```
