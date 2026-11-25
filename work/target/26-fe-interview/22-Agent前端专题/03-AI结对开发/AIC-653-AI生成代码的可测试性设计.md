---
title: [AIC-653] 怎么引导 AI 写出「可测试」的代码？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-653：怎么引导 AI 写出「可测试」的代码？

**答**：
- 结论先行：**可测试性不是测出来的，是设计出来的——让 AI 写「纯函数 + 依赖注入 + 单一职责」，测试自然好写**。如果 AI 写出「组件里直接调 API + 一堆内部状态」，测试就得疯狂 mock，测的全是 mock 逻辑（AIC-236 mock 过度）。
- 三个设计原则喂给 AI：1) **纯函数优先**：业务逻辑抽成纯函数（输入→输出，无副作用），组件只做渲染——纯函数无需 mock，直接断言；2) **依赖注入**：API 调用、时间、随机数通过参数传入（而非模块内直接 import/调用），测试时注入桩；3) **单一职责**：一个函数做一件事，职责单一才能针对性测试。
- 在 rules 里写死：例如「数据转换逻辑必须抽成独立纯函数文件 xxx.utils.ts」「时间获取用注入的 now() 而非 Date.now()」——把可测试性变成团队规范（AIC-510 rules 设计模式）。
- 验收把关：review 时看「这个函数好测吗」——如果一个简单逻辑需要 5 个 mock，说明设计有问题，让 AI 重构而非补更多 mock。
- 追问钩子：为什么「依赖注入」能减少 mock 过度？——因为直接 import 的依赖无法替换，测试只能 mock 整个模块（连带着把不该 mock 的也 mock 了）；注入后只替换那一个依赖，测试更精确、更接近真实逻辑——mock 越少，测试越可信。

```typescript
// 反例：不可测试 —— 组件内直接调 API + 用当前时间
// function Price() { const p = await fetch('/api/price'); const expired = Date.now() > ... }

// 正例：纯函数 + 依赖注入
interface Deps { fetchPrice: (id: string) => Promise<number>; now: () => number }

// 纯业务逻辑：无副作用，直接测
export function calcDiscount(price: number, now: number, expiry: number): number {
  return now > expiry ? price : price * 0.9;
}

// 组件只编排，依赖通过参数注入
export async function loadPrice(id: string, deps: Deps) {
  const price = await deps.fetchPrice(id);
  return { price, discounted: calcDiscount(price, deps.now(), Date.now() + 86400000) };
}

// 测试：注入桩，无需 mock 模块
console.log(calcDiscount(100, 200, 100)); // 100 —— 已过期不打折
console.log(calcDiscount(100, 50, 100));  // 90 —— 打折
```
