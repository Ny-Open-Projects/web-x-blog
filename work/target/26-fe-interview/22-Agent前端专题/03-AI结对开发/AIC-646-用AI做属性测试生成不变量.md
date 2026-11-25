---
title: [AIC-646] 让 AI 写属性测试，怎么帮它找到「不变量」？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-646：让 AI 写属性测试，怎么帮它找到「不变量」？

**答**：
- 结论先行：**属性测试（Property-Based Testing）的关键是「不变量」——对任意输入都成立的性质**（如「排序后长度不变」「序列化再反序列化等于原值」）。AI 不擅长凭空发现不变量，但擅长在人的引导下把不变量翻译成生成器与断言。
- 什么是不变量：不是「某个具体输入输出」（那是例子测试），而是「一类输入都满足的规律」。例：商品列表「无论多少条数据，筛选后的结果一定是原列表的子集」。
- 让 AI 生成的方法：1) **人给规律，AI 写代码**：人说清不变量，AI 生成 fast-check 的 arbitrary（生成器）+ property 断言；2) **从类型/文档推断**：让 AI 读函数签名与注释，列出候选不变量，人筛选；3) **从 bug 反推**：每个历史 bug 对应一条被违反的不变量，让 AI 提炼（AIC-655）。
- 生成器质量是难点：AI 常写出「只生成正常值」的生成器（如只生成正数），漏掉边界（0、负数、空、极大）。要显式要求生成器覆盖边界与脏数据（AIC-059 mock 规范）。
- 追问钩子：为什么属性测试比例子测试更能发现 AI 代码的 bug？——因为例子测试只覆盖人想到的几个点，而属性测试用随机生成覆盖成百上千种输入组合；AI 代码常在「没想到的边界」出错，属性测试恰好专打这些盲区。

```typescript
// 用 fast-check 风格：不变量「排序不改变元素集合与长度」
type Arbitrary<T> = { generate: () => T };

function checkProperty<T>(
  arb: Arbitrary<T[]>,
  property: (input: T[]) => boolean,
  runs = 100,
): { passed: boolean; counterexample?: T[] } {
  for (let i = 0; i < runs; i++) {
    const input = arb.generate();
    if (!property(input)) return { passed: false, counterexample: input };
  }
  return { passed: true };
}

const intArb = { generate: () => Array.from({ length: 5 }, () => Math.floor(Math.random() * 100)) };
const result = checkProperty(intArb, xs => {
  const sorted = [...xs].sort((a, b) => a - b);
  return sorted.length === xs.length
    && [...sorted].sort((a, b) => a - b).join(',') === [...xs].sort((a, b) => a - b).join(',');
});
console.log(result.passed); // true —— 排序不变量成立
```
