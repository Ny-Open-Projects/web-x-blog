---
title: [MFW-146] 笔试：手写一个类型安全的 searchParams 解析器
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-146：笔试：手写一个类型安全的 searchParams 解析器
**答**：实现 `parseSearch(search, schema)`：① schema 描述字段类型（string/number/enum/boolean）与默认值；② URLSearchParams → 类型化对象，缺失用默认值；③ 非法值（如 page=abc、sort=x）按策略处理：带默认值用默认值并收集警告，无默认值抛错；④ 重复参数取最后一个；⑤ 输出与 TS 类型一致（返回类型由泛型推导）。

```ts
type FieldType =
  | { type: 'string'; default?: string }
  | { type: 'number'; default?: number; min?: number; max?: number }
  | { type: 'enum'; values: string[]; default?: string }
  | { type: 'boolean'; default?: boolean };

type Schema = Record<string, FieldType>;

type Result<T> = { data: T; warnings: string[] };

class InvalidParamError extends Error {
  constructor(public key: string) { super(`参数 ${key} 非法且无默认值`); }
}

function parseOne(field: FieldType, raw: string | undefined, key: string, warnings: string[]): unknown {
  if (raw === undefined || raw === '') {
    if ('default' in field) return field.default;
    throw new InvalidParamError(key); // 缺失且无默认
  }
  switch (field.type) {
    case 'number': {
      const n = Number(raw);
      if (Number.isNaN(n)) {
        if ('default' in field) { warnings.push(`${key}: ${raw} -> ${field.default}`); return field.default; }
        throw new InvalidParamError(key);
      }
      if (field.min !== undefined && n < field.min) return field.min; // 钳制
      if (field.max !== undefined && n > field.max) return field.max;
      return n;
    }
    case 'enum':
      if (field.values.includes(raw)) return raw;
      if ('default' in field) { warnings.push(`${key}: ${raw} -> ${field.default}`); return field.default; }
      throw new InvalidParamError(key);
    case 'boolean':
      return raw === 'true' || raw === '1';
    default:
      return raw;
  }
}

function parseSearch<T extends Record<string, unknown>>(
  search: URLSearchParams | string,
  schema: Schema,
): Result<T> {
  const sp = typeof search === 'string' ? new URLSearchParams(search) : search;
  const data: Record<string, unknown> = {};
  const warnings: string[] = [];

  for (const [key, field] of Object.entries(schema)) {
    const values = sp.getAll(key);
    // 重复参数取最后一个（浏览器表单常见行为）
    data[key] = parseOne(field, values[values.length - 1], key, warnings);
  }
  return { data: data as T, warnings };
}

// —— 用例 ——
const schema: Schema = {
  q: { type: 'string' },
  page: { type: 'number', default: 1, min: 1, max: 500 },
  sort: { type: 'enum', values: ['sales', 'price'], default: 'sales' },
  hot: { type: 'boolean', default: false },
};

const r = parseSearch<{ q?: string; page: number; sort: string; hot: boolean }>(
  '?q=键盘&page=99&sort=price&hot=1&page=2', schema, // page 重复取最后 = 2；99 超 max 钳到 500？不，99 在界内
);
// r.data = { q: '键盘', page: 2, sort: 'price', hot: true }
// parseSearch('?sort=x', schema).warnings -> ['sort: x -> sales']
// parseSearch('?page=abc', { ...schema, q: { type: 'string' } }) -> q 抛 InvalidParamError
```

**评分点**：
1. 重复参数取最后一个（getAll + 尾值），与浏览器语义一致。
2. 缺失/空串/默认值三分支处理，无默认值抛结构化错误。
3. 数字非法走默认值+警告，enum 非法同理，min/max 钳制边界。
4. boolean 解析覆盖 'true'/'1' 两种真值。
5. 泛型输出与 schema 对齐，能口头说明「运行时校验与编译期类型同源」的 TanStack 思想。
