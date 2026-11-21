---
title: [TS-118] 如何为 CSV/Excel 表头设计行对象映射类型？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-118：如何为 CSV/Excel 表头设计行对象映射类型？
**答**：
- 表头数组 `as const` 后，`typeof HEADERS[number]` 得到表头名联合；`Record<Header, string>` 得到一行记录类型。
- 表头到字段名的映射也用 `as const`，配合条件类型把"中文表头对象"转成"英文字段对象"。
- 好处：表头改名时编译期立刻暴露所有依赖处，杜绝运行时 undefined。

```typescript
const HEADERS = ["姓名", "年龄", "邮箱"] as const;
type Header = typeof HEADERS[number]; // "姓名" | "年龄" | "邮箱"

type CsvRow = Record<Header, string>; // 一行必须包含全部表头

const HEADER_TO_FIELD = {
  "姓名": "name",
  "年龄": "age",
  "邮箱": "email",
} as const;

type FieldMap = typeof HEADER_TO_FIELD;
type Field = FieldMap[Header]; // "name" | "age" | "email"
type ParsedRow = { [K in Field]: string }; // { name: string; age: string; email: string }

function parseCsvRow(row: CsvRow): ParsedRow {
  return Object.fromEntries(
    Object.entries(row).map(([h, v]) => [HEADER_TO_FIELD[h as Header], v])
  ) as ParsedRow;
}

const row: CsvRow = { "姓名": "张三", "年龄": "18", "邮箱": "a@b.c" };
const parsed = parseCsvRow(row);
parsed.name; // string，字段名类型安全
```

## 第二十七章 TS 与运行时边界
