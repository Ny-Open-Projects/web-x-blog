---
title: [TST-028] 只想 mock 模块的部分导出怎么办？importActual / partial mock 怎么用？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-028：只想 mock 模块的部分导出怎么办？importActual / partial mock 怎么用？
**答**：
- 需求场景：utils 模块有 10 个导出，只想换掉 `fetchData`，其余保持真实现——全量 mock 会让其他用例失效。
- 三种写法：① 工厂里展开 `importActual` 结果再覆盖单个导出；② 对象字面量展开真模块（小模块直接 import 真值再展开）；③ `vi.spyOn(模块命名空间, 'fn')` 部分替换（需模块可拿到实例）。
- importActual 提升规则：`vi.importActual` 本身不会被提升处理，可在工厂内调用拿到真实模块。
- 注意：部分 mock 后被覆盖的导出仍是 mock，记得 reset；被测代码若按命名空间 `import * as` 引用，spyOn 路径才生效。
- 追问钩子：CJS 的 require 顶层缓存、ESM 的绑定语义，决定了 spy 能否生效——ESM 具名导出是只读绑定，spyOn 命名空间对象仅对 Vitest 转换后的引用有效。

```typescript
import { describe, it, expect, vi } from 'vitest';

// ① importActual 保留全部真实现，仅覆盖 fetchData
vi.mock('./utils', async (importOriginal) => {
  const actual = await importOriginal<typeof import('./utils')>();
  return { ...actual, fetchData: vi.fn() };
});

import { fetchData, formatDate } from './utils'; // fetchData 是 mock，formatDate 是真的

describe('部分 mock', () => {
  it('其他导出仍是真实现', () => {
    expect(formatDate(new Date('2026-01-01'))).toBe('2026-01-01'); // 真实逻辑
    vi.mocked(fetchData).mockResolvedValue({ ok: true });
    expect(fetchData).toBeTypeOf('function');
  });
});
```
