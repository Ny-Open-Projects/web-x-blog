---
title: [TS-181] getter/setter 访问器的类型有哪些规则？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-181：getter/setter 访问器的类型有哪些规则？
**答**：
- TS 4.3+ 支持读写不同类型：get 返回 number、set 接收 string | number 是合法组合。
- 接口层用 `get x(): T; set x(v: U)` 成对表达访问器契约。
- 访问器让"内部存储形状"与"对外契约"解耦，是运行时适配层的类型化表达。

```typescript
class Temperature {
  private celsiusValue = 0;

  get celsius(): number { return this.celsiusValue; }
  set celsius(v: number) { this.celsiusValue = v; }

  // 读窄写宽的合法组合
  get raw(): number { return this.celsiusValue; }
  set raw(v: string | number) { this.celsiusValue = Number(v); }
}

// 接口层同样成对表达
interface TemperatureLike {
  get celsius(): number;
  set celsius(v: number);
}

const t = new Temperature();
t.celsius = 36;              // set: number
const c: number = t.celsius; // get: number
// const bad: string = t.celsius; // 报错
```

## 第三十七章 严格度与错误治理（TS-182 ~ TS-187）
