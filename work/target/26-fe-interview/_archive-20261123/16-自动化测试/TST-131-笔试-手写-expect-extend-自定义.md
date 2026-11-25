---
title: [TST-131] 笔试：手写 expect.extend 自定义 matcher（toBeWithinRange + 异步版）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-131：笔试：手写 expect.extend 自定义 matcher（toBeWithinRange + 异步版）
**答**：
- 需求：用 Vitest/Jest 的 `expect.extend` 实现两个自定义断言：① `toBeWithinRange(floor, ceiling)`（数字区间，支持 .not）；② `toSubmitWith(expectedBody)`——断言某请求被以指定 body 发出（收集型断言，配合 mock 捕获）。
- matcher 规范：返回 `{ pass, message }`；message 必须同时适配正反两种语境（`.not` 时文案反转，用 `this.utils.printReceived` 输出带颜色的实际值）；异步 matcher 返回 Promise 或直接用 `expect.poll`。
- 常见丢分点：message 只写了正向文案导致 `.not` 时报错信息莫名其妙；忘记处理非 number 输入；类型声明没给（TS 项目里 matcher 要模块扩展 declaration）。

```javascript
// matchers.ts
import { expect } from 'vitest';

expect.extend({
  toBeWithinRange(received, floor, ceiling) {
    const pass = typeof received === 'number' && received >= floor && received <= ceiling;
    return {
      pass,
      message: () =>
        pass
          ? `expected ${received} NOT to be within range ${floor}..${ceiling}`  // .not 语境
          : `expected ${received} to be within range ${floor}..${ceiling}`,
    };
  },

  toSubmitWith(receivedSpy, expectedBody) {
    const calls = receivedSpy.mock.calls.map((c) => c[0]);       // 收集所有请求体
    const pass = calls.some((body) => JSON.stringify(body) === JSON.stringify(expectedBody));
    return {
      pass,
      message: () =>
        `expected fetch to be called with body\n  ${JSON.stringify(expectedBody, null, 2)}\n` +
        `received bodies:\n  ${JSON.stringify(calls, null, 2)}`,
    };
  },
});

// ---- 用法 ----
test('区间断言', () => {
  expect(85).toBeWithinRange(60, 100);
  expect(50).not.toBeWithinRange(60, 100);
});

// 类型扩展（matcher.d.ts）
// interface Matchers<R> {
//   toBeWithinRange(floor: number, ceiling: number): R;
//   toSubmitWith(expectedBody: unknown): R;
// }
```

**评分点**：
1. 返回 `{ pass, message }` 结构正确，message 是函数（惰性求值）。
2. `.not` 语境文案正确反转（高频丢分点）。
3. 异常输入（非 number）不抛错而是 pass=false。
4. TS 项目给出 Matchers 接口扩展声明（类型完整度）。
