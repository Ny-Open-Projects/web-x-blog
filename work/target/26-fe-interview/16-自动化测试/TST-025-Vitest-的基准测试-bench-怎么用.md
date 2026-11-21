---
title: [TST-025] Vitest 的 benchmark（vitest bench）是什么？什么时候用？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-025：Vitest 的 benchmark（vitest bench）是什么？什么时候用？
**答**：
- 定位：`vitest bench` 跑 `*.bench.ts` 文件，基于 tinybench 做微基准——测的是「多快」，不是「对不对」，用于性能敏感函数的方案对比。
- API：`bench(name, fn, options)`，输出 ops/sec、平均耗时、p75/p99、样本数；`bench.add` 或同文件多个 bench 自动并排对比。
- 使用纪律：样本要预热（tinybench 自动）、避免在 CI 波动环境里拿单次结果当结论；关注相对差异与 p99 而不是均值。
- 典型场景：深拷贝实现对比、正则 vs 手写解析、序列化方案选型——为技术方案评审提供量化证据。
- 追问钩子：bench 不进 CI 门禁（性能波动大），适合本地/基准环境手动跑并记录历史。

```typescript
// src/clone.bench.ts
import { bench, describe } from 'vitest';

const obj = { a: 1, b: { c: [1, 2, 3] }, d: 'text' };

describe('deepClone 方案对比', () => {
  bench('JSON.parse/stringify', () => {
    JSON.parse(JSON.stringify(obj));
  });
  bench('structuredClone', () => {
    structuredClone(obj);
  });
  bench('手写递归', () => {
    const clone = (v) => Array.isArray(v) ? v.map(clone)
      : v && typeof v === 'object' ? Object.fromEntries(Object.entries(v).map(([k, x]) => [k, clone(x)]))
      : v;
    clone(obj);
  });
});
// 运行：npx vitest bench
```
