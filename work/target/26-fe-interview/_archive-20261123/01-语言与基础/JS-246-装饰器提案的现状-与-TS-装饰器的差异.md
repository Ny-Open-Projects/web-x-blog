---
title: [JS-246] 装饰器提案的现状：与 TS 装饰器的差异
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 新特性]
type: 面试题
---

## JS-246：装饰器提案现状与 TS 装饰器差异

**答**：
- 生态并存两代：legacy（TS experimentalDecorators，Angular/NestJS 在用）与标准版（ES 装饰器提案 stage 3，TS 5.0 默认）
- 标准版差异：装饰对象是「明确的语法元素」（方法/字段/accessor/class），参数结构不同；不能装饰任意表达式；元数据靠 decorator metadata 提案另补
- 能力定位：方法包装（日志/重试/防抖）、字段初始化 hook、类包装（mixins）——不能改变运行时调用约定（legacy 的复杂魔法写不了）
- 实用建议：新项目 TS 5 用标准版；与 Angular 生态对接时仍用 legacy；运行时注解系统（NestJS 风格 DI）需要 legacy + reflect-metadata
- 面试话术：说出「两代并存、按生态选版本」即是熟悉者

```typescript
// 标准版装饰器：方法计时
function timed(target, { name }, descriptor) {
  const orig = descriptor;
  return {
    ...orig,
    async method(...args) { /* 包装实现 */ },
  };
}
class Api {
  @timed
  async fetchUser(id: string) { /* ... */ }
}
```
