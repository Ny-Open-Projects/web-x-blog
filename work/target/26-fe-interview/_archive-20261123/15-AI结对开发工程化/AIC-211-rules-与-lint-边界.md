---
title: [AIC-211] 哪些规范该进 Cursor rules，哪些该进 ESLint？两者边界怎么划？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-211：哪些规范该进 Cursor rules，哪些该进 ESLint？两者边界怎么划？
**答**：
- 可静态判定的（语法/模式级）进 lint：no-var、import 顺序、禁用 API——机器能 100% 判断。
- 需要语义判断的进 rules：分层架构约束、命名背后的领域含义、「什么时候该抽象」。
- 灰色地带看误报率：lint 规则误报高就降级为 rules 引导。
- 铁律：AI 产出必须过 lint，所以 lint 是底线，rules 是提效。

```javascript
const boundary = {
  eslint: ['no-var', 'no-console', 'import/order', 'no-restricted-imports'], // 静态可判
  rules: ['服务端数据必须经 hooks 层消费', '错误处理优先用 Result 类型而非 throw',
          '提取组件的时机（三处重复再抽）'],                              // 语义判断
  fallback: 'lint 误报率 > 20% 的规则 → 降级为 rules 引导 + code review 提示',
};
r
```
