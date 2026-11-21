---
title: [BAS-114] TypeScript 函数重载怎么写？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-114：TypeScript 函数重载怎么写？
**答**：
- 重载签名只声明不实现，列出各调用形态；最后是实现签名，参数类型要兼容所有形态。
- 调用时按签名从上到下匹配；实现内部需自行用 typeof 收窄参数。
- 只在"同一函数不同入参形态且返回类型随入参变化"时用，滥用不如联合类型直观。

```typescript
function parse(input: string): string[];
function parse(input: number): string;
function parse(input: string | number): string[] | string {
  return typeof input === 'string' ? input.split(',') : String(input * 100);
}
const a = parse('a,b');   // string[]
const b = parse(1.23);    // string
```
