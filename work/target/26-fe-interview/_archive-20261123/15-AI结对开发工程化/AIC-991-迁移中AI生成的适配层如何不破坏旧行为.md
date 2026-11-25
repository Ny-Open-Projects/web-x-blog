---
title: [AIC-991] 遗留系统迁移时 AI 生成了一层「新旧接口适配层」，如何保证它没有破坏旧调用方的行为？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-991：遗留系统迁移时 AI 生成了一层「新旧接口适配层」，如何保证它没有破坏旧调用方的行为？
**答**：
- 适配层是迁移的「兼容契约」——结论：它必须以旧调用方为基准做验证，而非以新接口为准。先穷举旧接口的所有调用形态（参数、返回值、错误语义）。
- 用「契约测试 + 回放」双保险：把旧接口的历史真实调用录制成用例，适配层回放这些用例输出必须与旧实现一致；契约测试锁定签名与错误语义。
- 特别注意「隐式行为」：旧接口可能返回 undefined 而非抛错、参数顺序特殊、有副作用——AI 生成的规范适配层常把这些「不规范但被依赖」的行为改掉，导致隐性破坏。
- 追问钩子：能说出「适配层的价值是『让旧调用方无感』，验证标准应是旧调用方的全部既有行为，而非新系统的理想行为」的候选人抓住了兼容的本质。

```typescript
// 适配层回放校验：以旧调用方行为为基准
const oldCalls = [ // 历史真实调用录制
  { args:['A001'], expect:{ price:100, currency:'CNY' } },
  { args:['BAD'],  expect:null }, // 旧行为：非法 sku 返回 null 而非抛错
];
function oldApi(sku){ return sku==='A001'?{price:100,currency:'CNY'}:null; }
function newApi(sku){ return sku==='A001'?{price:100,currency:'CNY'}:undefined; } // AI写的适配层
function adapter(sku){ const r=newApi(sku); return r===undefined?null:r; } // 修正隐式行为
function verify(calls, impl) {
  return calls.filter(c=>JSON.stringify(impl(...c.args))!==JSON.stringify(c.expect));
}
console.log('旧适配层差异:', verify(oldCalls, newApi).length, '修正后:', verify(oldCalls, adapter).length);
```
